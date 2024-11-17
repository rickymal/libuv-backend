from abc import abstractmethod, ABC
from collections import defaultdict
from dataclasses import dataclass

import re


def regex_finder(text: str, pattern: str) -> list[tuple[int, int, str]]:
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.end(), match.group()))
    return matches



class ObjectSelector(ABC):

    def __init__(self):
        self.left: list[ObjectSelector] = []
        self.right: list[ObjectSelector] = []


    def look_forward(self, *other: 'ObjectSelector'):
        self.right.append(*other)

    def look_behind(self, *other: 'ObjectSelector'):
        self.right.append(*other)

    def get_forward(self):
        return self.right



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

    def compile(self):
        raise NotImplementedError("")
        pass

    def __init__(self, token):
        super().__init__()
        self.token = token

    def get_value(self, pos: int):
        if pos == 0:
            return [self.token]
        else:
            raise NotImplementedError("")
        pass

class ZeroOrOneSelector(ObjectSelector):

    def compile(self):
        raise NotImplementedError("")

    def __init__(self, tk):
        super().__init__()
        self.tk = tk

    def get_value(self, pos: int):
        if pos == 0:
            return [self.tk, self.get_next()]
        else:
            raise NotImplementedError("")
        pass

class OneToManySelector(ObjectSelector):

    def compile(self):
        pass

    def __init__(self, tk: Token):
        self.tk = tk
        super().__init__()

    def get_value(self, pos: int):
        if pos == 0:
            return self.tk
        else:
            return self.tk

class OrSelector(ObjectSelector):

    def compile(self):
        pass

    def __init__(self, *tks: ObjectSelector):
        self.tks = tks
        super().__init__()

    def get_value(self, pos: int):
        if pos == 0:
            return [tk.get_value(pos) for tk in self.tks]
        else:
            raise NotImplementedError("")


class EndOfSeqSelector(ObjectSelector):
    def get_value(self, pos: int):
        pass

    def compile(self):
        pass


class AndSelector(ObjectSelector):

    def get_value(self, pos: int):
        pass

    def __init__(self, *objectSelector: ObjectSelector):
        self.obj_selector: list[ObjectSelector] = objectSelector
        self.sequence = defaultdict(list)
        super().__init__()

    def compile(self, seq=None, actual_pos=0):
        if seq is None:
            seq = defaultdict(list)

        # self.obj_selector.append(EndOfSeqSelector())
        for tk1, tk2 in zip(self.obj_selector[:-1], self.obj_selector[1:]):
            tk1.look_forward(tk2)

            if isinstance(tk1, OneToManySelector):
                tk1.look_forward(self)

        obj_selector_reversed = self.obj_selector[::-1]

        for tk1, tk2 in zip(obj_selector_reversed[:-1], obj_selector_reversed[1:]):
            if isinstance(tk1, ZeroOrOneSelector):
                tk2.look_forward(*tk1.get_forward())

        for idx, seq in enumerate(self.obj_selector):
            seq[idx] = seq
            # seq.compile()
        return seq



root = AndSelector(
    OneSelector(open_bracket),
    ZeroOrOneSelector(
        OrSelector(
            OneSelector(open_bracket),
            ZeroOrOneSelector(slash),
            OneSelector(close_bracket)
        ),
    ),
)

tk_seq = root.compile()
