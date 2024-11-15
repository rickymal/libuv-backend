import re
from typing import List, Tuple, Dict, Any, Optional

from main import ParserContext, Token, Grammar


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




def build_sequencializer(grammar: Grammar, code: str, token_str: str):

    ctx = grammar.build_grammar(visitor=Visitor())
    tk = grammar.extract_token_from_context(token_str, ctx)
    tk_left = grammar.compile_token(tk)
    return tk_left
