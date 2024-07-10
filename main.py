# main.py
from lib.lexer import Lexer
from lib.parser import Parser
from lib.interpreter import Interpreter


class Language:
    def __init__(self):
        self.lexer = Lexer()
    
    def process(self, expression : str):
        self.lexer.from_input(expression)
        tokens = self.lexer.tokenize()
        parser = Parser(tokens)
        interpreter = Interpreter(parser)
        return interpreter.interpret()

def main():
    input_expr = "9 + 1 - 1"
    # lexer = Lexer()
    # lexer.from_input(input_expr)
    # tokens = lexer.tokenize()

    # print(tokens)
    # parser = Parser(tokens)
    # interpreter = Interpreter(parser)
    # result = interpreter.interpret()

    language = Language()

    print(f"Resultado: {language.process(input_expr)}")

if __name__ == "__main__":
    main()
