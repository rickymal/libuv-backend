from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple, Union


import yaml

import dataclasses
from typing import Any, Dict

from analyzier import analyze_pattern
from enums import Personality, PropagationType
from etc import *
import re

def get_value(value: str, contexts: List['ParserContext']) -> Tuple['Token', Optional['ParserContext']]:
    for ctx in contexts:
        token = ctx.get_token(value)
        if token:
            return token, ctx
    raise ValueError(f"Token '{value}' não encontrado em nenhum contexto.")


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
    parents: List['Token'] = field(default_factory=list)
    children: List['Token'] = field(default_factory=list)
    specification: Dict[str, Any] = field(default_factory=dict)
    value: Optional[Dict[str, Union[int, str]]] = None

class Grammar(ABC):
   
    def __init__(self):
        self.hydrated_token = None
        self.parser_context = None
        self.visitor = None
        self.token_start = None

    @abstractmethod
    def build_grammar(self, visitor):
        raise NotImplementedError("")



    def extract_token_from_context(self, token_str_pattern: str, context_to_extract: 'ParserContext'):

        # 1. Obter o token atual para iniciar o processo
        actual_token = context_to_extract.get_token(token_str_pattern)
        if not actual_token:
            raise ValueError(f"Token {token_str_pattern} não encontrado no contexto do parser.")

        return actual_token

    def compile_token(self, actual_token):
        # 3. Realiza a hidração dos dados em si
        actual_token.specification, c_pattern_seq_list = analyze_pattern(actual_token.pattern)

        lof_tk = []
        for str_patter in c_pattern_seq_list:
            tk, ctx = get_value(str_patter, actual_token.contexts)
            tk.parents.append(actual_token)
            actual_token.children.append(tk)
            lof_tk.append(tk)

            # Aqui ocorre a recursão
            if not tk.is_primitive:
                raise NotImplementedError("")

        return lof_tk[0]

    @abstractmethod
    def define_start_token(self, tk_left: Token):
        pass

class ObjectGrammar(Grammar):

    def build_grammar(self, visitor) -> 'ParserContext':
        parser_context = ParserContext(name='parser')
        token_context = ParserContext(name='token', parent=parser_context)

        TOKEN_SPECIFICATION = [
            ('&OPEN_BRACKET', {'pattern': r'<', 'is_primitive': True, 'extract': regex_finder}),
            ('&CLOSE_BRACKET', {'pattern': r'>', 'is_primitive': True, 'extract': regex_finder}),
            ('&SLASH', {'pattern': r'/', 'is_primitive': True, 'extract': regex_finder}),
            ('&EQUAL_SIGN', {'pattern': r'=', 'is_primitive': True, 'extract': regex_finder}),
            ('&COLON', {'pattern': r':', 'is_primitive': True, 'extract': regex_finder}),
            ('&OPEN_KEY', {'pattern': r'\{', 'is_primitive': True, 'extract': regex_finder}),
            ('&CLOSE_KEY', {'pattern': r'\}', 'is_primitive': True, 'extract': regex_finder}),
            ('&COMMA', {'pattern': r',', 'is_primitive': True, 'extract': regex_finder}),
            ('&REQUIRE_LITERAL', {'pattern': r'require', 'is_primitive': True, 'extract': regex_finder}),
            ('&STRING', {'pattern': r'"(?:\\.|[^"\\])*"', 'is_primitive': True, 'extract': regex_finder}),
            ('&A_IDENTIFIER', {'pattern': r'[a-zA-Z_][a-zA-Z0-9_\.]*', 'is_primitive': True, 'extract': regex_finder}),
            ('&NEWLINE', {'pattern': r'\n', 'is_primitive': True, 'extract': regex_finder}),
            ('&SKIP', {'pattern': r'[ \t]+', 'is_primitive': True, 'extract': regex_finder}),
            ('&MISMATCH', {'pattern': r'.', 'is_primitive': True, 'extract': regex_finder}),
        ]

        for name, info in TOKEN_SPECIFICATION:
            token_context.set_token(name, info)

        # Definindo tokens complexos
        complex_tokens = {
            "&B_IDENTIFIER": {
                "pattern": "&LIST|&OBJECT|&A_IDENTIFIER",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&LIST": {
                "pattern": "&OPEN_BRACKET &B_IDENTIFIER (&COMMA &B_IDENTIFIER)*? &CLOSE_BRACKET",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "visitor": visitor.visit_list,
            },
            "&OBJECT": {
                "pattern": "&OPEN_KEY (&A_IDENTIFIER &COLON &B_IDENTIFIER)*? &CLOSE_KEY",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "visitor": visitor.visit_object,
            },
            "&ATTRIBUTE": {
                "pattern": "&A_IDENTIFIER (&EQUAL_SIGN|&COLON) &B_IDENTIFIER",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&ATTRIBUTES": {
                "pattern": "(&ATTRIBUTE)*",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&EOF": {
                "scan": eof_finder,
                "is_owner": False,
                "contexts": [token_context]
            },
            "&OPEN_TAG": {
                "pattern": "&OPEN_BRACKET &A_IDENTIFIER &ATTRIBUTES? &CLOSE_BRACKET",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&PROGRAM": {
                "pattern": "(&XML_STATEMENT|&REQUIRE_STATEMENT)*",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&CLOSE_TAG": {
                "pattern": "&OPEN_BRACKET &SLASH &B_IDENTIFIER &CLOSE_BRACKET",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&XML_STATEMENT": {
                "pattern": "&OPEN_TAG &PROGRAM &CLOSE_TAG",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&REQUIRE_STATEMENT": {
                "pattern": "&REQUIRE_LITERAL &A_IDENTIFIER",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False
            },
            "&ROOT": {
                "pattern": "&PROGRAM &EOF",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "personality": Personality.LAZY
            },
            "&TEST1": {
                "pattern": "(&OPEN_BRACKET &SLASH &CLOSE_BRACKET)",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "personality": Personality.LAZY
            },
            "&TEST2": {
                "pattern": "(&OPEN_BRACKET &SLASH &CLOSE_BRACKET)*",
                "contexts": [token_context],
                "scan": pattern_finder,
                "is_owner": False,
                "personality": Personality.LAZY
            },
        }

        for name, info in complex_tokens.items():
            parser_context.set_token(name, info)

        return parser_context

    def define_start_token(self, tk_left):
        self.token_start = tk_left

    def iter(self):
        tk_manager = self.token_start.parents[0]
        tk_sequence = tk_manager.children

        if self.token_start != tk_manager.children[0]:
            raise Exception("algo de errado não está certo")

        if tk_manager.specification['propagation'] == PropagationType.ONLY_ONE and tk_manager.specification['is_group']:
            for tk in tk_sequence:
                yield tk

        if tk_manager.specification['propagation'] == PropagationType.ONE_TO_MANY and tk_manager.specification['is_group']:
            while True:
                for tk in tk_sequence:
                    yield tk


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

# Exemplo de Uso
if __name__ == "__main__":
    # Construir a gramática
    object_grammar = ObjectGrammar()


    try:

        tk_left = build_sequencializer(object_grammar, "</>", "&TEST1")
        object_grammar.define_start_token(tk_left)

        for og in object_grammar.iter():
            print(og)

        tk_left = build_sequencializer(object_grammar, "</>", "&TEST2")
        object_grammar.define_start_token(tk_left)

        for og in object_grammar.iter():
            print(og)


        print("Parsing concluído com sucesso.")
        export_dict_to_yaml_file(convert_to_dict(object_grammar), "out.yaml")
    except NotImplementedError as nie:
        print(f"Funcionalidade não implementada: {nie}")
        raise Exception(nie)
    except Exception as e:
        print(f"Erro durante o parsing: {e}")
        raise Exception(e)
