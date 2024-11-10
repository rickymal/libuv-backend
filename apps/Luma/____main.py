from collections import defaultdict
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

class Personality(Enum):
    LAZY = 0
    DELEGATOR = 1
    COLLABORATIVE = 2
    BOSSY = 3


class Dimension(Enum):
    HIDDEN = 0
    VISIT = 1

# Classe PrototypeContext
class PrototypeContext:
    def __init__(self, name: str = 'root', parent: Optional['PrototypeContext'] = None):
        self.name = name
        self.parent = parent
        self.variables = {}

    def set(self, key: str, value):
        self.variables[key] = value

    def get(self, key: str):
        if key in self.variables:
            return self.variables[key]
        elif self.parent:
            return self.parent.get(key)
        else:
            return None

    def chain_new_context(self, name: str = 'child'):
        return PrototypeContext(name=name, parent=self)

# Implementações simplificadas dos finders
def literal_finder(pattern):
    # Simula a divisão do padrão em tokens com base em espaços
    return pattern.strip().split()

def regex_finder(pattern):
    # Simula a correspondência de um padrão regex
    return [pattern]

def pattern_finder(pattern):
    # Simula o processamento de um padrão composto
    return pattern.strip().split()

def eof_finder(pattern):
    # Simula o reconhecimento do fim do arquivo
    return ['EOF']

# Implement 'match_literal' function
def match_literal(token_pattern, text):
    if text == token_pattern:
        return text
    return None

# Implement 'match_regex' function
import re
def match_regex(token_pattern, text):
    match = re.fullmatch(token_pattern, text)
    if match:
        return match.group()
    return None


# Construção da gramática
ctx_root = PrototypeContext(name='root')



ctx_root.set("OPEN_BRACKET", dict(pattern='<', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("CLOSE_BRACKET", dict(pattern='>', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("SLASH", dict(pattern='/', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("EQUAL_SIGN", dict(pattern='=', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("COLON", dict(pattern=':', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("OPEN_KEY", dict(pattern='{', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("CLOSE_KEY", dict(pattern='}', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("COMMA", dict(pattern=',', contexts=(ctx_root,), scan=literal_finder, extract = match_literal))
ctx_root.set("REQUIRE_LITERAL", dict(pattern="require", contexts=(ctx_root,), scan=literal_finder, extract = match_literal))


ctx_root.set("A_IDENTIFIER", dict(pattern=r'[a-zA-Z_][a-zA-Z0-9_\.]*', contexts=(ctx_root,), scan=regex_finder, extract = match_regex))
ctx_root.set("STRING", dict(pattern=r'"(?:\\.|[^"\\])*"', dim=("uma_dimensão",), contexts=(ctx_root,), scan=regex_finder, extract = match_regex))
ctx_root.set("B_IDENTIFIER", dict(pattern="&LIST|&OBJECT|&A_IDENTIFIER", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("LIST", dict(pattern="&OPEN_BRACKET &B_IDENTIFIER (&COMMA &B_IDENTIFIER)*? &CLOSE_BRACKET", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("OBJECT", dict(pattern="&OPEN_KEY (&A_IDENTIFIER &COLON &B_IDENTIFIER)*? &CLOSE_KEY", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("ATTRIBUTE", dict(pattern="&A_IDENTIFIER (&EQUAL_SIGN|&COLON) &B_IDENTIFIER", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("ATTRIBUTES", dict(pattern="(&ATTRIBUTE)*", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("EOF", dict(scan=eof_finder, contexts=(ctx_root,)))  # Adicionado 'contexts'
ctx_root.set("OPEN_TAG", dict(pattern="&OPEN_BRACKET &A_IDENTIFIER &ATTRIBUTES? &CLOSE_BRACKET", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("PROGRAM", dict(pattern="(&XML_STATEMENT|&REQUIRE_STATEMENT)*", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("CLOSE_TAG", dict(pattern="&OPEN_BRACKET &SLASH &B_IDENTIFIER &CLOSE_BRACKET", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("XML_STATEMENT", dict(pattern="&OPEN_TAG &PROGRAM &CLOSE_TAG", contexts=(ctx_root,), scan=pattern_finder))
ctx_root.set("REQUIRE_STATEMENT", dict(pattern="&REQUIRE_LITERAL &A_IDENTIFIER", contexts=(ctx_root,), scan=pattern_finder))

ctx_root.set("ROOT", dict(pattern="&PROGRAM &EOF", contexts=(ctx_root,), scan=pattern_finder, personality = Personality.LAZY))

# Código de exemplo para analisar
code = """
<code>
    require Ship
    <wolfram.Math instance=[Ship, Algo] anotherParameter={identifier: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

# ...


def find_finder(value, ctxs):
    if ctxs is None:
        ctxs = (ctx_root,)  # Adiciona um contexto padrão se ctxs for None
    for ctx in ctxs:
        val = ctx.get(value)
        if val is not None:
            val['name'] = value  # Adiciona o nome do token
            return val, ctx
    return None, None

def cleanup(seq):
    val = seq.strip()
    is_identifier = False
    is_optional = False
    is_sequential = False
    is_grouped = False

    if val.startswith("&"):
        is_identifier = True
        val = val[1:]

    if val.endswith("?"):
        is_optional = True
        val = val[:-1]

    if val.endswith("*"):
        is_sequential = True
        val = val[:-1]

    if val.startswith("(") and val.endswith(")"):
        is_grouped = True
        val = val[1:-1]
    return val, is_identifier, is_optional, is_sequential, is_grouped

def create_ast_node(token, actual_node=PrototypeContext(name='node_root'), processing_tokens=None):
    if processing_tokens is None:
        processing_tokens = set()

    val = token.get('name', token.get('value', None))
    if val in processing_tokens:
        # Já estamos processando este token; evitar recursão infinita
        return []

    # Adiciona o token ao conjunto de tokens em processamento
    processing_tokens.add(val)

    lof_tokens = []
    pos = 0

    if not isinstance(token, dict):
        raise Exception("enviado formato invalido")

    pattern = token.get("pattern")
    scanner = token.get('scan', None)
    contexts = token.get('contexts')
    if contexts is None:
        contexts = (ctx_root,)  # Adiciona um contexto padrão se contexts for None

    # Obter sequência de padrões
    sequences = scanner(pattern)
    for seq in sequences:
        has_or_operand = False  # Inicializa a variável
        val_seq, is_identifier, is_optional, is_sequential, is_grouped = cleanup(seq)
        children = []

        if "|" in val_seq:
            has_or_operand = True
            nc = actual_node.chain_new_context("child_array")
            options = val_seq.split("|")
            for sub_val in options:
                sub_val = sub_val.strip()
                sub_val, sub_is_identifier, sub_is_optional, sub_is_sequential, sub_is_grouped = cleanup(sub_val)
                sub_sequence, ctx_chosen = find_finder(sub_val, contexts)
                if sub_sequence and ctx_chosen:
                    sub_children = create_ast_node(sub_sequence, nc, processing_tokens)
                else:
                    sub_children = []
                option_sequence_dict = {
                    'is_identifier': sub_is_identifier,
                    'is_optional': sub_is_optional,
                    'is_sequential': sub_is_sequential,
                    'has_or_operand': False,
                    'is_grouped': sub_is_grouped,
                    'node': nc,
                    'children': sub_children,
                    'pos': pos,
                    'value': sub_val
                }
                children.append(option_sequence_dict)
        else:
            sub_sequence, ctx_chosen = find_finder(val_seq.strip(), contexts)
            if sub_sequence and ctx_chosen:
                children = create_ast_node  (sub_sequence, ctx_chosen.chain_new_context(name='sub'), processing_tokens)
            else:
                children = []

        # Monta o dicionário do token atual
        sequence_dict = {
            'is_identifier': is_identifier,
            'is_optional': is_optional,
            'is_sequential': is_sequential,
            'has_or_operand': has_or_operand,
            'is_grouped': is_grouped,
            'node': actual_node,
            'children': children,
            'pos': pos,  # posição virtual
            'value': val_seq
        }
        lof_tokens.append(sequence_dict)
        pos += 1

    # Remove o token do conjunto após o processamento
    processing_tokens.remove(val)

    return lof_tokens


# Exibe os tokens gerados
import pprint
def print_tokens(tokens, indent=0):
    for token in tokens:
        info = []
        if token['is_optional']:
            info.append('optional')
        if token['is_sequential']:
            info.append('sequential')
        if token['has_or_operand']:
            info.append('or')
        if token['is_grouped']:
            info.append('grouped')
        info_str = f" ({', '.join(info)})" if info else ''
        print('    ' * indent + f"- {token['value']}{info_str}")
        if token['children']:
            print_tokens(token['children'], indent + 1)


from collections import defaultdict

def flatten_tokens(tokens, current_pos=0, tk_sequence=None):
    if tk_sequence is None:
        tk_sequence = defaultdict(list)

    for tk in tokens:
        value = tk.get('value')
        is_identifier = tk.get('is_identifier', False)
        is_optional = tk.get('is_optional', False)
        is_sequential = tk.get('is_sequential', False)
        has_or_operand = tk.get('has_or_operand', False)
        is_grouped = tk.get('is_grouped', False)
        children = tk.get('children', [])
        extract_method = None

        # Se o token é um identificador, obtemos sua definição para verificar o 'extract'
        if is_identifier:
            token_def, ctx = find_finder(value, None)
            if token_def:
                extract_method = token_def.get('extract', None)

        if extract_method:
            # Token tem o método 'extract', então pode extrair do texto
            tk_sequence[current_pos].append(tk)
            # Atualiza a posição dependendo se é sequencial
            if is_sequential:
                MAX_REPEAT = 3  # Defina um limite adequado
                for repeat in range(MAX_REPEAT):
                    tk_sequence[current_pos + repeat].append(tk)
                current_pos += MAX_REPEAT
            else:
                current_pos += 1
        else:
            # Token não tem 'extract'; processamos seus filhos
            if has_or_operand:
                # Processamos cada opção nos filhos na mesma posição
                for option in children:
                    flatten_tokens([option], current_pos, tk_sequence)
            else:
                # Processamos os filhos recursivamente
                flatten_tokens(children, current_pos, tk_sequence)
                # Atualizamos a posição virtual se o token não for opcional
                if not is_optional:
                    if is_sequential:
                        MAX_REPEAT = 3  # Defina um limite adequado
                        current_pos += MAX_REPEAT
                    else:
                        current_pos += 1
                else:
                    # Se for opcional, não avançamos a posição virtual
                    pass  # Já estamos considerando ambos os casos

    return tk_sequence


tks = create_ast_node(ctx_root.get('ROOT'))


fkl_tks = flatten_tokens(tks)


# Update the parsing loop
p1, p2 = 0, 0
step = 0
code_length = len(code)
parsed_tokens = []

# Output the parsed tokens
print("Parsed Tokens:")
for token_name, token_text in parsed_tokens:
    print(f"{token_name}: {token_text}")


# # Imprime o tk_sequence
# for pos in sorted(fkl_tks.keys()):
#     print(f"Posição {pos}:")
#     for tk in fkl_tks[pos]:
#         print(f"  - {tk['value']} (is_optional={tk.get('is_optional')}, is_sequential={tk.get('is_sequential')})")