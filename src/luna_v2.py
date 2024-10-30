# Padrões básicos
import re
from abc import ABC, abstractmethod
from enum import Enum



class Propagation(Enum):
    ONLY_LOCAL = 1
    PROPAGATE_TO_CHILD_NODES = 2
    PROPAGATE_TO_FATHER_NODES = 3
    GLOBAL = 4

letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'

# Base Parser Transformer Interface
class IParserTransformer(ABC):
    def __init__(self, name, value, *dim, **kdim):
        self.name = name
        self.value = value
        self.dim = dim
        self.kdim = kdim
        self.children = []
        self.tokens = []
    
    @abstractmethod
    def compose(self, **kwargs):
        pass
    
    @abstractmethod
    def match(self, text):
        pass

    @abstractmethod
    def match_many(self, text):
        pass

# Exact Value Matcher
class ExactValue(IParserTransformer):
    def compose(self, **kwargs):
        return self
    
    def match(self, text):
        if text.startswith(self.value):
            return self.value, text[len(self.value):]
        return None, text

# Regular Expression Matcher
class ClassicRegex(IParserTransformer):
    def compose(self, **kwargs):
        self.pattern = re.compile(self.value)
        return self
    
    def match(self, text):
        match = self.pattern.match(text)
        if match:
            return match.group(), text[match.end():]
        return None, text

# ANTLR4-Like Grammar Parser
class ANTLR4Like(IParserTransformer):
    def compose(self, **kwargs):
        self.children = kwargs.get('values', [])
        self.propagation = kwargs.get('propagation', {})
        # Propagate tokens if needed
        for prop_type, tokens in self.propagation.items():
            if prop_type == Propagation.PROPAGATE_TO_CHILD_NODES:
                for child in self.children:
                    child.tokens.extend(tokens)
        return self
    
    def match(self, text):
        original_text = text
        results = []
        for child in self.children:
            result, text = child.match(text)
            if result is None:
                return None, original_text
            results.append(result)
        return results, text

# Additional Tokens and Grammar Rules
extra_pattern_like_tokens = [
    ExactValue(name='OPEN_ELEMENT', value='<'),
    ExactValue(name='CLOSE_ELEMENT', value='>'),
    ClassicRegex(name='DIGIT', value=digit_pattern),
    ClassicRegex(name='IDENTIFIER', value=f'{letter_pattern}{letter_or_digit}*'),
    ClassicRegex(name='Q_IDENTIFIER', value=f'{letter_pattern}{letter_or_digit}*(?:\\.{letter_pattern}{letter_or_digit}*)*'),
    ExactValue(name='EQUALS', value='='),
    ExactValue(name='OPEN_BRACKET', value='['),
    ExactValue(name='CLOSE_BRACKET', value=']'),
    ExactValue(name='SLASH', value='/'),
    ExactValue(name='OPEN_KEY', value='{'),
    ExactValue(name='CLOSE_KEY', value='}'),
    ExactValue(name='TWO_DOTS', value=':'),
    ExactValue(name='COMMA', value=','),
]

# Grammar Definitions
require = ExactValue(name='REQUIRE', value='require').compose()
comma = ExactValue(name='COMMA', value=',').compose()
equals = ExactValue(name='EQUALS', value='=').compose()
open_bracket = ExactValue(name='OPEN_BRACKET', value='[').compose()
close_bracket = ExactValue(name='CLOSE_BRACKET', value=']').compose()
open_key = ExactValue(name='OPEN_KEY', value='{').compose()
close_key = ExactValue(name='CLOSE_KEY', value='}').compose()
two_dots = ExactValue(name='TWO_DOTS', value=':').compose()
open_element = ExactValue(name='OPEN_ELEMENT', value='<').compose()
close_element = ExactValue(name='CLOSE_ELEMENT', value='>').compose()
slash = ExactValue(name='SLASH', value='/').compose()
identifier = ClassicRegex(name='IDENTIFIER', value=f'{letter_pattern}{letter_or_digit}*').compose()
q_identifier = ClassicRegex(name='Q_IDENTIFIER', value=f'{letter_pattern}{letter_or_digit}*(?:\\.{letter_pattern}{letter_or_digit}*)*').compose()

# Define t_identifier first to use in xml_attribute
def get_t_identifier():
    return ANTLR4Like(name='T_IDENTIFIER', value='&VECTOR | &OBJECT | &PROGRAM').compose(
        values=[
            vector.compose(),
            object_.compose(),
            program  # Reference to program to allow nesting
        ]
    )

# Forward declarations to handle recursive definitions
program = None
vector = None
object_ = None

# Define Grammar Rules
def build_grammar():
    global program, vector, object_

    # VECTOR Rule
    vector = ANTLR4Like(name='VECTOR', value='&OPEN_BRACKET &Q_IDENTIFIER (&COMMA &Q_IDENTIFIER)* &CLOSE_BRACKET').compose(
        values=[
            open_bracket,
            q_identifier,
            ANTLR4Like(name='Q_IDENTIFIER_LIST', value='(&COMMA &Q_IDENTIFIER)*').compose(
                values=[
                    ANTLR4Like(name='Q_IDENTIFIER_ITEM', value='&COMMA &Q_IDENTIFIER').compose(
                        values=[comma, q_identifier]
                    )
                ]
            ),
            close_bracket
        ]
    )

    # OBJECT Rule
    object_ = ANTLR4Like(name='OBJECT', value='&OPEN_KEY &Q_IDENTIFIER &TWO_DOTS &PROGRAM &CLOSE_KEY').compose(
        values=[
            open_key,
            q_identifier,
            two_dots,
            lambda text: program.match(text),  # Recursive call to program
            close_key
        ]
    )

    # T_IDENTIFIER Rule
    t_identifier = get_t_identifier()

    # XML_ATTRIBUTE Rule
    xml_attribute = ANTLR4Like(name='XML_ATTRIBUTE', value='&Q_IDENTIFIER &EQUALS &T_IDENTIFIER').compose(
        values=[q_identifier, equals, t_identifier]
    )

    # OPEN_TAG Rule
    open_tag = ANTLR4Like(name='OPEN_TAG', value='&OPEN_ELEMENT &Q_IDENTIFIER &XML_ATTRIBUTE* &CLOSE_ELEMENT').compose(
        values=[
            open_element,
            q_identifier,
            ANTLR4Like(name='XML_ATTRIBUTE_LIST', value='&XML_ATTRIBUTE*').compose(
                values=[xml_attribute]
            ),
            close_element
        ]
    )

    # CLOSE_TAG Rule
    close_tag = ANTLR4Like(name='CLOSE_TAG', value='&OPEN_ELEMENT &SLASH &Q_IDENTIFIER &CLOSE_ELEMENT').compose(
        values=[open_element, slash, q_identifier, close_element]
    )

    # XML_STATEMENT Rule
    xml_statement = ANTLR4Like(name='XML_STATEMENT', value='&OPEN_TAG &PROGRAM &CLOSE_TAG').compose(
        values=[open_tag, lambda text: program.match(text), close_tag]
    )

    # IMPORT_STATEMENT Rule
    import_statement = ANTLR4Like(name='IMPORT_STATEMENT', value='&REQUIRE &IDENTIFIER').compose(
        values=[require, identifier]
    )

    # PROGRAM Rule
    program = ANTLR4Like(name='PROGRAM', value='(&XML_STATEMENT | &IMPORT_STATEMENT)').compose(
        values=[xml_statement, import_statement],
        
    )

build_grammar()



# Sample Code
code = """
<code>
    <wolfram.Math instance=[Ship, Algo] anotherParameter={name: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

# Parsing the Code
parsed_output = program.match_many(code)
print(parsed_output)
