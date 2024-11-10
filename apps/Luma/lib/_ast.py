from dataclasses import dataclass
import re
from typing import List, Dict, Tuple, Union, Optional


from enum import Enum

class Personality(Enum):
    LAZY = 0
    DELEGATOR = 1
    COLLABORATIVE = 2
    BOSSY = 3

# Implementação simplificada do PrototypeContext
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


# Definição básica da classe Finder
class Finder:
    def __init__(self, pattern: str, dim: Tuple[str, ...] = ("default",), contexts: Tuple[PrototypeContext, ...] = None, personality=None):
        self.dim = dim
        self.personality = personality
        self.contexts = contexts if contexts else ()
        self.pattern = pattern

        if len(self.contexts) == 0:
            raise Exception("contexto não pode ser nulo")

    def set_context(self, context):
        self.context = context

    def parse(self, text: str, position: int):
        raise NotImplementedError

    def inject_context(self):
        # Combina os contextos e define self.context
        self.parsed_pattern = self._parse_pattern(self.pattern)
        pass 


    def _parse_pattern(self, pattern: str):
        # Função para transformar o pattern string em uma estrutura de dados que facilita o parsing
        # Aqui vamos implementar um parser simples para nossa linguagem de padrões
        tokens = self._tokenize(pattern)
        ast = self._build_ast(tokens)
        return ast 




# ---


from enum import Enum
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

class SequenceType(Enum):
    SEQUENTIAL = 0 # dESCREve uqe temos uma sequencia
    OPTIONAL = 1 #quando temos um caracteres como 'optional'
    INFINITY = 2 #quando temos um caractere como asterístico,
    PRIMITIVE = 3 # são os outros finders, caso seja regex finder ou literal finder
    ROOT = 4 #
    PARENTHESIS = 5 # contido no parentese
    OR_LOGIC = 6 # contem lógica "OU" xom
    REGEX = 7
    LITERAL = 8
    IDENTIFIER = 9

class ParserUnity:

    def __init__(self,template, contexts, pos, is_owner, type):
        self.template = template 
        self.contexts = contexts 
        self.is_owner = is_owner
        self.type = type
        self.chd = []
        self.actual_position = 0


    def define_children(self, new_value):
        pass

    

class PatternFinder(Finder):

    def build(self):
        
        root = ParserUnity(template=self.pattern, contexts=self.contexts, pos = 0, is_owner=False, type=SequenceType.ROOT)

        for val in self.pattern.split(" "):
            root.define_children(val)


        
        

        
        return sequence

# ---

























# Agora, vamos implementar o PatternFinder
class _PatternFinder(Finder): 

    def _tokenize(self, pattern: str):
        # Tokeniza o pattern string
        token_specification = [
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('ASTERISK', r'\*'),
            ('PLUS',     r'\+'),
            ('QUESTION', r'\?'),
            ('PIPE',     r'\|'),
            ('AMP',      r'&'),
            ('IDENT',    r'[a-zA-Z_][a-zA-Z0-9_\.]*'),
            ('SKIP',     r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        pos = 0
        tokens = []
        while pos < len(pattern):
            match = get_token(pattern, pos)
            if match is None:
                raise SyntaxError(f'Unexpected character at position {pos}')
            typ = match.lastgroup
            if typ != 'SKIP':
                val = match.group(typ)
                tokens.append((typ, val))
            pos = match.end()
        return tokens


    def obtain_value(self, val, ref):
        value = None
        for ctx in self.contexts:
            value = ctx.get(val)
            if value != ref:
                break
            else:
                continue
        return value



    def _build_ast(self, tokens):
        # Constrói uma árvore de análise sintática simples do padrão
        def parse_expression(index):
            nodes = []
            while index < len(tokens):
                typ, val = tokens[index]
                if typ == 'LPAREN':
                    index += 1
                    node, index = parse_expression(index)
                    nodes.append(node)
                elif typ == 'RPAREN':
                    index += 1
                    break
                elif typ == 'PIPE':
                    index += 1
                    right_node, index = parse_expression(index)
                    nodes = {'type': 'OR', 'left': nodes, 'right': right_node}
                    break
                elif typ == 'AMP':
                    index += 1
                    typ, val = tokens[index]
                    if typ == 'IDENT':   
                        finder = self.obtain_value(val, None)
                        if not finder:
                            raise ValueError(f'Finder "{val}" not found in context.')
                        nodes.append(finder)
                        index += 1
                    else:
                        raise SyntaxError(f'Expected identifier after "&" at position {index}')
                elif typ == 'IDENT':
                    # Pode ser um finder sem "&"
                    finder = self.context.get(val)
                    if not finder:
                        raise ValueError(f'Finder "{val}" not found in context.')
                    nodes.append(finder)
                    index += 1
                elif typ in ('ASTERISK', 'PLUS', 'QUESTION'):
                    # Operadores unários
                    operator = val
                    finder = nodes.pop()
                    nodes.append({'type': 'UNARY_OP', 'operator': operator, 'operand': finder})
                    index += 1
                else:
                    index += 1
            return nodes, index


        ast, _ = parse_expression(0)
        return ast

    # [entrypoint]
    def parse(self, text: str, position: int):
        self.parsed_pattern = self._parse_pattern(self.pattern)
        # Função recursiva para percorrer o AST e tentar casar o padrão
        success, new_pos = self._match(self.parsed_pattern, text, position)
        if success:
            return {
                'type': 'Pattern',
                'value': text[position:new_pos],
                'start': position,
                'end': new_pos,
                'dim': self.dim
            }, new_pos
        else:
            return None, position

    def _match(self, node, text: str, position: int):
        if isinstance(node, list):
            # Sequência de finders
            current_pos = position
            nodes = []
            for child in node:
                if current_pos == 0:
                    pass
                result, new_pos = self._match(child, text, current_pos)
                if result is None:
                    return None, position
                nodes.append(result)
                current_pos = new_pos
            return nodes, current_pos
        elif isinstance(node, dict):
            node_type = node.get('type')
            if node_type == 'OR':
                # Operador OR
                left_result, left_pos = self._match(node['left'], text, position)
                if left_result:
                    return left_result, left_pos
                right_result, right_pos = self._match(node['right'], text, position)
                if right_result:
                    return right_result, right_pos
                return None, position
            elif node_type == 'UNARY_OP':
                operator = node['operator']
                operand = node['operand']
                if operator == '*':
                    # Zero ou mais ocorrências
                    results = []
                    current_pos = position
                    while True:
                        result, new_pos = self._match(operand, text, current_pos)
                        if result is None or new_pos == current_pos:
                            break
                        results.append(result)
                        current_pos = new_pos
                    return results, current_pos
                elif operator == '+':
                    # Uma ou mais ocorrências
                    results = []
                    current_pos = position
                    first_result, first_pos = self._match(operand, text, current_pos)
                    if first_result is None:
                        return None, position
                    results.append(first_result)
                    current_pos = first_pos
                    while True:
                        result, new_pos = self._match(operand, text, current_pos)
                        if result is None or new_pos == current_pos:
                            break
                        results.append(result)
                        current_pos = new_pos
                    return results, current_pos
                elif operator == '?':
                    # Zero ou uma ocorrência
                    result, new_pos = self._match(operand, text, position)
                    if result:
                        return result, new_pos
                    else:
                        return None, position
            else:
                raise ValueError(f'Unknown node type: {node_type}')
        elif isinstance(node, Finder):
            # Chama o parse do Finder
            return node.parse(text, position)
        else:
            raise ValueError(f'Invalid node in AST: {node}')


class LiteralFinder(Finder):
    # def __init__(self, pattern: str, **kwargs):
    #     super().__init__(**kwargs)
    #     self.pattern = pattern

    def parse(self, text: str):
        """
        Tenta casar o padrão literal com o texto na posição fornecida.

        :param text: O texto de entrada onde a busca será realizada.
        :param position: A posição inicial no texto para começar a busca.
        :return: Um dicionário com informações sobre o match e a nova posição, ou None se não houver match.
        """
        pos = 0
        end_pos = pos + len(self.pattern)
        # Verifica se o texto a partir da posição atual começa com o padrão literal
        if text[pos:end_pos] == self.pattern:
            return {
                'type': 'Literal',
                'value': self.pattern,
                'start': pos,
                'end': end_pos,
                'dim': self.dim
            }, end_pos
        else:
            return None, pos



import re
from typing import Tuple, Optional

# Classe RegexFinder
class RegexFinder(Finder):
    # def __init__(self, pattern: str, **kwargs):
    #     super().__init__(**kwargs)
    #     self.pattern = pattern

    def parse(self, text: str, position: int):
        self.regex = re.compile(self.pattern)
        match = self.regex.match(text, position)
        if match:
            return {
                'type': 'Regex',
                'value': match.group(),
                'start': position,
                'end': match.end(),
                'dim': self.dim
            }, match.end()
        else:
            return None, position


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


class EndOfFileFinder(Finder):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def parse(self, text: str, position: int):
        """
        Verifica se chegamos ao fim do texto de entrada.

        :param text: O texto de entrada a ser analisado.
        :param position: A posição atual no texto.
        :return: Um dicionário com informações se estivermos no EOF, ou None caso contrário.
        """
        if position >= len(text):
            return {
                'type': 'EOF',
                'value': None,
                'start': position,
                'end': position,
                'dim': self.dim
            }, position
        else:
            return None, position

if __name__ == "__main__":
    # Texto de entrada
    text = "HelloWorld"

    # Cria um RegexFinder para capturar uma palavra composta apenas por letras maiúsculas ou minúsculas
    word_finder = RegexFinder(pattern=r'[a-zA-Z]+')
    
    # Cria o EndOfFileFinder
    eof_finder = EndOfFileFinder()
    
    # Posição inicial
    position = 0

    # Tenta casar a palavra
    result, new_position = word_finder.parse(text, position)
    if result:
        print(f"Palavra encontrada: {result}")
        position = new_position
    else:
        print("Nenhuma palavra encontrada.")
    
    # Tenta verificar se estamos no EOF
    result, new_position = eof_finder.parse(text, position)
    if result:
        print("Fim do texto alcançado.")
    else:
        print("Ainda há texto a ser analisado.")


class IVisitorPatternInterpreter:
    def visit(self, node):
        """
        Dispatch method that calls the appropriate visit method for the given node type.

        :param node: The AST node to visit.
        """
        node_type = node.get('type')
        method_name = f'visit_{node_type}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """
        Default visit method if no explicit visitor function exists for a node.

        :param node: The AST node to visit.
        """
        raise NotImplementedError(f"No visit_{node.get('type')} method")




import yaml

class YAMLExporter(IVisitorPatternInterpreter):
    def __init__(self):
        self.output = None

    def export(self, ast):
        """
        Starts the visiting process and returns the YAML representation.

        :param ast: The root of the AST to export.
        :return: A YAML-formatted string representing the AST.
        """
        self.output = self.visit(ast)
        return yaml.dump(self.output, sort_keys=False)

    def visit_Pattern(self, node):
        """
        Visits a Pattern node.

        :param node: The Pattern node to visit.
        """
        result = {
            'type': node['type'],
            'value': node['value'],
            'start': node['start'],
            'end': node['end'],
            'dim': node['dim'],
            'children': []
        }
        # Assuming 'children' are stored in 'nodes' key
        nodes = node.get('nodes', [])
        for child in nodes:
            result['children'].append(self.visit(child))
        return result

    def visit_Literal(self, node):
        """
        Visits a Literal node.

        :param node: The Literal node to visit.
        """
        return {
            'type': node['type'],
            'value': node['value'],
            'start': node['start'],
            'end': node['end'],
            'dim': node['dim']
        }

    def visit_Regex(self, node):
        """
        Visits a Regex node.

        :param node: The Regex node to visit.
        """
        return {
            'type': node['type'],
            'value': node['value'],
            'start': node['start'],
            'end': node['end'],
            'dim': node['dim']
        }

    def visit_EOF(self, node):
        """
        Visits an EOF node.

        :param node: The EOF node to visit.
        """
        return {
            'type': node['type'],
            'start': node['start'],
            'end': node['end'],
            'dim': node['dim']
        }

    def generic_visit(self, node):
        """
        Default method for nodes without a specific visit method.
        """
        result = {
            'type': node.get('type'),
            'value': node.get('value'),
            'start': node.get('start'),
            'end': node.get('end'),
            'dim': node.get('dim'),
            'children': []
        }
        nodes = node.get('nodes', [])
        for child in nodes:
            result['children'].append(self.visit(child))
        return result

# Aqui temos um exportador da árvore para outro código Python, otimizado para ser utilizado como interpretador.
# O código dos finders não possui nenhuma otimização.
class PythonExporter(IVisitorPatternInterpreter):
    pass

class InputDeliver():
    def __init__(self, text: str):
        self.text = text

def init(root_parser: PatternFinder, input_stream: str, transpiler: IVisitorPatternInterpreter):
    """
    Inicializa o parser com o parser raiz, fluxo de entrada e interpretador (transpiler).

    :param root_parser: O parser raiz que contém a gramática completa.
    :param input_stream: O fluxo de entrada que fornece os dados ao parser.
    :param transpiler: O interpretador ou transpiler que processará a árvore sintática gerada.
    """
    

    # Inicia o processo de parsing a partir da posição inicial (0)
    ast, position = root_parser.parse(input_stream.text, 0)

    if ast:
        print("Parsing concluído com sucesso!")
        # Utiliza o transpiler para processar a AST gerada
        output = transpiler.export(ast)
        print("Saída do Transpiler:")
        print(output)
    else:
        print("Falha no parsing. Nenhuma AST foi gerada.")



# Exemplo de uso
if __name__ == "__main__":
    # Texto de entrada
    text = "variable1 = 42"

    # Cria o contexto raiz
    ctx_root = PrototypeContext(name='root')

    # Cria o RegexFinder para identificadores e adiciona ao contexto
    identifier_finder = RegexFinder(pattern=r'[a-zA-Z_][a-zA-Z0-9_]*')
    ctx_root.set("IDENTIFIER", identifier_finder)

    # Cria o LiteralFinder para o sinal de igual e adiciona ao contexto
    equal_sign = LiteralFinder(pattern='=')
    ctx_root.set("EQUAL_SIGN", equal_sign)

    # Cria o RegexFinder para números inteiros e adiciona ao contexto
    integer_finder = RegexFinder(pattern=r'\d+')
    ctx_root.set("INTEGER", integer_finder)

    # Define o PatternFinder para uma instrução de atribuição
    assignment_pattern = "&IDENTIFIER &EQUAL_SIGN &INTEGER"
    assignment_finder = PatternFinder(pattern=assignment_pattern, contexts=(ctx_root,))

    # Testar o PatternFinder
    result, position = assignment_finder.parse(text, 0)
    if result:
        print(f"Instrução de atribuição encontrada: {result}")
    else:
        print("Instrução de atribuição não encontrada.")



# Exemplo de uso com as classes definidas
if __name__ == "__main__":
    # Cria o contexto raiz
    ctx_root = PrototypeContext(name='root')

    # Define alguns LiteralFinders
    open_bracket = LiteralFinder(pattern='<')
    close_bracket = LiteralFinder(pattern='>')
    slash = LiteralFinder(pattern='/')

    ctx_root.set("OPEN_BRACKET", open_bracket)
    ctx_root.set("CLOSE_BRACKET", close_bracket)
    ctx_root.set("SLASH", slash)

    # Define um RegexFinder para identificadores
    identifier_finder = RegexFinder(pattern=r'[a-zA-Z_][a-zA-Z0-9_\.]*')
    ctx_root.set("A_IDENTIFIER", identifier_finder)
    ctx_root.set("B_IDENTIFIER", identifier_finder)  # Simplicidade

    # Define um PatternFinder
    open_tag_pattern = "&OPEN_BRACKET &B_IDENTIFIER &CLOSE_BRACKET"
    open_tag = PatternFinder(pattern=open_tag_pattern, contexts=(ctx_root,))
    ctx_root.set("OPEN_TAG", open_tag)

    # Testa o PatternFinder
    text = "<myTag>"
    result, pos = open_tag.parse(text, 0)
    if result:
        print(f"Parsed successfully: {result}")
    else:
        print("Parsing failed.")


if __name__ == "__main__":
    # Texto de entrada
    text = "<tag>Content</tag>"

    # Cria um LiteralFinder para o símbolo '<'
    open_bracket = LiteralFinder(pattern='<')
    # Cria um LiteralFinder para o símbolo '>'
    close_bracket = LiteralFinder(pattern='>')

    # Posição inicial
    position = 0

    # Tenta casar o '<' no início do texto
    result, new_position = open_bracket.parse(text, position)
    if result:
        print(f"Encontrado: {result}")
        position = new_position  # Atualiza a posição
    else:
        print("Símbolo '<' não encontrado.")

    # Continuar o parsing para buscar 'tag'
    # Supondo que temos um RegexFinder para identificadores
    identifier_finder = RegexFinder(pattern=r'[a-zA-Z_][a-zA-Z0-9_]*')
    result, new_position = identifier_finder.parse(text, position)
    if result:
        print(f"Identificador encontrado: {result}")
        position = new_position
    else:
        print("Identificador não encontrado.")

    # Tenta casar o '>' após o identificador
    result, new_position = close_bracket.parse(text, position)
    if result:
        print(f"Encontrado: {result}")
        position = new_position
    else:
        print("Símbolo '>' não encontrado.")
