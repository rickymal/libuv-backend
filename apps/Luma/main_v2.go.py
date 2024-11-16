from abc import abstractmethod, ABC
from dataclasses import dataclass

from main import ParserContext

import re


def regex_finder(text: str, pattern: str) -> list[tuple[int, int, str]]:
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.end(), match.group()))
    return matches



class ObjectSelector(ABC):

    @abstractmethod
    def get_value(self, pos: int):
        pass


    @abstractmethod
    def compile(self):
        pass

    def get_next(self):
        pass

    def chain(self, left: 'ObjectSelector', right: 'ObjectSelector', dim: str):
        self.left = left
        self.right = right
        self.dim = dim


@dataclass
class Token:
    name: str
    scan: any




class ParserBuilder:
    def __init__(self, parent = None):
        self.parent = parent
        self.chars = []
        self.ctx_tokens = []
        self.sequence: list[ObjectSelector] = []
        pass

    def stmt(self):
        return ParserBuilder(parent = self)

    def skip_chars(self, *chars):
        self.chars = chars

    def add_ctx(self, tk):
        self.ctx_tokens.append(tk)

    def create_sequence(self, *objectSelector: ObjectSelector):
        self.sequence = objectSelector

    def compile(self):
        for seq in self.sequence:
            seq.compile()

        return self.sequence[0]


class ParserTokens:
    def __init__(self):
        self.tokens = dict()
        pass

    def token(self, name: str, scan: any) -> Token:
        tk = Token(name = name, scan = scan)
        self.tokens[name] = tk
        return tk


ps = ParserBuilder()
pt = ParserTokens()

open_bracket: Token = pt.token(name = "OPEN_BRACKET", scan = lambda text: regex_finder(text = text, pattern = r"<"))
slash: Token = pt.token(name = "OPEN_BRACKET", scan = lambda text: regex_finder(text = text, pattern = r"/"))
close_bracket: Token = pt.token(name = "OPEN_BRACKET", scan = lambda text: regex_finder(text = text, pattern = r">"))

root_stmt: ParserBuilder = ps.stmt()
root_stmt.skip_chars("\n", "\r", "\t", " ")


root_stmt.add_ctx(pt)

class OneSelector(ObjectSelector):

    def __init__(self, token):
        self.token = token

    def get_value(self, pos: int):
        if pos == 0:
            return [self.token]
        else:
            raise NotImplementedError("")
        pass

class ZeroOrOneSelector(ObjectSelector):

    def __init__(self, tk):
        self.tk = tk

    def get_value(self, pos: int):
        if pos == 0:
            return [self.tk, self.get_next()]
        else:
            raise NotImplementedError("")
        pass

class OneToManySelector(ObjectSelector):

    def __init__(self, tk: Token):
        self.tk = tk

    def get_value(self, pos: int):
        if pos == 0:
            return self.tk
        else:
            return self.tk

class OptionSelector(ObjectSelector):

    def __init__(self, *tks: ObjectSelector):
        self.tks = tks

    def get_value(self, pos: int):
        if pos == 0:
            return [tk.get_value(pos) for tk in self.tks]
        else:
            raise NotImplementedError("")


root_stmt.create_sequence(
    OneSelector(open_bracket),
    ZeroOrOneSelector(
        OptionSelector(
            OneSelector(open_bracket),
            ZeroOrOneSelector(slash),
            OneSelector(close_bracket)
        ),
    ),
)

tk_seq = ps.compile()

tk_seq.get_next() # Obtem o token open_bracket
tk_seq.get_next() # Obtem o token open_bracket etc...

