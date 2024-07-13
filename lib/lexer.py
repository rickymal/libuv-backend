import pdb

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'

class Lexer:
    def __init__(self):
        self.input = ""
        self.position = 0
        self.current_char = None

    def from_input(self, input_):
        self.input = input_
        self.position = 0
        self.current_char = self.input[self.position] if self.input else None

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

    def word(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def skip_comment(self):
        while self.current_char is not None and self.current_char != "\n":
            self.advance()
        self.advance()

    def check_comment(self):
        try:
            return (self.current_char == "/" and self.peek() == "/") or self.current_char == "#"
        except:
            pdb.set_trace()
    
    def peek(self):
        peek_pos = self.position + 1
        if peek_pos < len(self.input):
            # return self.input(peek_pos)
            return self.input[peek_pos]
        return None

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.check_comment():
                self.skip_comment()
                continue

            if self.current_char.isdigit():
                tokens.append(Token('INTEGER', self.integer()))
            elif self.current_char == '+':
                tokens.append(Token('PLUS', '+'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token('MINUS', '-'))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token("EQUAL", "="))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token("OPEN_BRACKET", '('))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token("CLOSE_BRACKET", ')'))
                self.advance()
            elif self.current_char == ";":
                tokens.append(Token("END_COMMNAND", ";"))
                self.advance()
            elif self.current_char == ".":
                tokens.append(Token("PUNCTUATION","."))
                self.advance()
            elif self.current_char.isalpha() or self.current_char == '_':
                word = self.word()
                if word in ['var', 'const', 'type', 'native', 'print']:
                    tokens.append(Token(word.upper(), word))
                else:
                    tokens.append(Token('IDENTIFIER', word))
            else:
                raise Exception(f'Invalid character: {self.current_char}')
        return tokens

