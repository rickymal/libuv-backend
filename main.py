# main.py
from lib.lexer import Lexer
from lib.parser import Parser
from lib.interpreter import Interpreter

def main():
    input_expr = "9 + 1 - 1"
    lexer = Lexer()
    lexer.from_input(input_expr)
    tokens = lexer.tokenize()

    print(tokens)
    parser = Parser(tokens)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    print(f"Resultado: {result}")

if __name__ == "__main__":
    main()
