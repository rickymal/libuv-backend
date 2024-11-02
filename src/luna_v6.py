import re
import logging

# Configurar o logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

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
        value = None
        if propagation == Prototype.ONLY_LOCAL:
            value = self.data.get(key, default)
        elif propagation == Prototype.FORWARD:
            value = self.data.get(key, None)
            if value is None and self.forward:
                return self.forward.get(key, default, propagation)
            value = value if value is not None else default
        elif propagation == Prototype.BACKWARD:
            value = self.data.get(key, None)
            if value is None and self.backward:
                return self.backward.get(key, default, propagation)
            value = value if value is not None else default
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
            value = default
        else:
            value = default

        logging.debug(f"Context get: key={key}, value={value}, context={self.name}")
        return value

    def set(self, key, value):
        logging.debug(f"Context set: key={key}, value={value}, context={self.name}")
        self.data[key] = value

    def append_child_context(self, name):
        child_context = PrototypeContext(name)
        child_context.backward = self
        self.forward = child_context
        logging.debug(f"Context append_child: parent={self.name}, child={child_context.name}")
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
        yaml_str += f"{ind}  value: \"{self.value.strip()}\"\n"
        if self.children:
            yaml_str += f"{ind}  children:\n"
            for child in self.children:
                yaml_str += child.to_yaml(indent + 1)
        return yaml_str

    def to_mermaid(self, parent_id=None, node_id=0):
        lines = []
        current_id = node_id
        label = f"{self.name}: {self.value.strip().replace('\"', '\\\"')}"
        label = label.replace('\n', '\\n')  # Escapar quebras de linha
        lines.append(f'id{current_id}["{label}"]')
        if parent_id is not None:
            lines.append(f'id{parent_id} --> id{current_id}')
        next_id = current_id + 1
        for child in self.children:
            child_lines, next_id = child.to_mermaid(parent_id=current_id, node_id=next_id)
            lines.extend(child_lines)
        return lines, next_id

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
        logging.debug(f"LiteralFinder scanning for '{self.pattern}' at position {pos}")
        if text.startswith(self.pattern, pos):
            start_pos = pos
            end_pos = pos + len(self.pattern)
            token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=self.pattern)
            for func in self.on_find_token:
                func(token, context)
            logging.debug(f"LiteralFinder found '{self.pattern}' from {start_pos} to {end_pos}")
            return token, end_pos
        else:
            logging.debug(f"LiteralFinder did not find '{self.pattern}' at position {pos}")
            return None, pos

class RegexFinder(Finder):
    def __init__(self, on_find_token=None, pattern='', name=''):
        super().__init__(on_find_token, pattern, name)
        self.regex = re.compile(pattern, re.DOTALL)

    def scan(self, text, context, pos=0):
        logging.debug(f"RegexFinder scanning with pattern '{self.pattern}' at position {pos}")
        m = self.regex.match(text, pos)
        if m:
            start_pos = pos
            end_pos = m.end()
            value = m.group()
            token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=value)
            for func in self.on_find_token:
                func(token, context)
            logging.debug(f"RegexFinder found '{value}' from {start_pos} to {end_pos}")
            return token, end_pos
        else:
            logging.debug(f"RegexFinder did not match at position {pos}")
            return None, pos

class ForwardFinder(Finder):
    def __init__(self, name=''):
        super().__init__(name=name)
        self.target = None

    def set_target(self, target):
        self.target = target
        logging.debug(f"ForwardFinder '{self.name}' target set to '{target.name}'")

    def scan(self, text, context, pos=0):
        if self.target is None:
            raise ValueError(f"ForwardFinder target not set for {self.name}")
        logging.debug(f"ForwardFinder '{self.name}' delegates to '{self.target.name}' at position {pos}")
        return self.target.scan(text, context, pos)

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
        logging.debug(f"PatternParser parsing pattern: {self.pattern}")
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
                        logging.debug(f"Tokenized: '{token}'")
                    break

    def next_token(self):
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            self.pos += 1
            logging.debug(f"Next token: '{self.current_token}'")
        else:
            self.current_token = None
            logging.debug("No more tokens")

    def expression(self):
        term = self.term()
        if self.current_token == '|':
            finders = [term]
            while self.current_token == '|':
                self.next_token()
                finders.append(self.term())
            logging.debug(f"Created AlternationFinder with {len(finders)} options")
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
            logging.debug(f"Created SequenceFinder with {len(factors)} factors")
            return SequenceFinder(factors, name='sequence')

    def factor(self):
        base = self.base()
        while self.current_token in {'*', '+', '?'}:
            quantifier = self.current_token
            self.next_token()
            base = QuantifierFinder(base, quantifier, name='quantifier')
            logging.debug(f"Applied quantifier '{quantifier}'")
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
            logging.debug(f"Referenced parser: '{token_name}'")
            return parser
        else:
            # Trata literais
            literal = self.current_token
            self.next_token()
            # Remover aspas simples se existirem
            if literal.startswith("'") and literal.endswith("'"):
                literal = literal[1:-1]
            logging.debug(f"Created LiteralFinder for '{literal}'")
            return LiteralFinder(pattern=literal, name='literal')

class QuantifierFinder(Finder):
    def __init__(self, finder, quantifier, name=''):
        super().__init__(name=name)
        self.finder = finder
        self.quantifier = quantifier  # '*', '+', '?'

    def scan(self, text, context, pos=0):
        logging.debug(f"QuantifierFinder '{self.quantifier}' scanning at position {pos}")
        start_pos = pos
        children = []
        if self.quantifier == '*':
            while True:
                token, new_pos = self.finder.scan(text, context, pos)
                if token is not None and new_pos > pos:
                    children.append(token)
                    pos = new_pos
                else:
                    break
            # Sempre retornar um token, mesmo se nenhuma ocorrência for encontrada
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            logging.debug(f"QuantifierFinder '*' matched {len(children)} times from {start_pos} to {pos}")
            return token, pos
        elif self.quantifier == '+':
            token, pos = self.finder.scan(text, context, pos)
            if token is None:
                logging.debug(f"QuantifierFinder '+' failed to match at position {pos}")
                return None, start_pos
            children.append(token)
            while True:
                token, new_pos = self.finder.scan(text, context, pos)
                if token is not None and new_pos > pos:
                    children.append(token)
                    pos = new_pos
                else:
                    break
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            logging.debug(f"QuantifierFinder '+' matched {len(children)} times from {start_pos} to {pos}")
            return token, pos
        elif self.quantifier == '?':
            token, new_pos = self.finder.scan(text, context, pos)
            if token is not None and new_pos > pos:
                children.append(token)
                pos = new_pos
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            logging.debug(f"QuantifierFinder '?' matched {len(children)} times from {start_pos} to {pos}")
            return token, pos
        else:
            raise ValueError(f"Unknown quantifier: {self.quantifier}")


class AlternationFinder(Finder):
    def __init__(self, finders, name=''):
        super().__init__(name=name)
        self.finders = finders

    def scan(self, text, context, pos=0):
        logging.debug(f"AlternationFinder scanning at position {pos}")
        for finder in self.finders:
            token, new_pos = finder.scan(text, context, pos)
            if token is not None:
                logging.debug(f"AlternationFinder matched '{finder.name}' at position {pos}")
                return token, new_pos
        logging.debug("AlternationFinder did not match any option")
        return None, pos

class SequenceFinder(Finder):
    def __init__(self, finders, name=''):
        super().__init__(name=name)
        self.finders = finders

    def scan(self, text, context, pos=0):
        logging.debug(f"SequenceFinder scanning at position {pos}")
        start_pos = pos
        children = []
        for finder in self.finders:
            # Skip whitespace before each token
            while pos < len(text) and text[pos].isspace():
                pos +=1
            token, pos = finder.scan(text, context, pos)
            if token is None:
                logging.debug(f"SequenceFinder failed at '{finder.name}' starting at position {pos}")
                return None, start_pos
            children.append(token)
        end_pos = pos
        value = ''.join(child.value for child in children)
        token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=value, children=children)
        return token, pos


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
equal_sign = LiteralFinder(pattern='=', name='equal_sign')

ctx_root.set("PS:OPEN_BRACKET", open_bracket)
ctx_root.set("PS:CLOSE_BRACKET", close_bracket)
ctx_root.set("PS:SLASH", slash)
ctx_root.set("PS:EQUAL_SIGN", equal_sign)

# Parsers para identificadores e valores
identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_\.]*'
identifier_finder = RegexFinder(pattern=identifier_pattern, name='identifier')
ctx_root.set("PS:IDENTIFIER", identifier_finder)

# Parser para strings entre aspas duplas
string_pattern = r'"(?:\\.|[^"\\])*"'
string_finder = RegexFinder(pattern=string_pattern, name='string')
ctx_root.set("PS:STRING", string_finder)

# Implementação recursiva para listas e objetos
class ListParser(Finder):
    def __init__(self, name='list'):
        super().__init__(name=name)

    def scan(self, text, context, pos=0):
        logging.debug(f"ListParser scanning at position {pos}")
        if pos >= len(text) or text[pos] != '[':
            return None, pos
        start_pos = pos
        pos += 1  # Skip '['
        children = []
        while pos < len(text):
            # Skip whitespace
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Check for closing ']'
            if pos < len(text) and text[pos] == ']':
                pos += 1  # Skip ']'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ListParser found empty list at positions {start_pos}-{pos}")
                return token, pos
            # Try to parse a value
            value_parser = context.get('PS:VALUE')
            token, pos = value_parser.scan(text, context, pos)
            if token is None:
                logging.debug(f"ListParser failed to parse value at position {pos}")
                return None, start_pos
            children.append(token)
            # Skip whitespace
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Check for ',' or ']'
            if pos < len(text) and text[pos] == ',':
                pos += 1  # Skip ','
            elif pos < len(text) and text[pos] == ']':
                pos += 1  # Skip ']'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ListParser parsed list from positions {start_pos}-{pos}")
                return token, pos
            else:
                logging.debug(f"ListParser expected ',' or ']' at position {pos}")
                return None, start_pos
        logging.debug("ListParser reached end of text without closing ']'")
        return None, start_pos

class ObjectParser(Finder):
    def __init__(self, name='object'):
        super().__init__(name=name)

    def scan(self, text, context, pos=0):
        logging.debug(f"ObjectParser scanning at position {pos}")
        if pos >= len(text) or text[pos] != '{':
            return None, pos
        start_pos = pos
        pos += 1  # Skip '{'
        children = []
        while pos < len(text):
            # Skip whitespace
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Check for closing '}'
            if pos < len(text) and text[pos] == '}':
                pos += 1  # Skip '}'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ObjectParser found empty object at positions {start_pos}-{pos}")
                return token, pos
            # Try to parse an attribute
            attribute_parser = context.get('PS:ATTRIBUTE')
            token, pos = attribute_parser.scan(text, context, pos)
            if token is None:
                logging.debug(f"ObjectParser failed to parse attribute at position {pos}")
                return None, start_pos
            children.append(token)
            # Skip whitespace
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Check for ',' or '}'
            if pos < len(text) and text[pos] == ',':
                pos += 1  # Skip ','
            elif pos < len(text) and text[pos] == '}':
                pos += 1  # Skip '}'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ObjectParser parsed object from positions {start_pos}-{pos}")
                return token, pos
            else:
                logging.debug(f"ObjectParser expected ',' or '}}' at position {pos}")
                return None, start_pos
        logging.debug("ObjectParser reached end of text without closing '}'")
        return None, start_pos


list_parser = ListParser()
ctx_root.set("PS:LIST", list_parser)

object_parser = ObjectParser()
ctx_root.set("PS:OBJECT", object_parser)

# Criar o ForwardFinder para TAG
tag_placeholder = ForwardFinder(name='tag')
ctx_root.set("PS:TAG", tag_placeholder)

# Parser para valores (pode ser um identificador, string, lista, objeto ou tag)
value_pattern = "&STRING | &LIST | &OBJECT | &IDENTIFIER | &TAG"
value_parser = PatternParser(value_pattern, ctx_root)
value = value_parser.parse()
value.name = 'value'
ctx_root.set("PS:VALUE", value)




# Definir o LiteralFinder para ':'
colon = LiteralFinder(pattern=':', name='colon')
ctx_root.set("PS:COLON", colon)

# Parser para atributo que aceita '=' ou ':'
attribute_pattern = "&IDENTIFIER (&EQUAL_SIGN | &COLON) &VALUE"
attribute_parser = PatternParser(attribute_pattern, ctx_root)
attribute = attribute_parser.parse()
attribute.name = 'attribute'
ctx_root.set("PS:ATTRIBUTE", attribute)


attribute_parser = PatternParser(attribute_pattern, ctx_root)
attribute = attribute_parser.parse()
attribute.name = 'attribute'
ctx_root.set("PS:ATTRIBUTE", attribute)

# Parser para atributos múltiplos
attributes_pattern = "(&ATTRIBUTE)*"
attributes_parser = PatternParser(attributes_pattern, ctx_root)
attributes = attributes_parser.parse()
attributes.name = 'attributes'
ctx_root.set("PS:ATTRIBUTES", attributes)

# Parser para tag aberta (com atributos opcionais)
open_tag_pattern = "&OPEN_BRACKET &IDENTIFIER &ATTRIBUTES &CLOSE_BRACKET"
open_tag_parser = PatternParser(open_tag_pattern, ctx_root)
open_tag = open_tag_parser.parse()
open_tag.name = 'open_tag'
ctx_root.set("PS:OPEN_TAG", open_tag)

# Parser para tag fechada
close_tag_pattern = "&OPEN_BRACKET &SLASH &IDENTIFIER &CLOSE_BRACKET"
close_tag_parser = PatternParser(close_tag_pattern, ctx_root)
close_tag = close_tag_parser.parse()
close_tag.name = 'close_tag'
ctx_root.set("PS:CLOSE_TAG", close_tag)

# Parser para texto
text_pattern = r'[^<]+'
text_finder = RegexFinder(pattern=text_pattern, name='text')
ctx_root.set("PS:TEXT", text_finder)

# Parser para elementos dentro de uma tag (pode ser outra tag ou texto)
element_pattern = "&TAG | &TEXT"
element_parser = PatternParser(element_pattern, ctx_root)
element = element_parser.parse()
element.name = 'element'
ctx_root.set("PS:ELEMENT", element)

# Parser para o corpo de uma tag (zero ou mais elementos)
content_pattern = "(&ELEMENT)*"
content_parser = PatternParser(content_pattern, ctx_root)
content = content_parser.parse()
content.name = 'content'
ctx_root.set("PS:CONTENT", content)

# Parser para tag completa
tag_pattern = "&OPEN_TAG &CONTENT &CLOSE_TAG"
tag_parser = PatternParser(tag_pattern, ctx_root)
tag = tag_parser.parse()
tag.name = 'tag'
ctx_root.set("PS:TAG", tag)

# Atualizar o ForwardFinder
tag_placeholder.set_target(tag)

# Parser raiz
root_pattern = "&TAG"
root_parser = PatternParser(root_pattern, ctx_root)
root = root_parser.parse()
root.name = 'root'
root.on_find_token = [extract]

# Código de exemplo
code = """
<code>
    require Ship
    <wolfram.Math instance=[Ship, Algo] anotherParameter={identifier: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

# Remover espaços em branco iniciais e finais
text = code.strip()

# Scan do texto
result_token, pos = root.scan(text, context=ctx_root, pos=0)

if result_token:
    print("Parsing bem-sucedido. O token resultante é:")
    print(result_token.to_yaml(indent=0))

    # Gerar a representação Mermaid
    mermaid_lines, _ = result_token.to_mermaid()
    mermaid_output = "graph TD;\n" + "\n".join(mermaid_lines)
    print("\nRepresentação Mermaid:\n")
    print(mermaid_output)
else:
    print("Parsing falhou.")

