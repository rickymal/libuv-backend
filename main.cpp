#include <iostream>
#include "lib/core.cpp"

int main() {
    std::string input = "1 + 2 - 3";  // Exemplo de entrada
    Lexer lexer(input);
    std::cout << "iniciando tokenização" << std::endl;
    std::vector<Token> tokens = lexer.tokenize();  // Tokenizar a entrada

    Parser parser(tokens);
    ASTNode* root = parser.parse();  // Parsear os tokens para criar a AST

    std::cout << "iniciando tokenização" << std::endl;
    // Aqui você poderia adicionar um interpretador para executar a AST
    Interpreter interpreter(root);
    int result = interpreter.interpret();  // Interpretar e executar a AST

    std::cout << "Resultado da expressão: " << result << std::endl;

    // Limpar memória
    delete root;

    return 0;
}
