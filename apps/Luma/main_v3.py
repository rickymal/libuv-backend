from abc import abstractmethod, ABC
from collections.abc import Iterable
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum, auto
import re
from typing import Union

from anyio.abc import value
from click import option


def regex_finder(text: str, pattern: str) -> list[tuple[int, int, str]]:
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.end(), match.group()))
    return matches


@dataclass
class TK:
    scan: callable

@dataclass
class TKP:
    name: str
    tk: TK
    sequence: bool
    optional: bool

    def __repr__(self):
        return f"TKP: {self.name}"

open_bracket = TK(scan = lambda text: regex_finder(text, pattern="<"))
slash = TK(scan = lambda text: regex_finder(text, pattern="/"))
question = TK(scan = lambda text: regex_finder(text, pattern="?"))
close_bracket = TK(scan = lambda text: regex_finder(text, pattern=">"))

@dataclass
class Chain:
    def __init__(self, value = None):
        self.value = value
        self.next: list[Chain | TKP] = []
        self.pos = 0


    def set_next(self, tk: Union['Chain', TK]):
        ch = Chain()
        ch.value = tk
        self.next.append(ch)



class Selector(ABC):
    def __init__(self, sequence: bool, optional: bool):
        self.sequence = sequence
        self.optional = optional
        self.chn: list[Chain | Selector] = []

    @abstractmethod
    def compile(self, input_ch: Chain, output: Chain):
        pass


class AndSelector(Selector):

    def __init__(self, *tkp: TKP | Selector):
        super().__init__(sequence = False, optional=False)

        for val in tkp:
            ch = val
            if not isinstance(ch, Chain):
                ch = Chain(value = ch)
            else:
                raise Exception("")

            self.chn.append(ch)



    def compile(self, input_ch: Chain, output_ch: Chain):
        lof: list[Chain] = self.chn

        direct = tuple(lof)
        reverse = direct[::-1]

        for ch1, ch2 in zip(direct[:-1], direct[1:]):
            ch1.next.append(ch2)

            if ch1.value.sequence:
                ch1.next.append(ch1)

        for ch1, ch2 in zip(reverse[:-1], reverse[1:]):
            if ch1.value.optional:
                ch2.next.append(*ch1.next)

        input_ch.next.append(lof[0])
        lof[-1].next.append(output_ch)



        for chn1, chn2, chn3 in zip(self.chn[0:-2], self.chn[1:-1], self.chn[2:]):
            if isinstance(chn2.value, Selector):
                chn2.value.compile(chn1, chn3)
            pass





class OrSelector(Selector):
    def __init__(self, *tkp: TKP | Chain):
        super().__init__(sequence = False, optional=False)

        for tk in tkp:
            if not isinstance(tk, Chain):
                ch = Chain(value = tk)
                self.chn.append(ch)
            else:
                self.chn.append(tk)

    def compile(self, input_ch: Chain, output_ch: Chain):
        for tk in self.chn:
            input_ch.next.append(tk)
            tk.next.append(output_ch)



input_ch = Chain()
output_ch = Chain()

and_s = AndSelector(
    TKP(name = "AAA",tk=open_bracket, sequence=False, optional=False),
    OrSelector(
        TKP(name = "BBB", tk=slash, sequence=False, optional=False),
        TKP(name = "CCC", tk=question, sequence=False, optional=False),
    ),
    TKP(name = "DDD", tk=close_bracket, sequence=False, optional=False),
)


and_s.compile(input_ch, output_ch)