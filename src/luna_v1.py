
# Padrões básicos
from abc import ABC


from enum import Enum

class DiaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7


class Propagation(Enum):
    ONLY_LOCAL = 1
    PROPAGATE_TO_CHILD_NODES = 2
    PROPAGATE_TO_FATHER_NODES = 3
    GLOBAL = 4

letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'

# [TODO] Terminar implementação
class IParserTransformer(ABC):
    def __init__(self, name, value, *dim, **kdim) -> None:
        self.name = name
        self.value = value
        self.dim = dim
        self.kdim = kdim
        pass

# [TODO] Terminar implementação
class ExactValue(IParserTransformer):
    pass

# [TODO] Terminar implementação
class ClassicRegex(IParserTransformer):
    pass

# [TODO] Terminar implementação
class ANTLR4Like(IParserTransformer):
    pass


extra_pattern_like_tokens = [
    ExactValue(name = 'OPEN_ELEMENT', value = '<'),
    ExactValue(name = 'CLOSE_ELEMENT', value = '>'),
    ExactValue(name = 'OPEN_ELEMENT', value = '<'),
    ClassicRegex(name = 'DIGIT', value = digit_pattern),
    ClassicRegex(name = 'IDENTIFIER', value=f'{letter_pattern}{letter_or_digit}*'),
    ClassicRegex(name = 'Q_IDENTIFIER', value=f'{letter_pattern}{letter_or_digit}*(?:\\.{letter_pattern}{letter_or_digit}*)*',),
    ExactValue(name = 'EQUALS', value = '='),
    ExactValue(name = 'OPEN_BRACKET', value = '['),
    ExactValue(name = 'CLOSE_BRACKET', value = ']'),
    ExactValue(name = 'SLASH', value='/'),
    ExactValue(name = 'OPEN_KEY', value='{'),
    ExactValue(name = 'CLOSE_KEY', value='}'),
    ExactValue(name = 'TWO_DOTS', value=':'),
]

program = ANTLR4Like(name = 'PROGRAM', value = '(&XML_STATEMENT | &IMPORT_STATEMENT)')

xml_statement = ANTLR4Like(name = 'XML_STATEMENT', value='&OPEN_TAG &PROGRAM &CLOSE_TAG')
import_statement = ANTLR4Like(name = 'IMPORT_STATEMENT', value='&REQUIRE &IDENTIFIER')

open_tag = ANTLR4Like(name = 'OPEN_TAG', value='&OPEN_ELEMENT &Q_IDENTIFIER &XML_ATTRIBUTE*? &CLOSE_ELEMENT')
close_tag = ANTLR4Like(name = 'CLOSE_TAG', value='&OPEN_ELEMENT &SLASH &Q_IDENTIFIER &CLOSE_ELEMENT')
require = ExactValue(name = 'REQUIRE', value = 'require')

xml_attribute = ANTLR4Like(name = 'XML_ATTRIBUTE', value = '&Q_IDENTIFIER &EQUAL &T_IDENTIFIER')


t_identifier = ANTLR4Like(name = 'T_IDENTIFIER', value = '&VECTOR | &OBJECT | &PROGRAM')

vector = ANTLR4Like(name = 'VECTOR', value='&OPEN_BRACKET Q_IDENTIFIER (&COMMA Q_IDENTIFIER)* &CLOSE_BRACKET')

object = ANTLR4Like(name = 'OBJECT', value='&OPEN_KEY &Q_IDENTIFIER &TWO_DOT &PROGRAM')


program.compose(
    propagation = {
        Propagation.PROPAGATE_TO_CHILD_NODES: extra_pattern_like_tokens,
    },
    values = [
        xml_statement.compose(
            values = [
                open_tag.compose(
                    values = xml_attribute.compose(
                        value = [
                            t_identifier.compose(
                            values = [
                                vector.compose(),
                                object.compose(),
                                program.compose(),
                            ]
                        )
                        ],
                    ),
                ),
                close_tag.compose(),
                program.compose(),
            ],
        ),
        import_statement.compose(
            values = [
                require.compose(),
            ]
        ),
    ]
)

code = """
<code>
    <wolfram.Math instance=[Ship, Algo] anotherParameter={name: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

program.match_many(code)
