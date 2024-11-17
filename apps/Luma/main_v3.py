from collections.abc import Iterable
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum, auto
import re
from typing import Union


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


def and_selector(*tks: TKP | Chain) -> Chain:
    lof: list[Chain] = [Chain(val) for val in tks]

    direct = tuple(lof)
    reverse = direct[::-1]

    for ch1, ch2 in zip(direct[:-1], direct[1:]):
        ch1.next.append(ch2)

        if ch1.value.sequence:
            ch1.next.append(ch1)

    for ch1, ch2 in zip(reverse[:-1], reverse[1:]):
        if ch1.value.optional:
            ch2.next.append(*ch1.next)


    for idx, val in enumerate(lof):
        val.pos = idx

    return lof[0]


def or_selector(*tks: TKP, input_ch: Chain, output_ch: Chain):
    lof: list[Chain] = [Chain(val) for val in tks]
    for ch in lof:
        input_ch.next.append(ch)
        ch.next.append(output_ch)


v = and_selector(
TKP(name = 'OPEN_BRACKET', tk = open_bracket, sequence=False, optional=False),
    or_selector(TKP(name = 'SLASH', tk = slash, sequence=False, optional=False),),
    TKP(name = 'CLOSE_BRACKET', tk = close_bracket, sequence=False, optional=False)
)
from IPython import embed
embed()

primeiro = v.next[0]