class PrototypeContext:
    def __init__(self, parent=None, name=''):
        self.parent = parent
        self.name = name
        self.variables = {}

    def set(self, key, value):
        """Stores a value under the given key in the current context."""
        self.variables[key] = value

    def get(self, key):
        """Retrieves the value associated with the key, searching parent contexts if necessary."""
        if key in self.variables:
            return self.variables[key]
        elif self.parent:
            return self.parent.get(key)
        else:
            return None

    def chain_new_context(self, name=''):
        """Creates a new child context that inherits from the current context."""
        return PrototypeContext(parent=self, name=name)

class LiteralFinder:
    def __init__(self, pattern, dim=None):
        self.pattern = pattern
        self.dim = dim or ('default',)

    def find(self, text, pos=0):
        """Encontra todas as ocorrências do padrão literal no texto a partir da posição pos."""
        matches = []
        index = text.find(self.pattern, pos)
        while index != -1:
            start_pos = index
            end_pos = index + len(self.pattern)
            # Calcula linha e coluna inicial
            start_line = text.count('\n', 0, start_pos) + 1
            start_line_start_pos = text.rfind('\n', 0, start_pos)
            if start_line_start_pos == -1:
                start_line_start_pos = -1
            start_column = start_pos - start_line_start_pos
            # Calcula linha e coluna final
            end_line = text.count('\n', 0, end_pos) + 1
            end_line_start_pos = text.rfind('\n', 0, end_pos)
            if end_line_start_pos == -1:
                end_line_start_pos = -1
            end_column = end_pos - end_line_start_pos
            result = {
                'start_line': start_line,
                'start_column': start_column,
                'end_line': end_line,
                'end_column': end_column,
                'value': self.pattern,
                'dim': self.dim
            }
            matches.append(result)
            index = text.find(self.pattern, end_pos)
        return matches


import re

import re

class RegexFinder:
    def __init__(self, pattern, dim=None):
        self.pattern = pattern
        self.regex = re.compile(pattern)
        self.dim = dim or ('default',)

    def find(self, text, pos=0):
        """Encontra todas as correspondências do padrão regex no texto a partir da posição pos."""
        matches = []
        for match in self.regex.finditer(text, pos):
            start_pos = match.start()
            end_pos = match.end()
            # Calcula linha e coluna inicial
            start_line = text.count('\n', 0, start_pos) + 1
            start_line_start_pos = text.rfind('\n', 0, start_pos)
            if start_line_start_pos == -1:
                start_line_start_pos = -1
            start_column = start_pos - start_line_start_pos
            # Calcula linha e coluna final
            end_line = text.count('\n', 0, end_pos) + 1
            end_line_start_pos = text.rfind('\n', 0, end_pos)
            if end_line_start_pos == -1:
                end_line_start_pos = -1
            end_column = end_pos - end_line_start_pos
            result = {
                'start_line': start_line,
                'start_column': start_column,
                'end_line': end_line,
                'end_column': end_column,
                'value': match.group(),
                'dim': self.dim
            }
            matches.append(result)
        return matches


class EndOfFileFinder:
    def __init__(self, dim=None):
        self.dim = dim or ('default',)

    def find(self, text, pos=0):
        """Verifica se o fim do texto foi alcançado a partir da posição pos."""
        if pos >= len(text):
            # Calcula linha e coluna onde o EOF ocorre
            if text.endswith('\n'):
                pos = len(text) - 1  # Ajusta para não ultrapassar o índice
            start_line = text.count('\n', 0, pos) + 1
            start_line_start_pos = text.rfind('\n', 0, pos)
            if start_line_start_pos == -1:
                start_line_start_pos = -1
            start_column = pos - start_line_start_pos
            result = {
                'start_line': start_line,
                'start_column': start_column,
                'end_line': start_line,
                'end_column': start_column,
                'value': 'EOF',
                'dim': self.dim
            }
            return [result]
        else:
            return []

import re

import re

class PatternFinder:
    def __init__(self, pattern, context=None, personality=None, dim=None):
        self.pattern = pattern
        self.context = context or PrototypeContext()
        self.personality = personality
        self.dim = dim or ('default',)
        self.ast = self.parse_pattern(pattern)

    def parse_pattern(self, pattern):
        """Parses the pattern string into an abstract syntax tree (AST)."""
        tokens = self.tokenize(pattern)
        ast = self.build_ast(tokens)
        return ast

    def tokenize(self, pattern):
        """Tokenizes the pattern string into a list of tokens."""
        # Regex pattern for tokens
        token_specification = [
            ('FINDER', r'\&\w+'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('STAR', r'\*'),
            ('QMARK', r'\?'),
            ('PIPE', r'\|'),
            ('WHITESPACE', r'\s+'),
            ('UNKNOWN', r'.'),  # Any other character
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        pos = 0
        tokens = []
        mo = get_token(pattern, pos)
        while mo:
            kind = mo.lastgroup
            value = mo.group(kind)
            if kind != 'WHITESPACE':
                tokens.append({'type': kind, 'value': value})
            pos = mo.end()
            mo = get_token(pattern, pos)
        if pos != len(pattern):
            raise SyntaxError('Unexpected character %r at position %d' % (pattern[pos], pos))
        return tokens

    def build_ast(self, tokens):
        """Builds an AST from the list of tokens."""
        def parse_expression(index):
            """Parses an expression from tokens starting at index."""
            nodes = []
            while index < len(tokens):
                token = tokens[index]
                if token['type'] == 'FINDER':
                    node = {'type': 'FINDER', 'value': token['value'][1:]}  # Remove '&'
                    index += 1
                    # Check for quantifiers
                    if index < len(tokens) and tokens[index]['type'] in ('STAR', 'QMARK'):
                        quantifier = tokens[index]['type']
                        node = {'type': 'QUANTIFIER', 'quantifier': quantifier, 'node': node}
                        index += 1
                    nodes.append(node)
                elif token['type'] == 'LPAREN':
                    index += 1
                    sub_nodes, index = parse_expression(index)
                    node = {'type': 'GROUP', 'nodes': sub_nodes}
                    # Check for quantifiers
                    if index < len(tokens) and tokens[index]['type'] in ('STAR', 'QMARK'):
                        quantifier = tokens[index]['type']
                        node = {'type': 'QUANTIFIER', 'quantifier': quantifier, 'node': node}
                        index += 1
                    nodes.append(node)
                elif token['type'] == 'RPAREN':
                    index += 1
                    break
                elif token['type'] == 'PIPE':
                    index += 1
                    right_nodes, index = parse_expression(index)
                    nodes = [{'type': 'ALTERNATION', 'left': nodes, 'right': right_nodes}]
                    break
                else:
                    raise SyntaxError(f"Unexpected token {token['type']} at position {index}")
            return nodes, index

        ast, index = parse_expression(0)
        if index != len(tokens):
            raise SyntaxError('Unexpected end of pattern')
        return ast

    def find(self, text, pos=0):
        """Matches the pattern against the text starting from position pos."""
        matches, end_pos = self.match_node(self.ast, text, pos)
        if matches is not None:
            return matches
        else:
            return []

    def match_node(self, node, text, pos):
        """Recursively matches a node in the AST against the text starting from pos."""
        if not node:
            return [], pos

        if isinstance(node, list):
            # Sequence of nodes
            current_pos = pos
            all_matches = []
            for child in node:
                matches, current_pos = self.match_node(child, text, current_pos)
                if matches is None:
                    return None, pos
                all_matches.extend(matches)
            return all_matches, current_pos

        elif node['type'] == 'FINDER':
            finder_name = node['value']
            finder = self.context.get(finder_name)
            if finder:
                match = finder.find(text, pos)
                if match:
                    return match, match[-1]['end_column'] - 1
                else:
                    return None, pos
            else:
                raise ValueError(f"Finder '{finder_name}' not found in context")

        elif node['type'] == 'GROUP':
            return self.match_node(node['nodes'], text, pos)

        elif node['type'] == 'QUANTIFIER':
            quantifier = node['quantifier']
            child_node = node['node']
            if quantifier == 'STAR':
                matches = []
                current_pos = pos
                while True:
                    result, new_pos = self.match_node(child_node, text, current_pos)
                    if result is not None:
                        matches.extend(result)
                        current_pos = new_pos
                        if new_pos == current_pos:
                            break
                    else:
                        break
                return matches, current_pos
            elif quantifier == 'QMARK':
                result, new_pos = self.match_node(child_node, text, pos)
                if result is not None:
                    return result, new_pos
                else:
                    return [], pos
            else:
                raise ValueError(f"Unknown quantifier '{quantifier}'")

        elif node['type'] == 'ALTERNATION':
            left_result, left_pos = self.match_node(node['left'], text, pos)
            if left_result is not None:
                return left_result, left_pos
            right_result, right_pos = self.match_node(node['right'], text, pos)
            if right_result is not None:
                return right_result, right_pos
            return None, pos

        else:
            raise ValueError(f"Unknown node type '{node['type']}'")



class IVisitorPatternInterpreter(type):
    def __new__(cls, name, bases, attrs):
        # Cria a classe primeiro
        new_class = super().__new__(cls, name, bases, attrs)
        
        # Obtém todos os atributos da classe, incluindo herdados
        members = dir(new_class)
        
        # Filtra apenas os métodos que começam com 'visit_'
        visit_methods = [attr for attr in members if attr.startswith('visit_') and callable(getattr(new_class, attr))]
        
        if not visit_methods:
            raise TypeError(f"A classe '{name}' deve definir pelo menos um método que começa com 'visit_'")
        
        return new_class

import yaml

class YAMLExporter(metaclass=IVisitorPatternInterpreter):
    def __init__(self):
        self.result = None

    def export(self, root_node):
        self.result = self.visit(root_node)
        yaml_output = yaml.dump(self.result, sort_keys=False)
        return yaml_output

    def visit_node(self, node):
        """Visits a node and returns its YAML representation."""
        node_dict = self._node_to_dict(node)
        return yaml.dump(node_dict, sort_keys=False)

    def _node_to_dict(self, node):
        node_dict = {
            'type': type(node).__name__,
            'value': getattr(node, 'value', None),
            'start_line': getattr(node, 'start_line', None),
            'start_column': getattr(node, 'start_column', None),
            'end_line': getattr(node, 'end_line', None),
            'end_column': getattr(node, 'end_column', None),
            'dim': getattr(node, 'dim', None),
            'children': [self.visit(child) for child in getattr(node, 'children', [])]
        }
        return node_dict


    # Example of a specific visit method
    def visit_LiteralFinder(self, node):
        return self.visit_node(node)

    # Additional 'visit_' methods for other node types can be added here



class ASTStreamingText:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.length = len(text)
        self.line = 1
        self.column = 1

    def peek(self, length=1):
        """Retorna os próximos 'length' caracteres sem avançar a posição."""
        return self.text[self.pos:self.pos + length]

    def consume(self, length=1):
        """Avança a posição em 'length' e retorna os caracteres consumidos."""
        result = self.text[self.pos:self.pos + length]
        self.pos += length
        # Atualiza linha e coluna
        lines = result.count('\n')
        if lines > 0:
            self.line += lines
            last_newline_index = result.rfind('\n')
            self.column = len(result) - last_newline_index
        else:
            self.column += length
        return result

    def is_eof(self):
        """Verifica se o fim do texto foi alcançado."""
        return self.pos >= self.length

    def get_position(self):
        """Retorna a posição atual (linha e coluna)."""
        return self.line, self.column

    def reset(self):
        """Reseta a posição para o início do texto."""
        self.pos = 0
        self.line = 1
        self.column = 1

    def consume_until(self, condition):
        """Consome caracteres até que a condição seja verdadeira."""
        result = ''
        while not self.is_eof() and not condition(self.peek()):
            result += self.consume()
        return result

    def lookahead(self, condition, max_length=1):
        """Olha adiante no texto e retorna True se a condição for satisfeita."""
        text_fragment = self.peek(max_length)
        return condition(text_fragment)


import logging

class TextMessager(ASTStreamingText):
    def __init__(self, text):
        super().__init__(text)
        self.logger = logging.getLogger(__name__)
        self.messages = []

    def log(self, message, level=logging.INFO):
        """Logs a message with the current line and column using the logging module."""
        try:
            line, column = self.get_position()
            full_message = f"Line {line}, Column {column}: {message}"
            self.logger.log(level, full_message)
            self.messages.append(full_message)
        except Exception as e:
            self.logger.error(f"Logging failed: {e}")

    def get_messages(self):
        """Returns a copy of all logged messages."""
        return list(self.messages)

    def clear_messages(self):
        """Clears all logged messages."""
        self.messages.clear()


class ClassicInputStream:
    def __init__(self, text: str):
        self.text: str = text
        self.pos: int = 0
        self.length: int = len(text)
        self.line: int = 1
        self.column: int = 1

    def read(self, n: int = 1) -> str:
        """Reads the next 'n' characters and advances the position."""
        if self.pos >= self.length:
            return None  # Explicitly indicate EOF
        else:
            result = self.text[self.pos:self.pos + n]
            self.pos += n
            # Update line and column numbers
            lines = result.count('\n')
            if lines > 0:
                self.line += lines
                last_newline_index = result.rfind('\n')
                self.column = len(result) - last_newline_index
            else:
                self.column += n
            return result

    def peek(self, n: int = 1) -> str:
        """Peeks at the next 'n' characters without advancing the position."""
        return self.text[self.pos:self.pos + n]

    def consume(self, n: int = 1) -> str:
        """Alias for 'read' to maintain consistency with other stream classes."""
        return self.read(n)

    def is_eof(self) -> bool:
        """Checks if the end of the text has been reached."""
        return self.pos >= self.length

    def reset(self) -> None:
        """Resets the stream to the beginning."""
        self.pos = 0
        self.line = 1
        self.column = 1

    def seek(self, pos: int) -> None:
        """Sets the current position to 'pos'."""
        if 0 <= pos <= self.length:
            self.pos = pos
            # Update line and column numbers
            self.line, self.column = self._calculate_line_column(pos)
        else:
            raise ValueError("Position out of bounds.")

    def tell(self) -> int:
        """Returns the current position."""
        return self.pos

    def get_position(self) -> (int, int):
        """Returns the current line and column numbers."""
        return self.line, self.column

    def _calculate_line_column(self, pos: int) -> (int, int):
        """Calculates line and column numbers up to a given position."""
        text_up_to_pos = self.text[:pos]
        line = text_up_to_pos.count('\n') + 1
        last_newline_index = text_up_to_pos.rfind('\n')
        if last_newline_index == -1:
            column = pos + 1
        else:
            column = pos - last_newline_index
        return line, column


def init(root_parser, input_stream, transpiler):
    """
    Inicializa o processo de parsing com o parser raiz, fluxo de entrada e transpiler fornecidos.
    """
    # Configura o input_stream e o transpiler no root_parser
    root_parser.input_stream = input_stream
    root_parser.transpiler = transpiler

    try:
        # Inicia o parsing
        parse_tree = root_parser.parse()

        # Processa a árvore de parsing com o transpiler
        result = transpiler.visit(parse_tree)

        # Retorna o resultado do transpiler, se necessário
        return result

    except Exception as e:
        print(f"Erro durante o parsing: {e}")
        # Possibilidade de lidar com a exceção ou re-levantar
        raise
