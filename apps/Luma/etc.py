import re
from collections import defaultdict
from collections.abc import Iterable
from token_tk_base import TokenTK
from typing import List, Tuple, Dict, Any, Optional, Union


from analyzier import analyze_pattern
from enums import PropagationType, Personality
from main import ParserContext, get_value, regex_finder, pattern_finder, eof_finder


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
        ('&OPEN_BRACKET', {'pattern': r'<', 'is_primitive': True, 'scan': regex_finder}),
        ('&CLOSE_BRACKET', {'pattern': r'>', 'is_primitive': True, 'scan': regex_finder}),
        ('&SLASH', {'pattern': r'/', 'is_primitive': True, 'scan': regex_finder}),
        ('&EQUAL_SIGN', {'pattern': r'=', 'is_primitive': True, 'scan': regex_finder}),
        ('&COLON', {'pattern': r':', 'is_primitive': True, 'scan': regex_finder}),
        ('&OPEN_KEY', {'pattern': r'\{', 'is_primitive': True, 'scan': regex_finder}),
        ('&CLOSE_KEY', {'pattern': r'\}', 'is_primitive': True, 'scan': regex_finder}),
        ('&COMMA', {'pattern': r',', 'is_primitive': True, 'scan': regex_finder}),
        ('&REQUIRE_LITERAL', {'pattern': r'require', 'is_primitive': True, 'scan': regex_finder}),
        ('&STRING', {'pattern': r'"(?:\\.|[^"\\])*"', 'is_primitive': True, 'scan': regex_finder}),
        ('&A_IDENTIFIER', {'pattern': r'[a-zA-Z_][a-zA-Z0-9_\.]*', 'is_primitive': True, 'scan': regex_finder}),
        ('&NEWLINE', {'pattern': r'\n', 'is_primitive': True, 'scan': regex_finder}),
        ('&SKIP', {'pattern': r'[ \t]+', 'is_primitive': True, 'scan': regex_finder}),
        ('&MISMATCH', {'pattern': r'.', 'is_primitive': True, 'scan': regex_finder}),
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
        "&TEST3": {
            "pattern": "(&OPEN_BRACKET &SLASH? &CLOSE_BRACKET)",
            "contexts": [token_context],
            "scan": pattern_finder,
            "is_owner": False,
            "personality": Personality.LAZY
        },
        "&TEST4": {
            "pattern": "(&OPEN_BRACKET (&OPEN_BRACKET|&SLASH?|&CLOSE_BRACKET)? &CLOSE_BRACKET*)",
            "contexts": [token_context],
            "scan": pattern_finder,
            "is_owner": False,
            "personality": Personality.LAZY
        },
    }

    for name, info in complex_tokens.items():
        parser_context.set_token(name, info)

    return parser_context



def iter_tk(token_start: TokenTK):
    tk_manager = token_start.parents[0]
    tk_sequence = tk_manager.children

    if token_start != tk_manager.children[0]:
        raise Exception("algo de errado não está certo")

    if tk_manager.specification['propagation'] == PropagationType.ONLY_ONE and tk_manager.specification['is_group']:
        for tk in tk_sequence:
            if tk.specification['propagation'] == PropagationType.ONLY_ONE:
                yield tk

            if tk.specification['propagation'] == PropagationType.ONE_TO_MANY:
                pass

    if tk_manager.specification['propagation'] == PropagationType.ONE_TO_MANY and tk_manager.specification['is_group']:
        while True:
            for tk in tk_sequence:
                yield tk


def get_view(token: TokenTK) -> tuple[bool, bool]:
    is_zero = token.specification['propagation'] in {PropagationType.ZERO_TO_ONE, PropagationType.ZERO_TO_MANY}
    is_many = token.specification['propagation'] in {PropagationType.ONE_TO_MANY, PropagationType.ZERO_TO_MANY}

    return is_zero, is_many

def chain_token(tokens: list[int, TokenTK]):

    for tk1, tk2 in zip(tokens[0:], tokens[1:]):

        _, is_many = get_view(tk1)
        tk1.ntokens.append(tk2)  # um token sempre apontará para o próximo
        if is_many:
            tk1.ntokens.append(tk1)  # aponta para ele mesmo

    reversed_tk = tokens[::-1]

    for tk1, tk2 in zip(reversed_tk[0:], reversed_tk[1:]):
        is_zero, _ = get_view(tk1)
        if is_zero:
            tk2.ntokens.append(*tk1.ntokens)


def compile_token(actual_token) -> dict[int, list[TokenTK]]:
    # 3. Realiza a hidração dos dados em si
    actual_token.specification, c_pattern_seq_list = analyze_pattern(actual_token.pattern, matcher=r"(\(.*\)|&?\w+)(\*\?|\*|\?|\?\*)?$")
    lof_tk = defaultdict(list)

    for rel_pos, str_patter in c_pattern_seq_list:
        tk, _ = get_value(str_patter, actual_token.contexts)
        tk.parents.append(actual_token)
        actual_token.children.append(tk)
        if tk.is_primitive:
            tk.specification, _ = analyze_pattern(str_patter, matcher=r"(&?\w+)(\*\?|\*|\?|\?\*)?$")

            lof_tk[rel_pos].append(tk)
        else:
            tk_l = compile_token(tk)
            lof_tk[rel_pos].append(tk_l[0])

    for _, val in lof_tk.items():
        chain_token(val)

    return lof_tk

def build_superficialize(ctx: ParserContext, token_str: str):

    tk = extract_token_from_context(token_str, ctx)
    tk_left = compile_token(tk)
    return tk_left
