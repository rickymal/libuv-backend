# main.py
from lib.lexer import Lexer
from lib.parser import Parser
from lib.interpreter import Interpreter
import os

class Language:
    def __init__(self):
        self.lexer = Lexer()
    
    def process(self, expression : str):
        tokens = self.load_tokens(expression=expression)
        print(tokens)
        parser = Parser(tokens)
        interpreter = Interpreter(parser)
        return interpreter.interpret()

    def load_tokens(self, expression : str):
        self.lexer.from_input(expression)
        return self.lexer.tokenize()
        
def main():
    input_expr = "9 + 1 - 1"
    # lexer = Lexer()
    # lexer.from_input(input_expr)
    # tokens = lexer.tokenize()

    # print(tokens)
    # parser = Parser(tokens)
    # interpreter = Interpreter(parser)
    # result = interpreter.interpret()
    print(os.listdir("examples"))
    # FileNotFoundError: [Errno 2] No such file or directory: 'examples/core-functionalities.txt'
    with open("examples/core-functionalities.txt") as file:
        input_expr = file.read()

    language = Language()
    print(f"Resultado: {language.load_tokens(input_expr)}")
    # print(f"Resultado: {language.process(input_expr)}")


if __name__ == "__main__":
    main()
