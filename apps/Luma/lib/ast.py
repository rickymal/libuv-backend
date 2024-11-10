from enum import Enum
from dataclasses import dataclass, field
from typing import List, Tuple, Optional



class SequenceType(Enum):
    SEQUENTIAL = 0 # dESCREve uqe temos uma sequencia
    OPTIONAL = 1 #quando temos um caracteres como 'optional'
    INFINITY = 2 #quando temos um caractere como asterístico,
    PRIMITIVE = 3 # são os outros finders, caso seja regex finder ou literal finder
    ROOT = 4 #
    PARENTHESIS = 5 # contido no parentese
    OR_LOGIC = 6 # contem lógica "OU" xom
    REGEX = 7
    LITERAL = 8
    IDENTIFIER = 9
