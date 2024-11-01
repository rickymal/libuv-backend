import re
from abc import ABC, abstractmethod

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

    def get_value(self, n=1):
        return self.consume(n)

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
        self.context = {}

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
                return parser, result
            consumer.position = original_position  # Reset position if no match
        return None, None

    @classmethod
    def parse(cls, parser, text: str):
        sequence_parser = parser.get_parser_sequence()
        prototype_context = PrototypeContext(name="root")
        consumer = cls.start_consume(text)
        previous_parser = None
        actual_parser = next(sequence_parser)
        while not consumer.finished():
            ln_begin, cl_begin = consumer.get_actual_position_consumer()
            parser_choosed, value = cls.select_candidate([actual_parser], consumer, min_look_ahead=1, max_look_ahead=10)
            if not parser_choosed:
                print(f"Error parsing at line {ln_begin}, column {cl_begin}")
                break
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
        self.context = kwargs.get('context', {})
        self.propagation = kwargs.get('propagation', {})
        return self

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
        self.context = kwargs.get('context', {})
        self.propagation = kwargs.get('propagation', {})
        self.parser_sequence = self.build_parser_sequence()
        return self

    def build_parser_sequence(self):
        tokens = self.tokenize_representation(self.representation)
        sequence = self.parse_expression(tokens)
        return sequence

    def tokenize_representation(self, representation):
        # Simple tokenizer for the representation string
        tokens = []
        i = 0
        while i < len(representation):
            c = representation[i]
            if c.isspace():
                i += 1
                continue
            elif c == '&':
                # Reference to a subparser
                i += 1
                start = i
                while i < len(representation) and (representation[i].isalnum() or representation[i] == '_'):
                    i += 1
                tokens.append(('REF', representation[start:i]))
            elif c in '()*+?|':
                tokens.append((c, c))
                i += 1
            else:
                # Unexpected character
                i += 1
        return tokens

    def parse_expression(self, tokens):
        # Parse alternation expressions separated by '|'
        self.tokens = tokens
        self.pos = 0
        return self._parse_expression()

    def _parse_expression(self):
        options = [self._parse_term()]
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == '|':
            self.pos += 1  # Consume '|'
            options.append(self._parse_term())
        if len(options) == 1:
            return options[0]
        else:
            return {'type': 'OR', 'options': options}

    def _parse_term(self):
        sequence = []
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] not in '|)':
            factor = self._parse_factor()
            if factor is not None:
                sequence.append(factor)
        return sequence

    def _parse_factor(self):
        token = self.tokens[self.pos]
        if token[0] == 'REF':
            parser_name = token[1]
            self.pos += 1
            quantifier = None
            if self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('*', '+', '?'):
                quantifier = self.tokens[self.pos][0]
                self.pos += 1
            return {'type': 'REF', 'name': parser_name, 'quantifier': quantifier}
        elif token[0] == '(':
            self.pos += 1
            expr = self._parse_expression()
            if self.pos >= len(self.tokens) or self.tokens[self.pos][0] != ')':
                raise ValueError("Expected ')'")
            self.pos += 1  # Consume ')'
            quantifier = None
            if self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('*', '+', '?'):
                quantifier = self.tokens[self.pos][0]
                self.pos += 1
            return {'type': 'GROUP', 'expr': expr, 'quantifier': quantifier}
        else:
            raise ValueError(f"Unexpected token {token}")

    def get_parser_by_name(self, name):
        parser = self.context.get(name)
        if parser is None:
            raise ValueError(f"Parser '{name}' not found in context")
        return parser

    def match(self, consumer):
        return self.match_expr(self.parser_sequence, consumer)

    def match_expr(self, expr, consumer):
        if isinstance(expr, dict):
            if expr['type'] == 'OR':
                for option in expr['options']:
                    original_position = consumer.position
                    result = self.match_expr(option, consumer)
                    if result is not None:
                        return result
                    consumer.position = original_position  # Backtrack
                return None
            elif expr['type'] == 'REF':
                parser = self.get_parser_by_name(expr['name'])
                return self.match_with_quantifier(parser, expr.get('quantifier'), consumer)
            elif expr['type'] == 'GROUP':
                return self.match_with_quantifier(expr['expr'], expr.get('quantifier'), consumer)
        elif isinstance(expr, list):
            original_position = consumer.position
            results = []
            for item in expr:
                result = self.match_expr(item, consumer)
                if result is None:
                    consumer.position = original_position  # Backtrack
                    return None
                results.append(result)
            return results
        else:
            raise ValueError("Invalid expression in parser sequence")

    def match_with_quantifier(self, parser, quantifier, consumer):
        results = []
        count = 0
        while True:
            original_position = consumer.position
            if isinstance(parser, IMicroInterpreter):
                result = parser.match(consumer)
            else:
                result = self.match_expr(parser, consumer)
            if result is not None:
                results.append(result)
                count += 1
                if quantifier == '?' or quantifier is None:
                    break
            else:
                consumer.position = original_position
                break
            if quantifier == '?' or quantifier == '':
                break
        if quantifier == '+' and count == 0:
            return None
        return results


# Define tokens and parsers

letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'

# Tokens
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
comment = ClassicRegex(identifier='COMMENT', representation=r'\#.*').compose()
whitespace = ClassicRegex(identifier='WHITESPACE', representation=r'[ \t\r\n]+').compose()

# Build context dictionary
context = {
    'REQUIRE': require,
    'COMMA': comma,
    'EQUALS': equals,
    'OPEN_BRACKET': open_bracket,
    'CLOSE_BRACKET': close_bracket,
    'OPEN_KEY': open_key,
    'CLOSE_KEY': close_key,
    'TWO_DOTS': two_dots,
    'OPEN_ELEMENT': open_element,
    'CLOSE_ELEMENT': close_element,
    'SLASH': slash,
    'IDENTIFIER': identifier,
    'Q_IDENTIFIER': q_identifier,
    'COMMENT': comment,
    'WHITESPACE': whitespace,
}

# Forward declarations
program = None
vector = None
object_ = None
t_identifier = None
xml_attribute = None
open_tag = None
close_tag = None
xml_statement = None
import_statement = None

# Define VECTOR rule
vector = ANTLR4Like(identifier='VECTOR', representation='&OPEN_BRACKET &Q_IDENTIFIER (&COMMA &Q_IDENTIFIER)* &CLOSE_BRACKET').compose(
    context=context
)

# Define OBJECT rule
object_ = ANTLR4Like(identifier='OBJECT', representation='&OPEN_KEY &Q_IDENTIFIER &TWO_DOTS &PROGRAM &CLOSE_KEY').compose(
    context=context
)

# Define T_IDENTIFIER rule
context['VECTOR'] = vector
context['OBJECT'] = object_

t_identifier = ANTLR4Like(identifier='T_IDENTIFIER', representation='&VECTOR | &OBJECT | &PROGRAM').compose(
    context=context
)

context['T_IDENTIFIER'] = t_identifier

# Define XML_ATTRIBUTE rule
xml_attribute = ANTLR4Like(identifier='XML_ATTRIBUTE', representation='&Q_IDENTIFIER &EQUALS &T_IDENTIFIER').compose(
    context=context
)

context['XML_ATTRIBUTE'] = xml_attribute

# Define OPEN_TAG rule
xml_attribute_list = ANTLR4Like(identifier='XML_ATTRIBUTE_LIST', representation='(&XML_ATTRIBUTE &WHITESPACE*)*').compose(
    context=context
)

context['XML_ATTRIBUTE_LIST'] = xml_attribute_list

open_tag = ANTLR4Like(identifier='OPEN_TAG', representation='&OPEN_ELEMENT &Q_IDENTIFIER &WHITESPACE* &XML_ATTRIBUTE_LIST &CLOSE_ELEMENT').compose(
    context=context
)

context['OPEN_TAG'] = open_tag

# Define CLOSE_TAG rule
close_tag = ANTLR4Like(identifier='CLOSE_TAG', representation='&OPEN_ELEMENT &SLASH &Q_IDENTIFIER &CLOSE_ELEMENT').compose(
    context=context
)

context['CLOSE_TAG'] = close_tag

# Define XML_STATEMENT rule
xml_statement = ANTLR4Like(identifier='XML_STATEMENT', representation='&OPEN_TAG &PROGRAM* &CLOSE_TAG').compose(
    context=context
)

context['XML_STATEMENT'] = xml_statement

# Define IMPORT_STATEMENT rule
import_statement = ANTLR4Like(identifier='IMPORT_STATEMENT', representation='&REQUIRE &WHITESPACE+ &IDENTIFIER').compose(
    context=context
)

context['IMPORT_STATEMENT'] = import_statement

# Define PROGRAM rule
program = ANTLR4Like(identifier='PROGRAM', representation='(&XML_STATEMENT | &IMPORT_STATEMENT | &COMMENT | &WHITESPACE)+').compose(
    context=context
)

context['PROGRAM'] = program

if __name__ == "__main__":
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


# test_parsers.py

import pytest

# Supondo que as classes estejam em um módulo chamado 'parsers'
# from parsers import Exactrepresentation, ClassicRegex, Consumer

# Para este exemplo, vou assumir que as classes estão disponíveis no contexto atual.

# Teste 1: Teste de correspondência exata bem-sucedida
def test_exactrepresentation_success():
    parser = Exactrepresentation(identifier='HELLO', representation='hello').compose()
    consumer = Consumer('hello world')
    result = parser.match(consumer)
    assert result == 'hello'
    assert consumer.position == 5  # 'hello' tem 5 caracteres

# Teste 2: Teste de correspondência exata falha
def test_exactrepresentation_failure():
    parser = Exactrepresentation(identifier='HELLO', representation='hello').compose()
    consumer = Consumer('world hello')
    result = parser.match(consumer)
    assert result is None
    assert consumer.position == 0  # A posição não deve avançar

# Teste 3: Teste de correspondência de regex bem-sucedida
def test_classicregex_success():
    parser = ClassicRegex(identifier='DIGITS', representation=r'\d+').compose()
    consumer = Consumer('123abc')
    result = parser.match(consumer)
    assert result == '123'
    assert consumer.position == 3  # '123' tem 3 caracteres

# Teste 4: Teste de correspondência de regex falha
def test_classicregex_failure():
    parser = ClassicRegex(identifier='DIGITS', representation=r'\d+').compose()
    consumer = Consumer('abc123')
    result = parser.match(consumer)
    assert result is None
    assert consumer.position == 0  # A posição não deve avançar

# Teste 5: Teste de correspondência exata com consumo completo
def test_exactrepresentation_full_consumption():
    parser = Exactrepresentation(identifier='HELLO', representation='hello').compose()
    consumer = Consumer('hello world')
    result = parser.match(consumer)
    assert result == 'hello'
    assert consumer.position == 5  # Verifica se consumiu exatamente 5 caracteres

# Teste 6: Teste de correspondência de regex com consumo parcial
def test_classicregex_partial_consumption():
    parser = ClassicRegex(identifier='WORD', representation=r'\w+').compose()
    consumer = Consumer('hello world')
    result = parser.match(consumer)
    assert result == 'hello'
    assert consumer.position == 5  # 'hello' tem 5 caracteres

# Teste 7: Teste de sequência de parsers
def test_sequence_of_parsers():
    parser1 = Exactrepresentation(identifier='HELLO', representation='hello').compose()
    parser2 = Exactrepresentation(identifier='SPACE', representation=' ').compose()
    parser3 = ClassicRegex(identifier='WORD', representation=r'\w+').compose()
    consumer = Consumer('hello world')
    
    result1 = parser1.match(consumer)
    assert result1 == 'hello'
    assert consumer.position == 5
    
    result2 = parser2.match(consumer)
    assert result2 == ' '
    assert consumer.position == 6
    
    result3 = parser3.match(consumer)
    assert result3 == 'world'
    assert consumer.position == 11

# Teste 8: Teste de correspondência exata sensível a maiúsculas e minúsculas
def test_exactrepresentation_case_sensitive():
    parser = Exactrepresentation(identifier='Hello', representation='Hello').compose()
    consumer = Consumer('hello world')
    result = parser.match(consumer)
    assert result is None
    assert consumer.position == 0  # Não deve avançar porque é case-sensitive

# Teste 9: Teste de correspondência de regex com caracteres especiais
def test_classicregex_special_characters():
    parser = ClassicRegex(identifier='DOMAIN', representation=r'\w+\.\w+').compose()
    consumer = Consumer('example.com is a domain')
    result = parser.match(consumer)
    assert result == 'example.com'
    assert consumer.position == 11  # 'example.com' tem 11 caracteres

# Teste 10: Teste de correspondência exata em string vazia
def test_exactrepresentation_empty_string():
    parser = Exactrepresentation(identifier='HELLO', representation='hello').compose()
    consumer = Consumer('')
    result = parser.match(consumer)
    assert result is None
    assert consumer.position == 0  # A posição permanece no início

# test_antlr4like.py

import pytest

# Supondo que os parsers e o contexto estejam definidos em um módulo chamado 'parsers'
# from parsers import ANTLR4Like, Exactrepresentation, ClassicRegex, Consumer

# Para este exemplo, vamos supor que os parsers e o contexto estão disponíveis no escopo atual

# Preparar o contexto com parsers básicos
letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'

# Tokens
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
comment = ClassicRegex(identifier='COMMENT', representation=r'\#.*').compose()
whitespace = ClassicRegex(identifier='WHITESPACE', representation=r'[ \t\r\n]+').compose()

# Construir o dicionário de contexto
context = {
    'REQUIRE': require,
    'COMMA': comma,
    'EQUALS': equals,
    'OPEN_BRACKET': open_bracket,
    'CLOSE_BRACKET': close_bracket,
    'OPEN_KEY': open_key,
    'CLOSE_KEY': close_key,
    'TWO_DOTS': two_dots,
    'OPEN_ELEMENT': open_element,
    'CLOSE_ELEMENT': close_element,
    'SLASH': slash,
    'IDENTIFIER': identifier,
    'Q_IDENTIFIER': q_identifier,
    'COMMENT': comment,
    'WHITESPACE': whitespace,
}

# Definir parsers a serem usados nos testes
vector = ANTLR4Like(identifier='VECTOR', representation='&OPEN_BRACKET &Q_IDENTIFIER (&COMMA &Q_IDENTIFIER)* &CLOSE_BRACKET').compose(
    context=context
)

object_ = ANTLR4Like(identifier='OBJECT', representation='&OPEN_KEY &Q_IDENTIFIER &TWO_DOTS &IDENTIFIER &CLOSE_KEY').compose(
    context=context
)

context['VECTOR'] = vector
context['OBJECT'] = object_

t_identifier = ANTLR4Like(identifier='T_IDENTIFIER', representation='&VECTOR | &OBJECT | &IDENTIFIER').compose(
    context=context
)

context['T_IDENTIFIER'] = t_identifier

# Agora, vamos escrever os testes.

# Teste 1: Teste de parsing de VECTOR com múltiplos Q_IDENTIFIERS
def test_vector_multiple_q_identifiers():
    consumer = Consumer('[item1,item2,item3]')
    result = vector.match(consumer)
    assert result is not None
    assert consumer.position == len('[item1,item2,item3]')

# Teste 2: Teste de parsing de VECTOR com um único Q_IDENTIFIER
def test_vector_single_q_identifier():
    consumer = Consumer('[item1]')
    result = vector.match(consumer)
    assert result is not None
    assert consumer.position == len('[item1]')

# Teste 3: Teste de parsing de OBJECT com IDENTIFIER
def test_object_with_identifier():
    consumer = Consumer('{key:value}')
    result = object_.match(consumer)
    assert result is not None
    assert consumer.position == len('{key:value}')

# Teste 4: Teste de parsing de T_IDENTIFIER correspondendo a VECTOR
def test_t_identifier_matches_vector():
    consumer = Consumer('[item1,item2]')
    result = t_identifier.match(consumer)
    assert result is not None
    assert consumer.position == len('[item1,item2]')

# Teste 5: Teste de parsing de T_IDENTIFIER correspondendo a OBJECT
def test_t_identifier_matches_object():
    consumer = Consumer('{key:value}')
    result = t_identifier.match(consumer)
    assert result is not None
    assert consumer.position == len('{key:value}')

# Teste 6: Teste de parsing de T_IDENTIFIER correspondendo a IDENTIFIER
def test_t_identifier_matches_identifier():
    consumer = Consumer('identifier')
    result = t_identifier.match(consumer)
    assert result == 'identifier'
    assert consumer.position == len('identifier')

# Teste 7: Teste de falha em sintaxe inválida de VECTOR
def test_vector_invalid_syntax():
    consumer = Consumer('[item1,item2')
    result = vector.match(consumer)
    assert result is None
    assert consumer.position == 0  # Não deve consumir entrada

# Teste 8: Teste de falha em sintaxe inválida de OBJECT
def test_object_invalid_syntax():
    consumer = Consumer('{key value}')
    result = object_.match(consumer)
    assert result is None
    assert consumer.position == 0

# Teste 9: Teste de parsing de VECTOR com espaços em branco
def test_vector_with_whitespace():
    consumer = Consumer('[ item1 , item2 ]')
    # Ajustar o parser vector para lidar com espaços em branco
    vector_ws = ANTLR4Like(identifier='VECTOR_WS', representation='&OPEN_BRACKET &WHITESPACE* &Q_IDENTIFIER (&WHITESPACE* &COMMA &WHITESPACE* &Q_IDENTIFIER)* &WHITESPACE* &CLOSE_BRACKET').compose(
        context=context
    )
    result = vector_ws.match(consumer)
    assert result is not None
    assert consumer.position == len('[ item1 , item2 ]')

# Teste 10: Teste de parsing de OBJECT com espaços em branco
def test_object_with_whitespace():
    consumer = Consumer('{ key : value }')
    # Ajustar o parser object para lidar com espaços em branco
    object_ws = ANTLR4Like(identifier='OBJECT_WS', representation='&OPEN_KEY &WHITESPACE* &Q_IDENTIFIER &WHITESPACE* &TWO_DOTS &WHITESPACE* &IDENTIFIER &WHITESPACE* &CLOSE_KEY').compose(
        context=context
    )
    result = object_ws.match(consumer)
    assert result is not None
    assert consumer.position == len('{ key : value }')

# Teste 11: Teste de parsing de VECTOR com OBJECT aninhado
def test_vector_with_nested_object():
    consumer = Consumer('[{key:value},item2]')
    # Atualizar o contexto para incluir object_
    context['OBJECT'] = object_
    vector_with_object = ANTLR4Like(identifier='VECTOR_WITH_OBJECT', representation='&OPEN_BRACKET (&T_IDENTIFIER) (&COMMA &T_IDENTIFIER)* &CLOSE_BRACKET').compose(
        context=context
    )
    result = vector_with_object.match(consumer)
    assert result is not None
    assert consumer.position == len('[{key:value},item2]')

# Teste 12: Teste de parsing de OBJECT com VECTOR aninhado
def test_object_with_nested_vector():
    consumer = Consumer('{key:[item1,item2]}')
    object_with_vector = ANTLR4Like(identifier='OBJECT_WITH_VECTOR', representation='&OPEN_KEY &Q_IDENTIFIER &TWO_DOTS &T_IDENTIFIER &CLOSE_KEY').compose(
        context=context
    )
    result = object_with_vector.match(consumer)
    assert result is not None
    assert consumer.position == len('{key:[item1,item2]}')

# Teste 13: Teste de parsing com quantificador *
def test_quantifier_zero_or_more():
    consumer = Consumer('aaa')
    parser = ANTLR4Like(identifier='A_STAR', representation='( &IDENTIFIER )*').compose(
        context=context
    )
    result = parser.match(consumer)
    assert result is not None
    assert consumer.position == len('aaa')  # Deve corresponder três vezes

# Teste 14: Teste de parsing com quantificador +
def test_quantifier_one_or_more():
    consumer = Consumer('aaa')
    parser = ANTLR4Like(identifier='A_PLUS', representation='( &IDENTIFIER )+').compose(
        context=context
    )
    result = parser.match(consumer)
    assert result is not None
    assert consumer.position == len('aaa')

# Teste 15: Teste de parsing com quantificador ?
def test_quantifier_zero_or_one():
    consumer = Consumer('a')
    parser = ANTLR4Like(identifier='A_OPTIONAL', representation='( &IDENTIFIER )?').compose(
        context=context
    )
    result = parser.match(consumer)
    assert result is not None
    assert consumer.position == len('a')

# Teste 16: Teste de parsing com alternância
def test_alternation():
    consumer = Consumer('option2')
    parser = ANTLR4Like(identifier='ALTERNATION', representation='&IDENTIFIER1 | &IDENTIFIER2').compose(
        context={'IDENTIFIER1': Exactrepresentation('IDENTIFIER1', 'option1'), 'IDENTIFIER2': Exactrepresentation('IDENTIFIER2', 'option2')}
    )
    result = parser.match(consumer)
    assert result is not None
    assert consumer.position == len('option2')

# Teste 17: Teste de parsing de alternância e sequência aninhadas
def test_nested_alternation_sequence():
    consumer = Consumer('start middle end')
    parser = ANTLR4Like(identifier='NESTED', representation='&START &WHITESPACE+ ( &MIDDLE1 | &MIDDLE2 ) &WHITESPACE+ &END').compose(
        context={
            'START': Exactrepresentation('START', 'start'),
            'MIDDLE1': Exactrepresentation('MIDDLE1', 'middle'),
            'MIDDLE2': Exactrepresentation('MIDDLE2', 'center'),
            'END': Exactrepresentation('END', 'end'),
            'WHITESPACE': whitespace,
        }
    )
    result = parser.match(consumer)
    assert result is not None
    assert consumer.position == len('start middle end')

# Teste 18: Teste de parsing com agrupamento
def test_grouping():
    consumer = Consumer('abcabcabc')
    parser = ANTLR4Like(identifier='GROUPING', representation='( &IDENTIFIER ){3}').compose(
        context={'IDENTIFIER': ClassicRegex('IDENTIFIER', 'abc')}
    )
    result = parser.match(consumer)
    assert result is not None
    assert consumer.position == len('abcabcabc')

# Teste 19: Teste de falha em entrada incompatível
def test_mismatched_input():
    consumer = Consumer('start wrong end')
    parser = ANTLR4Like(identifier='SEQUENCE', representation='&START &WHITESPACE+ &MIDDLE &WHITESPACE+ &END').compose(
        context={
            'START': Exactrepresentation('START', 'start'),
            'MIDDLE': Exactrepresentation('MIDDLE', 'middle'),
            'END': Exactrepresentation('END', 'end'),
            'WHITESPACE': whitespace,
        }
    )
    result = parser.match(consumer)
    assert result is None
    assert consumer.position == 0

# Teste 20: Teste de parsing de estrutura semelhante a XML
def test_xml_like_structure():
    consumer = Consumer('<tag>content</tag>')
    open_tag = ANTLR4Like(identifier='OPEN_TAG', representation='&OPEN_ELEMENT &IDENTIFIER &CLOSE_ELEMENT').compose(
        context=context
    )
    close_tag = ANTLR4Like(identifier='CLOSE_TAG', representation='&OPEN_ELEMENT &SLASH &IDENTIFIER &CLOSE_ELEMENT').compose(
        context=context
    )
    xml_content = ClassicRegex('CONTENT', '.+').compose()
    parser = ANTLR4Like(identifier='XML', representation='&OPEN_TAG &CONTENT &CLOSE_TAG').compose(
        context={'OPEN_TAG': open_tag, 'CLOSE_TAG': close_tag, 'CONTENT': xml_content, **context}
    )
    result = parser.match(consumer)
    assert result is not None
    assert consumer.position == len('<tag>content</tag>')
