import re
from abc import ABC, abstractmethod
from enum import Enum

class Prototype:
    ONLY_LOCAL = 1
    FORWARD = 2
    BACKWARD = 3
    GLOBAL = 4

class PrototypeContext:
    def __init__(self, name: str):
        self.name = name
        self.data = dict()
        self.forward = None
        self.backward = None

    def get(self, key: str, default=None, propagation=Prototype.ONLY_LOCAL):
        if propagation == Prototype.ONLY_LOCAL:
            return self.data.get(key, default)
        elif propagation == Prototype.FORWARD:
            value = self.data.get(key, None)
            if value is None and self.forward:
                return self.forward.get(key, default, propagation)
            return value if value is not None else default
        elif propagation == Prototype.BACKWARD:
            value = self.data.get(key, None)
            if value is None and self.backward:
                return self.backward.get(key, default, propagation)
            return value if value is not None else default
        elif propagation == Prototype.GLOBAL:
            # Search both backward and forward
            value = self.data.get(key, None)
            if value is not None:
                return value
            if self.backward:
                value = self.backward.get(key, default, propagation)
                if value is not None:
                    return value
            if self.forward:
                value = self.forward.get(key, default, propagation)
                if value is not None:
                    return value
            return default
        else:
            return default

    def set(self, key, value):
        self.data[key] = value

    def append_child_context(self, name):
        child_context = PrototypeContext(name)
        child_context.backward = self
        self.forward = child_context
        return child_context

class Consumer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.line = 1
        self.column = 1
        self.length = len(text)

    def peek(self, n=1):
        end = min(self.position + n, self.length)
        return self.text[self.position:end]

    def consume(self, n=1):
        consumed = self.text[self.position:self.position + n]
        self.position += n
        for c in consumed:
            if c == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
        return consumed

    def get_value(self):
        return self.consume(1)

    def finished(self):
        return self.position >= self.length

    def get_actual_position_consumer(self):
        return self.line, self.column

class IMicroInterpreter(ABC):
    def __init__(self, identifier, representation, *dim, **kdim):
        self.identifier = identifier
        self.representation = representation
        self.dim = dim
        self.kdim = kdim
        self.children = []
        self.tokens = []

    def get_parser_sequence(self):
        return iter([self])

    @classmethod
    def start_consume(cls, text):
        return Consumer(text)

    @classmethod
    def select_candidate(cls, parsers: list['IMicroInterpreter'], consumer, min_look_ahead=1, max_look_ahead=10):
        for parser in parsers:
            original_position = consumer.position
            result = parser.match(consumer)
            if result is not None:
                return parser
            consumer.position = original_position  # Reset position if no match
        return None

    @classmethod
    def parse(cls, parser, text: str):
        sequence_parser = parser.get_parser_sequence()
        prototype_context = PrototypeContext(name="root")
        consumer = cls.start_consume(text)
        previous_parser = None
        actual_parser = next(sequence_parser)
        while not consumer.finished():
            ln_begin, cl_begin = consumer.get_actual_position_consumer()
            parser_choosed = cls.select_candidate([actual_parser], consumer, min_look_ahead=1, max_look_ahead=10)
            if not parser_choosed:
                print(f"Error parsing at line {ln_begin}, column {cl_begin}")
                break
            value = parser_choosed.match(consumer)
            ln_end, cl_end = consumer.get_actual_position_consumer()
            prototype_context.set(parser_choosed.identifier, {
                'start': (ln_begin, cl_begin),
                'end': (ln_end, cl_end),
                'value': value
            })
            previous_parser = actual_parser
            try:
                actual_parser = next(sequence_parser)
            except StopIteration:
                break
            if actual_parser.is_child_of(previous_parser):
                prototype_context = prototype_context.append_child_context(actual_parser.identifier)
        return prototype_context.data

    def compose(self, **kwargs):
        pass

    def is_child_of(self, other):
        return self in getattr(other, 'children', [])

    @abstractmethod
    def match(self, consumer):
        pass

letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'

class Exactrepresentation(IMicroInterpreter):
    def compose(self, **kwargs):
        return self

    def match(self, consumer):
        text = consumer.text[consumer.position:]
        if text.startswith(self.representation):
            consumer.consume(len(self.representation))
            return self.representation
        return None

class ClassicRegex(IMicroInterpreter):
    def compose(self, **kwargs):
        self.pattern = re.compile(self.representation)
        return self

    def match(self, consumer):
        text = consumer.text[consumer.position:]
        match = self.pattern.match(text)
        if match:
            consumer.consume(match.end())
            return match.group()
        return None

class ANTLR4Like(IMicroInterpreter):
    def compose(self, **kwargs):
        self.children = kwargs.get('context', [])
        self.propagation = kwargs.get('propagation', {})
        return self

    def get_parser_sequence(self):
        return iter(self.children)

    def match(self, consumer):
        original_position = consumer.position
        results = []
        for child in self.children:
            result = child.match(consumer)
            if result is None:
                consumer.position = original_position  # Reset position
                return None
            results.append(result)
        return ''.join(results)

require = Exactrepresentation(identifier='REQUIRE', representation='require').compose()
comma = Exactrepresentation(identifier='COMMA', representation=',').compose()
equals = Exactrepresentation(identifier='EQUALS', representation='=').compose()
open_bracket = Exactrepresentation(identifier='OPEN_BRACKET', representation='[').compose()
close_bracket = Exactrepresentation(identifier='CLOSE_BRACKET', representation=']').compose()
open_key = Exactrepresentation(identifier='OPEN_KEY', representation='{').compose()
close_key = Exactrepresentation(identifier='CLOSE_KEY', representation='}').compose()
two_dots = Exactrepresentation(identifier='TWO_DOTS', representation=':').compose()
open_element = Exactrepresentation(identifier='OPEN_ELEMENT', representation='<').compose()
close_element = Exactrepresentation(identifier='CLOSE_ELEMENT', representation='>').compose()
slash = Exactrepresentation(identifier='SLASH', representation='/').compose()
identifier = ClassicRegex(identifier='IDENTIFIER', representation=f'{letter_pattern}{letter_or_digit}*').compose()
q_identifier = ClassicRegex(identifier='Q_IDENTIFIER', representation=f'{letter_pattern}{letter_or_digit}*(?:\\.{letter_pattern}{letter_or_digit}*)*').compose()
comment = ClassicRegex(identifier='COMMENT', representation=r'\#.*[\r\n]').compose()
no_representation_tokens_complete = ClassicRegex(identifier='NO_representation_TOKEN', representation=r'[\r\n\t ]+').compose()
no_representation_tokens_without_space = ClassicRegex(identifier='NO_representation_TOKEN', representation=r'[\r\n\t]+').compose()

# Forward declarations
program = None
vector = None
object_ = None

vector = ANTLR4Like(identifier='VECTOR', representation='').compose(
    context=[
        open_bracket,
        q_identifier,
        ANTLR4Like(identifier='Q_IDENTIFIER_LIST', representation='').compose(
            context=[
                ANTLR4Like(identifier='Q_IDENTIFIER_ITEM', representation='').compose(
                    context=[comma, q_identifier]
                )
            ]
        ),
        close_bracket
    ]
)

object_ = ANTLR4Like(identifier='OBJECT', representation='').compose(
    context=[
        open_key,
        q_identifier,
        two_dots,
        lambda consumer: program.match(consumer),  # Recursive call
        close_key
    ]
)

def get_t_identifier():
    return ANTLR4Like(identifier='T_IDENTIFIER', representation='').compose(
        context=[
            vector,
            object_,
            program  # Reference to program to allow nesting
        ]
    )

t_identifier = get_t_identifier()

xml_attribute = ANTLR4Like(identifier='XML_ATTRIBUTE', representation='').compose(
    context=[q_identifier, equals, t_identifier]
)

open_tag = ANTLR4Like(identifier='OPEN_TAG', representation='').compose(
    context=[
        open_element,
        q_identifier,
        ANTLR4Like(identifier='XML_ATTRIBUTE_LIST', representation='').compose(
            context=[xml_attribute]
        ),
        close_element
    ]
)

close_tag = ANTLR4Like(identifier='CLOSE_TAG', representation='').compose(
    context=[open_element, slash, q_identifier, close_element]
)

xml_statement = ANTLR4Like(identifier='XML_STATEMENT', representation='').compose(
    context=[open_tag, lambda consumer: program.match(consumer), close_tag]
)

import_statement = ANTLR4Like(identifier='IMPORT_STATEMENT', representation='').compose(
    context=[require, identifier]
)

program = ANTLR4Like(identifier='PROGRAM', representation='').compose(
    context=[xml_statement, import_statement, comment, no_representation_tokens_complete]
)

# Sample Code
code = """
<code>
    require Ship
    <wolfram.Math instance=[Ship, Algo] anotherParameter={identifier: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

# Parsing the Code
parsed_output = program.parse(program, code)
print(parsed_output)
