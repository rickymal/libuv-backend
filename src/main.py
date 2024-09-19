# main.py

import sys
from antlr4 import *
from lunaLexer import lunaLexer
from lunaParser import lunaParser
from lunaInterpreter import lunaInterpreter

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo-fonte>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = lunaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = lunaParser(stream)
    tree = parser.program()

    interpreter = lunaInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main()
