import re

class Lexer:
    """Lexer estendido para suportar funções e variáveis."""
    # Sub-regexes
    DIGIT = r'\d'
    LETTER = r'[a-zA-Z]'
    UNDERSCORE = r'_'
    IDENT_START = rf'{LETTER}|{UNDERSCORE}'
    IDENT_PART = rf'{LETTER}|{DIGIT}|{UNDERSCORE}'
    
    INTEGER = rf'{DIGIT}+'
    FLOAT = rf'{DIGIT}+\.\d*'
    NUMBER = rf'({FLOAT}|{INTEGER})'
    IDENTIFIER = rf'{IDENT_START}{IDENT_PART}*'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
    COMMA = r','
    WHITESPACE = r'[ \t]+'
    NEWLINE = r'\n+'
    MISMATCH = r'.'  # Qualquer outro caractere
    
    # Lista de palavras-chave
    keywords = {'func': 'FUNC', 'return': 'RETURN'}
    
    # Lista de especificações de tokens usando os sub-regexes
    token_specification = [
        ('NUMBER',     NUMBER),       # Número inteiro ou decimal
        ('IDENTIFIER', IDENTIFIER),   # Identificadores
        ('ASSIGN',     ASSIGN),       # Sinal de igual =
        ('PLUS',       PLUS),         # Operador +
        ('MINUS',      MINUS),        # Operador -
        ('TIMES',      TIMES),        # Operador *
        ('DIVIDE',     DIVIDE),       # Operador /
        ('LPAREN',     LPAREN),       # Parêntese esquerdo
        ('RPAREN',     RPAREN),       # Parêntese direito
        ('LBRACE',     LBRACE),       # Chave esquerda
        ('RBRACE',     RBRACE),       # Chave direita
        ('COMMA',      COMMA),        # Vírgula
        ('NEWLINE',    NEWLINE),      # Quebra de linha
        ('SKIP',       WHITESPACE),   # Espaços e tabulações
        ('MISMATCH',   MISMATCH),     # Qualquer outro caractere
    ]
    
    def __init__(self, text):
        self.tokens = self.tokenize(text)
        self.position = 0
    
    def tokenize(self, text):
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specification)
        get_token = re.compile(token_regex).match
        pos = 0
        tokens = []
        while pos < len(text):
            match = get_token(text, pos)
            if match:
                kind = match.lastgroup
                value = match.group(kind)
                if kind == 'NUMBER':
                    value = float(value)
                elif kind == 'IDENTIFIER' and value in self.keywords:
                    kind = self.keywords[value]
                if kind not in ['SKIP', 'NEWLINE']:
                    tokens.append((kind, value))
                pos = match.end()
            else:
                raise SyntaxError(f'Caractere inesperado "{text[pos]}" em posição {pos}')
        tokens.append(('EOF', ''))
        return tokens
    
    def peek(self, offset=0):
        """Olha o token na posição atual mais offset."""
        if self.position + offset < len(self.tokens):
            return self.tokens[self.position + offset]
        return ('EOF', '')
    
    def next(self):
        """Consome o próximo token."""
        token = self.peek()
        self.position += 1
        return token

class Parser:
    """Parser estendido para suportar funções e variáveis."""
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead_buffer = []
        self.dfa_cache = {}  # Cache para transições do DFA
    
    def lookahead(self, k):
        """Garante que o buffer de lookahead tenha pelo menos k tokens."""
        while len(self.lookahead_buffer) < k:
            self.lookahead_buffer.append(self.lexer.next())
    
    def match(self, *expected_types):
        """Tenta casar os próximos tokens com os tipos esperados."""
        self.lookahead(len(expected_types))
        tokens = tuple(tok[0] for tok in self.lookahead_buffer[:len(expected_types)])
        if tokens == expected_types:
            for _ in expected_types:
                self.lookahead_buffer.pop(0)
            return True
        return False
    
    def expect(self, *expected_types):
        """Tenta casar os próximos tokens com os tipos esperados ou lança um erro."""
        if not self.match(*expected_types):
            expected = ' ou '.join(expected_types)
            actual = self.lookahead_buffer[0][0] if self.lookahead_buffer else 'EOF'
            raise SyntaxError(f'Esperado {expected}, mas encontrado {actual}')
    
    def parse(self):
        """Inicia o parsing."""
        ast = self.program()
        self.expect('EOF')
        return ast
    
    def program(self):
        nodes = []
        while not self.match('EOF'):
            if self.match('FUNC'):
                func_def = self.function_def()
                nodes.append(func_def)
            else:
                expr = self.expression()
                nodes.append(expr)
        return ('program', nodes)
    
    def function_def(self):
        self.expect('IDENTIFIER')
        func_name = self.lookahead_buffer.pop(0)[1]
        self.expect('LPAREN')
        params = self.parameter_list()
        self.expect('RPAREN')
        self.expect('LBRACE')
        body = self.block()
        self.expect('RBRACE')
        return ('func_def', func_name, params, body)
    
    def parameter_list(self):
        params = []
        while not self.match('RPAREN'):
            self.expect('IDENTIFIER')
            param_name = self.lookahead_buffer.pop(0)[1]
            params.append(param_name)
            if not self.match('COMMA'):
                break
            else:
                self.lookahead_buffer.pop(0)
        return params
    
    def block(self):
        statements = []
        while not self.match('RBRACE'):
            stmt = self.statement()
            statements.append(stmt)
        return ('block', statements)
    
    def statement(self):
        if self.match('RETURN'):
            self.lookahead_buffer.pop(0)
            expr = self.expression()
            return ('return', expr)
        else:
            expr = self.expression()
            return expr
    
    def expression(self):
        return self.expr()
    
    def expr(self):
        node = self.term()
        while True:
            if self.match('PLUS'):
                self.lookahead_buffer.pop(0)
                right = self.term()
                node = ('+', node, right)
            elif self.match('MINUS'):
                self.lookahead_buffer.pop(0)
                right = self.term()
                node = ('-', node, right)
            else:
                break
        return node
    
    def term(self):
        node = self.factor()
        while True:
            if self.match('TIMES'):
                self.lookahead_buffer.pop(0)
                right = self.factor()
                node = ('*', node, right)
            elif self.match('DIVIDE'):
                self.lookahead_buffer.pop(0)
                right = self.factor()
                node = ('/', node, right)
            else:
                break
        return node
    
    def factor(self):
        if self.match('NUMBER'):
            token = self.lookahead_buffer.pop(0)
            return ('num', token[1])
        elif self.match('IDENTIFIER'):
            token = self.lookahead_buffer.pop(0)
            if self.match('LPAREN'):
                self.lookahead_buffer.pop(0)
                # Chamada de função
                args = self.argument_list()
                self.expect('RPAREN')
                return ('call', token[1], args)
            else:
                # Variável
                return ('var', token[1])
        elif self.match('LPAREN'):
            self.lookahead_buffer.pop(0)
            expr_node = self.expr()
            self.expect('RPAREN')
            return expr_node
        else:
            raise SyntaxError('Token inesperado em factor')
    
    def argument_list(self):
        args = []
        while not self.match('RPAREN'):
            arg = self.expression()
            args.append(arg)
            if not self.match('COMMA'):
                break
            else:
                self.lookahead_buffer.pop(0)
        return args

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

def evaluate(node, env):
    if node[0] == 'program':
        result = None
        for stmt in node[1]:
            result = evaluate(stmt, env)
        return result
    elif node[0] == 'func_def':
        _, func_name, params, body = node
        env['functions'][func_name] = (params, body)
    elif node[0] == 'return':
        value = evaluate(node[1], env)
        raise ReturnException(value)
    elif node[0] == 'num':
        return node[1]
    elif node[0] == 'var':
        name = node[1]
        if name in env['variables']:
            return env['variables'][name]
        else:
            raise NameError(f"Variável não definida '{name}'")
    elif node[0] == '+':
        return evaluate(node[1], env) + evaluate(node[2], env)
    elif node[0] == '-':
        return evaluate(node[1], env) - evaluate(node[2], env)
    elif node[0] == '*':
        return evaluate(node[1], env) * evaluate(node[2], env)
    elif node[0] == '/':
        return evaluate(node[1], env) / evaluate(node[2], env)
    elif node[0] == 'call':
        func_name = node[1]
        args = node[2]
        if func_name in env['functions']:
            params, body = env['functions'][func_name]
            if len(args) != len(params):
                raise TypeError(f"Função '{func_name}' espera {len(params)} argumentos, mas recebeu {len(args)}")
            local_env = {
                'variables': {},
                'functions': env['functions'],
            }
            for param, arg in zip(params, args):
                local_env['variables'][param] = evaluate(arg, env)
            try:
                evaluate(body, local_env)
            except ReturnException as e:
                return e.value
            return None
        else:
            raise NameError(f"Função não definida '{func_name}'")
    elif node[0] == 'block':
        result = None
        for stmt in node[1]:
            result = evaluate(stmt, env)
        return result
    else:
        raise ValueError(f"Nó desconhecido {node[0]}")

# Exemplo de uso
if __name__ == '__main__':
    expression = """
        func sum(a, b) {
            return a + b
        }

        sum(10, 20) + 3 - (3 + 2)
    """
    lexer = Lexer(expression)
    parser = Parser(lexer)
    ast = parser.parse()
    # print(f"AST: {ast}")
    env = {'variables': {}, 'functions': {}}
    result = evaluate(ast, env)
    print(f"Resultado: {result}")
