from antlr4 import *
from output_directory.lunaLexer import lunaLexer
from output_directory.lunaParser import lunaParser

def text():
    return """
    func main() int{
        var a = 1;
        var b = 2;
        var c = a + b;
        return c;
    }
    """

def main():

    input_stream = InputStream(text())
    lexer = lunaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = lunaParser(stream)
    
    # Supondo que 'program' seja a regra inicial da gramática
    tree = parser.program()

    # Opcional: para visualizar a árvore de parse
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
