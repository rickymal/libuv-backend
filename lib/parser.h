#ifndef PARSER_H
#define PARSER_H

#include "lexer.h"  // Inclui as definições de Lexer, substitua por "lexer.h" ao invés de "lexer.cpp"

// Declaração da estrutura ASTNode e suas subclasses
struct ASTNode {
    virtual ~ASTNode() {}
};

struct BinaryOp : public ASTNode {
    ASTNode* left;
    ASTNode* right;
    TokenType op;

    BinaryOp(ASTNode* left, TokenType op, ASTNode* right);
};

struct Number : public ASTNode {
    int value;
    explicit Number(int value);
};


// Declaração da classe Parser
class Parser {
public:
    explicit Parser(const std::vector<Token>& tokens);
    ASTNode* parse();

private:
    std::vector<Token> tokens;
    size_t pos;

    ASTNode* expression();
    ASTNode* term(); // Certifique-se de implementar isso em Parser.cpp se necessário
};

#endif // PARSER_H
