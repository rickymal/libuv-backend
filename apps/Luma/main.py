from abc import ABC, abstractmethod
import re
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


import yaml
from typing import Any, Dict


import dataclasses
from typing import Any, Dict

def convert_to_dict(obj: Any) -> Any:
    """
    Converte um objeto dataclass para um dicionário de forma recursiva.
    Se o objeto não for uma dataclass, retorna o objeto como está.

    Args:
        obj (Any): O objeto a ser convertido.

    Returns:
        Any: O dicionário resultante ou o objeto original se não for uma dataclass.
    """
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    elif isinstance(obj, list):
        return [convert_to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_to_dict(value) for key, value in obj.items()}
    else:
        return obj


def export_dict_to_yaml_file(data: Dict[str, Any], file_path: str) -> None:
    """
    Exporta um dicionário para um arquivo YAML.

    Args:
        data (Dict[str, Any]): O dicionário a ser exportado.
        file_path (str): O caminho do arquivo onde o YAML será salvo.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)
        print(f"Dados exportados com sucesso para {file_path}")
    except Exception as e:
        print(f"Erro ao exportar para YAML: {e}")



# Definições de Enums
class Personality(Enum):
    LAZY = auto()          # Delegar o proprietário para o novo token encontrado
    DELEGATOR = auto()    # Similar ao LAZY
    COLLABORATIVE = auto()# Leitura em conjunto com novos tokens
    BOSSY = auto()        # Não delega, lê até o final antes de passar para o próximo token


class Dimension(Enum):
    HIDDEN = auto()
    VISIT = auto()


class PropagationType(Enum):
    UNDEFINED = auto()
    ZERO_TO_ONE = auto()
    ZERO_TO_MANY = auto()
    ONE_TO_MANY = auto()


# Definição do Token
@dataclass
class Token:
    name: str
    pattern: str
    is_primitive: bool
    extract: Callable[[Dict[str, Any], str], List[Tuple[int, int, str]]]
    contexts: List['ParserContext'] = field(default_factory=list)
    is_owner: bool = False
    personality: Optional[Personality] = None
    next_tokens: List['Token'] = field(default_factory=list)
    specification: Dict[str, Any] = field(default_factory=dict)
    value: Optional[Dict[str, Union[int, str]]] = None




class Grammar(ABC):
   
    def __init__(self):
        self.hydrated_token = None
        self.parser_context = None
        self.visitor = None

    @abstractmethod
    def build_grammar(self, visitor):
        raise NotImplementedError("")

    def compile_tokens(self, init):
        actual_token = self.parser_context.get_token(init)
        if not actual_token:
            raise ValueError(f"Token {init} não encontrado no contexto do parser.")
        tokens_patterns = actual_token.pattern.split(" ")
        tokens_list = []
        for pattern in tokens_patterns:
            cleaned_pattern = re.sub(r"[^a-zA-Z0-9_]", "", pattern)
            token, ctx = get_value(cleaned_pattern, actual_token.contexts)
            token.specification = analyze_pattern(pattern)
            tokens_list.append(token)

        # Linkando os tokens
        for tk1, tk2 in zip(tokens_list, tokens_list[1:]):
            tk1.next_tokens.append(tk2)
        self.hydrated_token = tokens_list


class ObjectGrammar(Grammar):

    def build_grammar(self, visitor) -> 'ParserContext':
        parser_context = ParserContext(name='parser')
        token_context = ParserContext(name='token', parent=parser_context)

        TOKEN_SPECIFICATION = [
            ('OPEN_BRACKET', {'pattern': r'<', 'is_primitive': True, 'extract': regex_finder}),
            ('CLOSE_BRACKET', {'pattern': r'>', 'is_primitive': True, 'extract': regex_finder}),
            ('SLASH', {'pattern': r'/', 'is_primitive': True, 'extract': regex_finder}),
            ('EQUAL_SIGN', {'pattern': r'=', 'is_primitive': True, 'extract': regex_finder}),
            ('COLON', {'pattern': r':', 'is_primitive': True, 'extract': regex_finder}),
            ('OPEN_KEY', {'pattern': r'\{', 'is_primitive': True, 'extract': regex_finder}),
            ('CLOSE_KEY', {'pattern': r'\}', 'is_primitive': True, 'extract': regex_finder}),
            ('COMMA', {'pattern': r',', 'is_primitive': True, 'extract': regex_finder}),
            ('REQUIRE_LITERAL', {'pattern': r'require', 'is_primitive': True, 'extract': regex_finder}),
            ('STRING', {'pattern': r'"(?:\\.|[^"\\])*"', 'is_primitive': True, 'extract': regex_finder}),
            ('A_IDENTIFIER', {'pattern': r'[a-zA-Z_][a-zA-Z0-9_\.]*', 'is_primitive': True, 'extract': regex_finder}),
            ('NEWLINE', {'pattern': r'\n', 'is_primitive': True, 'extract': regex_finder}),
            ('SKIP', {'pattern': r'[ \t]+', 'is_primitive': True, 'extract': regex_finder}),
            ('MISMATCH', {'pattern': r'.', 'is_primitive': True, 'extract': regex_finder}),
        ]

        for name, info in TOKEN_SPECIFICATION:
            token_context.set_token(name, info)

        # Definindo tokens complexos
        complex_tokens = {
            "B_IDENTIFIER": {
                "pattern": "&LIST|&OBJECT|&A_IDENTIFIER",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "LIST": {
                "pattern": "&OPEN_BRACKET &B_IDENTIFIER (&COMMA &B_IDENTIFIER)*? &CLOSE_BRACKET",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "visitor": visitor.visit_list,
            },
            "OBJECT": {
                "pattern": "&OPEN_KEY (&A_IDENTIFIER &COLON &B_IDENTIFIER)*? &CLOSE_KEY",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "visitor": visitor.visit_object,
            },
            "ATTRIBUTE": {
                "pattern": "&A_IDENTIFIER (&EQUAL_SIGN|&COLON) &B_IDENTIFIER",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "ATTRIBUTES": {
                "pattern": "(&ATTRIBUTE)*",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "EOF": {
                "scan": eof_finder,
                "is_owner": False,
                "contexts": [token_context]
            },
            "OPEN_TAG": {
                "pattern": "&OPEN_BRACKET &A_IDENTIFIER &ATTRIBUTES? &CLOSE_BRACKET",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "PROGRAM": {
                "pattern": "(&XML_STATEMENT|&REQUIRE_STATEMENT)*",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "CLOSE_TAG": {
                "pattern": "&OPEN_BRACKET &SLASH &B_IDENTIFIER &CLOSE_BRACKET",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "XML_STATEMENT": {
                "pattern": "&OPEN_TAG &PROGRAM &CLOSE_TAG",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "REQUIRE_STATEMENT": {
                "pattern": "&REQUIRE_LITERAL &A_IDENTIFIER",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "ROOT": {
                "pattern": "&PROGRAM &EOF",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "personality": Personality.LAZY
            },
            "TEST1": {
                "pattern": "&OPEN_BRACKET &SLASH &CLOSE_BRACKET",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "personality": Personality.LAZY
            },
            "TEST2": {
                "pattern": "(&OPEN_BRACKET &SLASH &CLOSE_BRACKET)*",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "personality": Personality.LAZY
            },
        }

        for name, info in complex_tokens.items():
            parser_context.set_token(name, info)

        self.parser_context = parser_context


    def iter_tokens_light(self,):
        return iter(self.hydrated_token)


# Definição do Contexto de Parsing
class ParserContext:
    def __init__(self, name: str = 'root', parent: Optional['ParserContext'] = None):
        self.name = name
        self.parent = parent
        self.variables: Dict[str, Any] = {}
        self.tokens: Dict[str, Token] = {}

    def set_token(self, name: str, token_info: Dict[str, Any]):
        token = Token(
            name=name,
            pattern=token_info.get('pattern', ''),
            is_primitive=token_info.get('is_primitive', False),
            extract=token_info.get('extract', lambda tk, txt: []),
            is_owner=token_info.get('is_owner', False),
            personality=token_info.get('personality', None),
            contexts=list(token_info.get('contexts', ())),
        )
        self.tokens[name] = token

    def get_token(self, name: str) -> Optional[Token]:
        return self.tokens.get(name) or (self.parent.get_token(name) if self.parent else None)

    def set_variable(self, key: str, value: Any):
        self.variables[key] = value

    def get_variable(self, key: str) -> Any:
        return self.variables.get(key) or (self.parent.get_variable(key) if self.parent else None)


# Funções de Encontrar Tokens
def literal_finder(pattern: str, text: str) -> List[Tuple[int, int, str]]:
    tokens = pattern.strip().split()
    matches = []
    pos = 0
    for token in tokens:
        if text.startswith(token, pos):
            matches.append((pos, pos + len(token), token))
            pos += len(token)
        else:
            break
    return matches


def regex_finder(token_info: Dict[str, Any], text: str) -> List[Tuple[int, int, str]]:
    pattern = token_info['pattern']
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.end(), match.group()))
    return matches


def pattern_finder(pattern: str, text: str) -> List[Tuple[int, int, str]]:
    tokens = pattern.strip().split()
    return [(0, len(text), text)] if ' '.join(tokens) == text else []


def eof_finder(token_info: Dict[str, Any], text: str) -> List[Tuple[int, int, str]]:
    return [(0, 0, 'EOF')] if text == '' else []


# Funções de Match
def match_literal(token_pattern: str, text: str) -> Optional[str]:
    return text if text == token_pattern else None


def match_regex(token_pattern: str, text: str) -> Optional[str]:
    match = re.fullmatch(token_pattern, text)
    return match.group() if match else None


class Visitor:
    def visit_object(self,):
        pass

    def visit_list(self):
        pass

# Construção da Gramática

# Função para Obter Token
def get_value(value: str, contexts: List[ParserContext]) -> Tuple[Token, Optional[ParserContext]]:
    for ctx in contexts:
        token = ctx.get_token(value)
        if token:
            return token, ctx
    raise ValueError(f"Token '{value}' não encontrado em nenhum contexto.")


# Função Principal de Parsing
def parse_code(grammar: Grammar, code: str, init: str):


    grammar.build_grammar(visitor=Visitor())
    grammar.compile_tokens(init)


    for val in grammar.iter_tokens_light():
        print(val)



def analyze_pattern(pattern: str) -> Dict[str, Any]:
    is_identifier = pattern == "&"
    is_group = pattern.startswith("(") and pattern.endswith(")")
    is_sequence = "|" in pattern

    has_star = "*" in pattern[:-2]
    has_question = "?" in pattern[:-2]
    propagation = PropagationType.UNDEFINED

    if has_star and has_question:
        propagation = PropagationType.ZERO_TO_MANY
    elif has_star:
        propagation = PropagationType.ONE_TO_MANY
    elif has_question:
        propagation = PropagationType.ZERO_TO_ONE

    return {
        'is_identifier': is_identifier,
        'is_group': is_group,
        'propagation': propagation,
        'in_sequence': is_sequence
    }


# Exemplo de Uso
if __name__ == "__main__":
    # Construir a gramática
    parser_ctx = ObjectGrammar()

    try:
        parse_code(parser_ctx, "</>", "TEST1")

        print("Parsing concluído com sucesso.")
        export_dict_to_yaml_file(convert_to_dict(parser_ctx), "out.yaml")
    except NotImplementedError as nie:
        print(f"Funcionalidade não implementada: {nie}")
    except Exception as e:
        print(f"Erro durante o parsing: {e}")
