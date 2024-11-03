import sys
import os 
# Calcular o caminho absoluto para o diretório raiz
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adicionar o diretório raiz ao sys.path
sys.path.insert(0, ROOT_DIR)


import pytest
from lib.finders import (
    Prototype,
    PrototypeContext,
    Token,
    LiteralFinder,
    RegexFinder,
    ForwardFinder,
    PatternParser,
    QuantifierFinder,
    AlternationFinder,
    SequenceFinder,
    ListParser,
    ObjectParser,
    extract,
    extract_tree
)

def test_prototype_context():
    context = PrototypeContext('root')
    context.set('key1', 'value1')
    assert context.get('key1') == 'value1'
    assert context.get('key2', default='default') == 'default'

    child_context = context.append_child_context('child')
    child_context.set('key2', 'value2')
    assert child_context.get('key1', propagation=Prototype.BACKWARD) == 'value1'
    assert context.get('key2', propagation=Prototype.FORWARD) == 'value2'

def test_token():
    token = Token(1, 5, 'test', 'value')
    expected_yaml = '''- name: test
  start: 1
  end: 5
  value: "value"
'''
    assert token.to_yaml() == expected_yaml

def test_literal_finder():
    finder = LiteralFinder(pattern='hello', name='greeting')
    context = PrototypeContext('test')
    text = 'hello world'
    token, pos = finder.scan(text, context)
    assert token.value == 'hello'
    assert pos == 5

def test_regex_finder():
    finder = RegexFinder(pattern=r'\d+', name='number')
    context = PrototypeContext('test')
    text = '123 abc'
    token, pos = finder.scan(text, context)
    assert token.value == '123'
    assert pos == 3

def test_forward_finder():
    target_finder = LiteralFinder(pattern='world', name='planet')
    forward_finder = ForwardFinder(name='forward')
    forward_finder.set_target(target_finder)
    context = PrototypeContext('test')
    text = 'world'
    token, pos = forward_finder.scan(text, context)
    assert token.value == 'world'
    assert pos == 5

def test_pattern_parser_literal():
    context = PrototypeContext('test')
    parser = PatternParser("'hello'", context)
    finder = parser.parse()
    text = 'hello world'
    token, pos = finder.scan(text, context)
    assert token.value == 'hello'
    assert pos == 5

def test_pattern_parser_sequence():
    context = PrototypeContext('test')
    parser = PatternParser("'hello' 'world'", context)
    finder = parser.parse()
    text = 'hello world!'
    token, pos = finder.scan(text, context)
    assert token.value == 'helloworld'
    assert pos == 11

def test_pattern_parser_alternation():
    context = PrototypeContext('test')
    parser = PatternParser("'yes'|'no'", context)
    finder = parser.parse()
    text = 'nope'
    token, pos = finder.scan(text, context)
    
    assert token == Token(name = 'literal', start =1, end = 2, value = 'no', children=[])

    text = 'yes, I agree'
    token, pos = finder.scan(text, context)
    assert token.value == 'yes'
    assert pos == 3

def test_quantifier_finder():
    context = PrototypeContext('test')
    literal_finder = LiteralFinder(pattern='ha', name='laugh')
    quantifier_finder = QuantifierFinder(literal_finder, '+')
    text = 'hahaha!'
    token, pos = quantifier_finder.scan(text, context)
    assert token.value == 'hahaha'
    assert pos == 6

def test_sequence_finder():
    finder1 = LiteralFinder(pattern='foo', name='foo')
    finder2 = LiteralFinder(pattern='bar', name='bar')
    sequence_finder = SequenceFinder([finder1, finder2], name='foobar')
    context = PrototypeContext('test')
    text = 'foobar'
    token, pos = sequence_finder.scan(text, context)
    assert token.value == 'foobar'
    assert pos == 6

def test_alternation_finder():
    finder1 = LiteralFinder(pattern='foo', name='foo')
    finder2 = LiteralFinder(pattern='bar', name='bar')
    alternation_finder = AlternationFinder([finder1, finder2], name='foo_or_bar')
    context = PrototypeContext('test')
    text = 'barbaz'
    token, pos = alternation_finder.scan(text, context)
    assert token.value == 'bar'
    assert pos == 3

def test_list_parser_empty():
    context = PrototypeContext('test')
    context.set('PS:VALUE', LiteralFinder(pattern='value', name='value'))
    list_parser = ListParser()
    text = '[]'
    token, pos = list_parser.scan(text, context)
    assert token.value == '[]'
    assert pos == 2
    assert len(token.children) == 0

def test_list_parser():
    context = PrototypeContext('test')
    context.set('PS:VALUE', LiteralFinder(pattern='value', name='value'))
    list_parser = ListParser()
    text = '[value, value]'
    token, pos = list_parser.scan(text, context)
    assert token.value == '[value, value]'
    assert pos == 14
    assert len(token.children) == 2

def test_object_parser_empty():
    context = PrototypeContext('test')
    context.set('PS:ATTRIBUTE', LiteralFinder(pattern='attr', name='attribute'))
    object_parser = ObjectParser()
    text = '{}'
    token, pos = object_parser.scan(text, context)
    assert token.value == '{}'
    assert pos == 2
    assert len(token.children) == 0

def test_object_parser():
    context = PrototypeContext('test')
    context.set('PS:ATTRIBUTE', LiteralFinder(pattern='attr', name='attribute'))
    object_parser = ObjectParser()
    text = '{attr, attr}'
    token, pos = object_parser.scan(text, context)
    assert token.value == '{attr, attr}'
    assert pos == 12
    assert len(token.children) == 2

def test_extract_and_extract_tree():
    context = PrototypeContext('test')
    token = Token(1, 5, 'test', 'value')
    extract(token, context)
    retrieved_token = extract_tree(context)
    assert retrieved_token == token


if __name__ == "__main__":
    test_object_parser()