import re
from abc import ABC, abstractmethod

import re
from abc import ABC, abstractmethod

# Classe representando diferentes tipos de propagação para o contexto protótipo
class Prototype:
    ONLY_LOCAL = 1    # Propagação apenas local
    FORWARD = 2       # Propagação para a frente
    BACKWARD = 3      # Propagação para trás
    GLOBAL = 4        # Propagação global (ambos os sentidos)

# Classe que gerencia o contexto protótipo, permitindo armazenar e recuperar dados com base em regras de propagação
class PrototypeContext:
    def __init__(self, name: str):
        # Inicializa um novo contexto protótipo com um nome específico
        self.name = name
        self.data = dict()
        self.forward = None    # Contexto seguinte (para frente)
        self.backward = None   # Contexto anterior (para trás)
        pass

    def get(self, key: str, default=None, propagation=Prototype.ONLY_LOCAL):
        # Recupera um valor do contexto com base na chave e nas regras de propagação especificadas
        pass

    def set(self, key, value):
        # Define um valor no contexto atual associado a uma chave específica
        pass

    def append_child_context(self, name):
        # Cria e anexa um contexto filho ao contexto atual, estabelecendo links de propagação
        pass

# Classe que gerencia o consumo de caracteres de uma string de entrada, mantendo o rastreamento da posição e linha atual
class Consumer:
    def __init__(self, text):
        # Inicializa o consumidor com o texto de entrada e configura as posições iniciais
        self.text = text
        self.position = 0
        self.line = 1
        self.column = 1
        self.length = len(text)
        pass

    def peek(self, n=1):
        # Retorna os próximos 'n' caracteres sem avançar a posição do consumidor
        pass

    def consume(self, n=1):
        # Consome os próximos 'n' caracteres e atualiza a posição, linha e coluna do consumidor
        pass

    def get_value(self, n=1):
        # Consome e retorna os próximos 'n' caracteres
        pass

    def finished(self):
        # Verifica se todo o texto foi consumido
        pass

    def get_actual_position_consumer(self):
        # Retorna a linha e coluna atuais do consumidor
        pass

# Classe abstrata base para todos os parsers (interpretadores) no sistema
class IMicroInterpreter(ABC):
    def __init__(self, identifier, representation, *dim, **kdim):
        # Inicializa o interpretador com um identificador e uma representação (pode ser uma string ou padrão)
        self.identifier = identifier
        self.representation = representation
        self.dim = dim
        self.kdim = kdim
        self.children = []    # Lista de parsers filhos (se houver)
        self.tokens = []      # Tokens associados ao parser
        self.context = {}     # Contexto para resolução de referências
        pass

    def get_parser_sequence(self):
        # Retorna uma sequência iterável de parsers a serem usados durante a análise
        pass

    @classmethod
    def start_consume(cls, text):
        # Inicia um novo consumidor para o texto fornecido
        pass

    @classmethod
    def select_candidate(cls, parsers: list['IMicroInterpreter'], consumer, min_look_ahead=1, max_look_ahead=10):
        # Seleciona o parser candidato que corresponde ao texto atual do consumidor
        pass

    @classmethod
    def parse(cls, parser, text: str):
        # Método principal para iniciar o processo de parsing com o parser fornecido e o texto de entrada
        pass

    def compose(self, **kwargs):
        # Componha o interpretador configurando o contexto e a propagação conforme necessário
        pass

    def is_child_of(self, other):
        # Verifica se o interpretador atual é filho de outro interpretador
        pass

    @abstractmethod
    def match(self, consumer):
        # Método abstrato que tenta corresponder o texto atual do consumidor ao padrão do interpretador
        pass

# Padrões regex básicos para letras e dígitos
letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'

# Interpretador que corresponde a uma representação exata de string
class Exactrepresentation(IMicroInterpreter):
    def compose(self, **kwargs):
        # Configura o interpretador exato (neste caso, não há configurações adicionais)
        pass

    def match(self, consumer):
        # Tenta corresponder a representação exata no texto atual do consumidor
        pass

# Interpretador que utiliza expressões regulares clássicas para corresponder padrões no texto
class ClassicRegex(IMicroInterpreter):
    def compose(self, **kwargs):
        # Compila o padrão regex fornecido para uso posterior
        pass

    def match(self, consumer):
        # Tenta corresponder o padrão regex compilado no texto atual do consumidor
        pass


# Toda uma lógica abaixo para criar um interpretador bom
# ...

ANTLR4Like = IMicroInterpreter.from_new_parser(antlr4_like)

# ...


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
