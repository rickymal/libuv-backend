class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self):
        self.input = ""
        self.position = 0
        self.current_char = None

    def from_input(self, input_):
        self.input = input_
        self.position = 0
        self.current_char = self.input[self.position]

    def advance(self):
        self.position += 1
        if self.position >= len(self.input):
            self.current_char = None
        else:
            self.current_char = self.input[self.position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def tokenize(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                tokens.append(Token('INTEGER', self.integer()))
            elif self.current_char == '+':
                tokens.append(Token('PLUS', '+'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token('MINUS', '-'))
                self.advance()
            else:
                raise Exception(f'Invalid character: {self.current_char}')

        tokens.append(Token('EOF', None))
        return tokens
