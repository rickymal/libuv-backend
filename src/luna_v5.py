import re

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

class Token:
    def __init__(self, start, end, name, value='', children=None):
        self.start = start
        self.end = end
        self.name = name
        self.value = value
        self.children = children or []

    def to_yaml(self, indent=0):
        ind = '  ' * indent
        yaml_str = f"{ind}- name: {self.name}\n"
        yaml_str += f"{ind}  start: {self.start}\n"
        yaml_str += f"{ind}  end: {self.end}\n"
        yaml_str += f"{ind}  value: \"{self.value}\"\n"
        if self.children:
            yaml_str += f"{ind}  children:\n"
            for child in self.children:
                yaml_str += child.to_yaml(indent + 1)
        return yaml_str

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return (self.name == other.name and
                self.start == other.start and
                self.end == other.end and
                self.value == other.value and
                self.children == other.children)

    def __repr__(self):
        return (f"Token(name={self.name}, start={self.start}, end={self.end}, "
                f"value={self.value}, children={self.children})")

class Finder:
    def __init__(self, on_find_token=None, pattern='', name=''):
        self.on_find_token = on_find_token or []
        self.pattern = pattern
        self.name = name

    def scan(self, text, context, pos=0):
        pass

class LiteralFinder(Finder):
    def __init__(self, on_find_token=None, pattern='', name=''):
        super().__init__(on_find_token, pattern, name)

    def scan(self, text, context, pos=0):
        if text.startswith(self.pattern, pos):
            start_pos = pos
            end_pos = pos + len(self.pattern)
            token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=self.pattern)
            for func in self.on_find_token:
                func(token, context)
            return token, end_pos
        else:
            return None, pos

class RegexFinder(Finder):
    def __init__(self, on_find_token=None, pattern='', name=''):
        super().__init__(on_find_token, pattern, name)
        self.regex = re.compile(pattern)

    def scan(self, text, context, pos=0):
        m = self.regex.match(text, pos)
        if m:
            start_pos = pos
            end_pos = m.end()
            value = m.group()
            token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=value)
            for func in self.on_find_token:
                func(token, context)
            return token, end_pos
        else:
            return None, pos

class PatternParser:
    """
    Parser para analisar a string de padrão e construir a árvore de Finders.
    """
    TOKEN_REGEX = re.compile(r"\s*(?:(\()|(\))|(\|)|(&\w+)|(\*)|(\?)|(\+)|('([^']*)')|(\S+))")
    # Adicionamos ('([^']*)') para capturar literais entre aspas simples.

    def __init__(self, pattern, context):
        self.pattern = pattern
        self.context = context
        self.tokens = []
        self.pos = 0
        self.current_token = None

    def parse(self):
        self.tokenize()
        self.next_token()
        return self.expression()

    def tokenize(self):
        pos = 0
        while pos < len(self.pattern):
            m = self.TOKEN_REGEX.match(self.pattern, pos)
            if not m:
                raise SyntaxError(f"Unexpected character at position {pos}")
            pos = m.end()
            token = None
            for group_num in range(1, m.lastindex + 1):
                token = m.group(group_num)
                if token is not None:
                    token = token.strip()
                    if token:
                        self.tokens.append(token)
                    break

    def next_token(self):
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            self.pos += 1
        else:
            self.current_token = None

    def expression(self):
        term = self.term()
        if self.current_token == '|':
            finders = [term]
            while self.current_token == '|':
                self.next_token()
                finders.append(self.term())
            return AlternationFinder(finders, name='alternation')
        else:
            return term

    def term(self):
        factors = []
        while self.current_token and self.current_token not in {')', '|'}:
            factor = self.factor()
            factors.append(factor)
        if len(factors) == 1:
            return factors[0]
        else:
            return SequenceFinder(factors, name='sequence')

    def factor(self):
        base = self.base()
        while self.current_token in {'*', '+', '?'}:
            quantifier = self.current_token
            self.next_token()
            base = QuantifierFinder(base, quantifier, name='quantifier')
        return base

    def base(self):
        if self.current_token == '(':
            self.next_token()
            expr = self.expression()
            if self.current_token != ')':
                raise SyntaxError("Expected ')'")
            self.next_token()
            return expr
        elif self.current_token.startswith('&'):
            token_name = self.current_token[1:]
            self.next_token()
            parser = self.context.get(f"PS:{token_name}", None)
            if parser is None:
                raise ValueError(f"Parser {token_name} not found in context")
            return parser
        else:
            # Trata literais
            literal = self.current_token
            self.next_token()
            # Remover aspas simples se existirem
            if literal.startswith("'") and literal.endswith("'"):
                literal = literal[1:-1]
            return LiteralFinder(pattern=literal, name='literal')

class QuantifierFinder(Finder):
    def __init__(self, finder, quantifier, name=''):
        super().__init__(name=name)
        self.finder = finder
        self.quantifier = quantifier  # '*', '+', '?'

    def scan(self, text, context, pos=0):
        start_pos = pos
        children = []
        if self.quantifier == '*':
            while True:
                token, new_pos = self.finder.scan(text, context, pos)
                if token is not None:
                    children.append(token)
                    pos = new_pos
                else:
                    break
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            return token, pos
        elif self.quantifier == '+':
            token, pos = self.finder.scan(text, context, pos)
            if token is None:
                return None, start_pos
            children.append(token)
            while True:
                token, new_pos = self.finder.scan(text, context, pos)
                if token is not None:
                    children.append(token)
                    pos = new_pos
                else:
                    break
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            return token, pos
        elif self.quantifier == '?':
            token, new_pos = self.finder.scan(text, context, pos)
            if token is not None:
                children.append(token)
                pos = new_pos
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            return token, pos
        else:
            raise ValueError(f"Unknown quantifier: {self.quantifier}")

class AlternationFinder(Finder):
    def __init__(self, finders, name=''):
        super().__init__(name=name)
        self.finders = finders

    def scan(self, text, context, pos=0):
        for finder in self.finders:
            token, new_pos = finder.scan(text, context, pos)
            if token is not None:
                return token, new_pos
        return None, pos

class SequenceFinder(Finder):
    def __init__(self, finders, name=''):
        super().__init__(name=name)
        self.finders = finders

    def scan(self, text, context, pos=0):
        start_pos = pos
        children = []
        for finder in self.finders:
            token, pos = finder.scan(text, context, pos)
            if token is None:
                return None, start_pos
            children.append(token)
        end_pos = pos
        value = ''.join(child.value for child in children)
        token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=value, children=children)
        return token, pos

def tag_values(token, context):
    pass  # Implementação opcional

def extract(token, context):
    context.set('token', token)

def extract_tree(context):
    return context.get('token')

# Definição dos parsers básicos
ctx_root = PrototypeContext(name='root')

# Parsers literais
open_bracket = LiteralFinder(pattern='<', name='open_bracket')
close_bracket = LiteralFinder(pattern='>', name='close_bracket')
slash = LiteralFinder(pattern='/', name='slash')

ctx_root.set("PS:OPEN_BRACKET", open_bracket)
ctx_root.set("PS:CLOSE_BRACKET", close_bracket)
ctx_root.set("PS:SLASH", slash)

# Parser para 'b_identifier'
letter_pattern = '[a-zA-Z_À-ÿ]'
digit_pattern = '[0-9]'
letter_or_digit = f'(?:{letter_pattern}|{digit_pattern})'
b_identifier_pattern = f'{letter_pattern}{letter_or_digit}*(?:\\.{letter_pattern}{letter_or_digit}*)*'
b_identifier = RegexFinder(on_find_token=[], pattern=b_identifier_pattern, name='b_identifier')
ctx_root.set("PS:B_IDENTIFIER", b_identifier)

# Parser para 'TEXT'
text_pattern = '[^<>]+'
text_finder = RegexFinder(pattern=text_pattern, name='text')
ctx_root.set("PS:TEXT", text_finder)

# Parsers para tags específicas
# OPEN_B_TAG: <b>
open_b_tag_pattern = "&OPEN_BRACKET 'b' &CLOSE_BRACKET"
open_b_tag_parser = PatternParser(open_b_tag_pattern, ctx_root)
open_b_tag = open_b_tag_parser.parse()
open_b_tag.name = 'open_b_tag'
ctx_root.set("PS:OPEN_B_TAG", open_b_tag)

# CLOSE_B_TAG: </b>
close_b_tag_pattern = "&OPEN_BRACKET &SLASH 'b' &CLOSE_BRACKET"
close_b_tag_parser = PatternParser(close_b_tag_pattern, ctx_root)
close_b_tag = close_b_tag_parser.parse()
close_b_tag.name = 'close_b_tag'
ctx_root.set("PS:CLOSE_B_TAG", close_b_tag)

# OPEN_I_TAG: <i>
open_i_tag_pattern = "&OPEN_BRACKET 'i' &CLOSE_BRACKET"
open_i_tag_parser = PatternParser(open_i_tag_pattern, ctx_root)
open_i_tag = open_i_tag_parser.parse()
open_i_tag.name = 'open_i_tag'
ctx_root.set("PS:OPEN_I_TAG", open_i_tag)

# CLOSE_I_TAG: </i>
close_i_tag_pattern = "&OPEN_BRACKET &SLASH 'i' &CLOSE_BRACKET"
close_i_tag_parser = PatternParser(close_i_tag_pattern, ctx_root)
close_i_tag = close_i_tag_parser.parse()
close_i_tag.name = 'close_i_tag'
ctx_root.set("PS:CLOSE_I_TAG", close_i_tag)

# BOLD_TAG: <b>TEXT</b>
bold_tag_pattern = "&OPEN_B_TAG &TEXT &CLOSE_B_TAG"
bold_tag_parser = PatternParser(bold_tag_pattern, ctx_root)
bold_tag = bold_tag_parser.parse()
bold_tag.name = 'bold_tag'
ctx_root.set("PS:BOLD_TAG", bold_tag)

# ITALIC_TAG: <i>TEXT</i>
italic_tag_pattern = "&OPEN_I_TAG &TEXT &CLOSE_I_TAG"
italic_tag_parser = PatternParser(italic_tag_pattern, ctx_root)
italic_tag = italic_tag_parser.parse()
italic_tag.name = 'italic_tag'
ctx_root.set("PS:ITALIC_TAG", italic_tag)

# ELEMENT: BOLD_TAG | ITALIC_TAG | TEXT
element_pattern = "&BOLD_TAG | &ITALIC_TAG | &TEXT"
element_parser = PatternParser(element_pattern, ctx_root)
element = element_parser.parse()
element.name = 'element'
ctx_root.set("PS:ELEMENT", element)

# OPEN_TAG e CLOSE_TAG para 'code'
open_tag_pattern = "&OPEN_BRACKET 'code' &CLOSE_BRACKET"
open_tag_parser = PatternParser(open_tag_pattern, ctx_root)
open_tag = open_tag_parser.parse()
open_tag.name = 'open_tag'
ctx_root.set("PS:OPEN_TAG", open_tag)

close_tag_pattern = "&OPEN_BRACKET &SLASH 'code' &CLOSE_BRACKET"
close_tag_parser = PatternParser(close_tag_pattern, ctx_root)
close_tag = close_tag_parser.parse()
close_tag.name = 'close_tag'
ctx_root.set("PS:CLOSE_TAG", close_tag)

# Definição do parser 'root' com quantificadores e alternação
root_pattern = "&OPEN_TAG (&ELEMENT)* &CLOSE_TAG"
root_parser = PatternParser(root_pattern, ctx_root)
root = root_parser.parse()
root.name = 'root'
root.on_find_token = [extract]

# Atualizando o texto
text = "<code><b>Wolfram.math</b><i>Mathematica</i></code>"

# Scan do texto
result_token, pos = root.scan(text, context=ctx_root, pos=0)

# Token esperado (pode ser ajustado conforme necessário)
expected_result = Token(start=1, end=len(text), name='root', value=text, children=[
    # Tokens filhos aqui...
])

# Verifica se o resultado é igual ao esperado (se você tiver definido 'expected_result')
# assert result_token == expected_result

print("Parsing bem-sucedido. O token resultante é:")
print(result_token.to_yaml(indent=0))
