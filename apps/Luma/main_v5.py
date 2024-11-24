

code = "<wolfram.Math instance=[Ship, Algo] anotherParameter={name: Henrique} thirdParameter=<anotherXmlThing></anotherXmlThing>>"

root = None

from abc import ABC, abstractmethod
from dataclasses import dataclass
from os import name

@dataclass
class Token:
    name: str
    scan: Scanner
    zero: bool
    many: bool
    pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, text: str):
        pass

class RegexFinder(Scanner, Token):
    def __init__(self, pattern: str, zero: bool, many: bool, name: str):
        self.pattern = pattern
        Scanner.__init__(self)
        Token.__init__(self, name = name, zero = zero, many = many)
        pass

    def scan(self, text: str):
        pass # Aqui fica a lógica 

open_bracket = RegexFinder(pattern = '<', name="OPEN_BRACKET", zero=False, many=False)
close_bracket = RegexFinder(pattern = '>', zero = False, many=False, name="CLOSE_BRACKET")
b_identifier = RegexFinder(pattern = "^[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*$", zero = False, many=False, name="IDENTIFIER")
close_bracket = RegexFinder(pattern = '>', zero = False, many=False, name="CLOSE_BRACKET")
equal = RegexFinder(pattern = '=', zero = False, many=False, name="EQUAL")

open_quote = RegexFinder(pattern = '[', zero = False, many=False, name="OPEN_QUOTE")
close_quote = RegexFinder(pattern = ']', zero = False, many=False, name="CLOSE_QUOTE")
comma = RegexFinder(pattern = ',', zero = False, many=False, name="COMMA")
open_key = RegexFinder(pattern = '{', zero = False, many=False, name="OPEN_KEY")
two_dots = RegexFinder(pattern = ':', zero = False, many=False, name="TWO_DOTS")
close_key = RegexFinder(pattern = '}', zero = False, many=False, name="CLOSE_KEY")

class Statement(ABC):
    pass

class And(Statement):
    pass

class Or(Statement):
    pass

class ZeroToMany(Statement):
    pass

array_identifier = And(
    open_quote,
    b_identifier,
    ZeroToMany(
        comma,
        b_identifier
    ),
    close_quote
)

object_identifier = And(
    open_key ,
    b_identifier,
    two_dot,
    b_identifier
    ZeroToMany(
        comma,
        b_identifier,
        two_dot,
        b_identifier
    ),
    close_quote
)




c_identifier = Or(
    array_identifier,
    object_identifier
)


attributes = And(
    b_identifier,
    equal,
    c_identifier
)


xmlStmt = And(
    open_bracket,
    b_identifier,
    attributes,
    close_bracket,
)

commentStmt = And(
    required,
    identifier,
)

root = Or(
    xmlStmt,
    commentStmt,
)




