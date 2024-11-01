# Padrões básicos
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

    #[TODO] terminar implementação, a partir
    def get(key: str, default = None, propagation = Prototype.ONLY_LOCAL):
        if propagation == Prototype.ONLY_LOCAL:
            return self.data.get(key, default)
        elif propagation == Prototype.FORWARD:
            value = self.data.get(key, None)
            if value is None:
                return self.forward.get(key, default, propagation)
            return value
        else:
            #[TODO] Implementar as outras opções
            pass
        

    #[TODO]
    def set(key, *args, **kwargs):
        pass

#[TODO]
class Consumer:
    pass


class IMicroInterpreter:
    pass

letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'

# Base Parser Transformer Interface
class IMicroInterpreter(ABC):

    # [TODO] Pensar em como usar dim e kdim, a ideia é que eles representem dimensões
    # Como se fosse outra dimensão do interpretador por exemplo
    # Eu quero colocar comentários do código em uma dimensão separada
    # Para que futuramente eu os use para uma segunda etapa de parsing para documentação por exemplo
    def __init__(self, identifier, representation, *dim, **kdim):
        self.identifier = identifier
        self.representation = representation
        self.dim = dim
        self.kdim = kdim
        self.children = []
        self.tokens = []


    # [TODO] analisar a arvore criada e retornar um vetor de arrays de parser, o vetor representa a ordem de parsers a serem usadas
    # e o arrays entrega as opções possíveis de parserm a serem utilizadas
    def get_parser_sequence(self) -> list[IMicroInterpreter]:
        pass

    # [TODO] retorna um objeto para auxiliar no consumo, controla todo o acesso do que é lido ou não.
    @classmethod
    def start_consume(cls):
        pass


    @classmethod
    def parse(cls, parser, path: str):
        
        
        sequence_parser: iter[IMicroInterpreter] = parser.get_parser_sequence()

        vector_history = []
        prototype_context = PrototypeContext(name="root")
        main_context = prototype_context
        consumer = cls.start_consume(path)
        previous_parser = None
        actual_parser: list[IMicroInterpreter] = next(sequence_parser)        
        while not consumer.finished():
            ln_begin, cl_begin = consumer.get_actual_position_consumer()
            parser_choosed: IMicroInterpreter = cls.select_candidate(actual_parser, consumer, min_look_ahead = 1, max_look_ahead = 10,)
            value = consumer.get_value()
            ln_end, cl_end = consumer.get_actual_position_consumer()
            actual_parser.set(parser_choosed.name, ln_begin, cl_begin, ln_end, cl_end, value)

            previous_parser = actual_parser
            actual_parser = next(sequence_parser)

            if actual_parser.is_child_of(previous_parser):
                prototype_context = prototype_context.append_child_context()



    
    def compose(self, context: list[IMicroInterpreter]):
        
        pass
    
    @abstractmethod
    def match(self, text):
        pass


# Exact representation Matcher
class Exactrepresentation(IMicroInterpreter):
    def compose(self, **kwargs):
        return self
    
    def match(self, text):
        if text.startswith(self.representation):
            return self.representation, text[len(self.representation):]
        return None, text

# Regular Expression Matcher
class ClassicRegex(IMicroInterpreter):
    def compose(self, **kwargs):
        self.pattern = re.compile(self.representation)
        return self
    
    def match(self, text):
        match = self.pattern.match(text)
        if match:
            return match.group(), text[match.end():]
        return None, text

# ANTLR4-Like Grammar Parser
class ANTLR4Like(IMicroInterpreter):
    def compose(self, **kwargs):
        self.children = kwargs.get('representations', [])
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
    Exactrepresentation(identifier='OPEN_ELEMENT', representation='<'),
    Exactrepresentation(identifier='CLOSE_ELEMENT', representation='>'),
    ClassicRegex(identifier='DIGIT', representation=digit_pattern),
    ClassicRegex(identifier='IDENTIFIER', representation=f'{letter_pattern}{letter_or_digit}*'),
    ClassicRegex(identifier='Q_IDENTIFIER', representation=f'{letter_pattern}{letter_or_digit}*(?:\\.{letter_pattern}{letter_or_digit}*)*'),
    Exactrepresentation(identifier='EQUALS', representation='='),
    Exactrepresentation(identifier='OPEN_BRACKET', representation='['),
    Exactrepresentation(identifier='CLOSE_BRACKET', representation=']'),
    Exactrepresentation(identifier='SLASH', representation='/'),
    Exactrepresentation(identifier='OPEN_KEY', representation='{'),
    Exactrepresentation(identifier='CLOSE_KEY', representation='}'),
    Exactrepresentation(identifier='TWO_DOTS', representation=':'),
    Exactrepresentation(identifier='COMMA', representation=','),
]

# Grammar Definitions
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
comment = ClassicRegex(identifier='COMMENT', representation=f'\# .* [\r\n]', channel = 'hidden').compose() # [TODO] Corrigir a regex, o mode é para jogar para uma 'dimensão chamado 'mode comment', só parser nessa dimensão conseguirão ler
no_representation_tokens_complete = ClassicRegex(identifier='NO_representation_TOKEN', representation=f'[\r\n\t ]', channel = 'hidden').compose() # [TODO] Corrigir a regex, o mode é para jogar para uma 'dimensão chamado 'mode comment', só parser nessa dimensão conseguirão ler
no_representation_tokens_without_space = ClassicRegex(identifier='NO_representation_TOKEN', representation=f'[\r\n\t]', channel = 'hidden').compose() # [TODO] Corrigir a regex, o mode é para jogar para uma 'dimensão chamado 'mode comment', só parser nessa dimensão conseguirão ler



# Define t_identifier first to use in xml_attribute
def get_t_identifier():
    return ANTLR4Like(identifier='T_IDENTIFIER', representation='&VECTOR | &OBJECT | &PROGRAM').compose(
        representations=[
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
# VECTOR Rule
vector = ANTLR4Like(identifier='VECTOR', representation='&OPEN_BRACKET &Q_IDENTIFIER (&COMMA &Q_IDENTIFIER)* &CLOSE_BRACKET').compose(
    context=[
        open_bracket,
        q_identifier,
        ANTLR4Like(identifier='Q_IDENTIFIER_LIST', representation='(&COMMA &Q_IDENTIFIER)*').compose(
            context=[
                ANTLR4Like(identifier='Q_IDENTIFIER_ITEM', representation='&COMMA &Q_IDENTIFIER').compose(
                    context=[comma, q_identifier]
                )
            ]
        ),
        close_bracket
    ]
)

# OBJECT Rule
object_ = ANTLR4Like(identifier='OBJECT', representation='&OPEN_KEY &Q_IDENTIFIER &TWO_DOTS &PROGRAM &CLOSE_KEY').compose(
    context=[
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
xml_attribute = ANTLR4Like(identifier='XML_ATTRIBUTE', representation='&Q_IDENTIFIER &EQUALS &T_IDENTIFIER').compose(
    context=[q_identifier, equals, t_identifier]
)

# OPEN_TAG Rule
open_tag = ANTLR4Like(identifier='OPEN_TAG', representation='&OPEN_ELEMENT &Q_IDENTIFIER &XML_ATTRIBUTE* &CLOSE_ELEMENT').compose(
    context=[
        open_element,
        q_identifier,
        ANTLR4Like(identifier='XML_ATTRIBUTE_LIST', representation='&XML_ATTRIBUTE*').compose(
            context=[xml_attribute]
        ),
        close_element
    ]
)

# CLOSE_TAG Rule
close_tag = ANTLR4Like(identifier='CLOSE_TAG', representation='&OPEN_ELEMENT &SLASH &Q_IDENTIFIER &CLOSE_ELEMENT').compose(
    context=[open_element, slash, q_identifier, close_element]
)

# XML_STATEMENT Rule
xml_statement = ANTLR4Like(identifier='XML_STATEMENT', representation='&OPEN_TAG &PROGRAM &CLOSE_TAG').compose(
    context = [open_tag, program, close_tag, no_representation_tokens_without_space])

# IMPORT_STATEMENT Rule
import_statement = ANTLR4Like(identifier='IMPORT_STATEMENT', representation='&REQUIRE &IDENTIFIER').compose(
    context=[require, identifier]
)

# PROGRAM Rule
program = ANTLR4Like(identifier='PROGRAM', representation='(&XML_STATEMENT | &IMPORT_STATEMENT)*').compose(
    context = [xml_statement, import_statement, comment, no_representation_tokens_complete]
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
parsed_output = program.parse(code)
print(parsed_output)
