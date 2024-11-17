from collections.abc import Iterable
from dataclasses import dataclass, field
from collections import defaultdict
from enum import Enum, auto
import re

def regex_finder(text: str, pattern: str) -> list[tuple[int, int, str]]:
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.end(), match.group()))
    return matches

open_bracket = dict(scan = lambda text: regex_finder(text, pattern="<"), right = [], sequence = False, optional = False)
slash = dict(scan = lambda text: regex_finder(text, pattern="/"), right = [], sequence = False, optional = False)
close_bracket = dict(scan = lambda text: regex_finder(text, pattern=">"), right = [], sequence = False, optional = False)


def and_selector(*tks, visitor: callable):
    d_tks = tuple(tks)
    r_tks = d_tks[::-1]
    dd = dict()

    for tk1, tk2 in zip(d_tks[:-1], d_tks[1:]):
        tk1['right'].append(tk2)

        if tk1['sequence']:
            tk1['right'].append(tk1)


    for tk1, tk2 in zip(r_tks[:-1], r_tks[1:]):
        if tk1['optional'] and len(tk1['right']) > 0:
            tk2['right'](*tk1['right'])
        pass

    for idx, tk in enumerate(d_tks):
        yield idx, tk

def one_selector(tk:dict[int, dict]):
    yield {
        'pos': 0,
        'tk': tk,
        'right': [],
        'sequence' : False,
        'optional': False
    }

    raise StopIteration("")

def zero_or_one_selector(tk: dict[int, dict]):
    yield {
        'pos': 0,
        'tk': tk,
        'right': [],
        'optional' : True,
        'sequence' : False,
    }

    raise StopIteration("")



for val in and_selector(open_bracket, slash, close_bracket, visitor=None):
    print(val)
    pass

