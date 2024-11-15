import re
from typing import List, Tuple, Dict, Any, Optional

from analyzier import analyze_pattern
from enums import PropagationType, Personality
from main import ParserContext, Token, get_value, regex_finder, pattern_finder, eof_finder


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


def extract_token_from_context(token_str_pattern: str, context_to_extract: 'ParserContext'):

    # 1. Obter o token atual para iniciar o processo
    actual_token = context_to_extract.get_token(token_str_pattern)
    if not actual_token:
        raise ValueError(f"Token {token_str_pattern} não encontrado no contexto do parser.")

    return actual_token

def build_grammar(visitor) -> 'ParserContext':
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
        },
        "&OBJECT": {
            "pattern": "&OPEN_KEY (&A_IDENTIFIER &COLON &B_IDENTIFIER)*? &CLOSE_KEY",
            "contexts": [token_context],
            "scan": pattern_finder,
            "is_owner": False,
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


def iter_tk(token_start: Token):
    tk_manager = token_start.parents[0]
    tk_sequence = tk_manager.children

    if token_start != tk_manager.children[0]:
        raise Exception("algo de errado não está certo")

    if tk_manager.specification['propagation'] == PropagationType.ONLY_ONE and tk_manager.specification['is_group']:
        for tk in tk_sequence:
            yield tk

    if tk_manager.specification['propagation'] == PropagationType.ONE_TO_MANY and tk_manager.specification['is_group']:
        while True:
            for tk in tk_sequence:
                yield tk


def compile_token(actual_token):
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

def build_superficialize(ctx: ParserContext, token_str: str):

    tk = extract_token_from_context(token_str, ctx)
    tk_left = compile_token(tk)
    return tk_left
