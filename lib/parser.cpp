#include "lexer.h"

struct ASTNode {
    virtual ~ASTNode() {}
};

struct BinaryOp : public ASTNode {
    ASTNode* left;
    ASTNode* right;
    TokenType op;

    BinaryOp(ASTNode* left, TokenType op, ASTNode* right) : left(left), op(op), right(right) {}
};

struct Number : public ASTNode {
    int value;
    explicit Number(int value) : value(value) {}
};

class Parser {
public:
    Parser(const std::vector<Token>& tokens) : tokens(tokens), pos(0) {}

    ASTNode* parse() {
        return expression();
    }

private:
    std::vector<Token> tokens;
    size_t pos;

    ASTNode* expression() {
        ASTNode* result = term();
        while (pos < tokens.size() &&
               (tokens[pos].type == TokenType::PLUS || tokens[pos].type == TokenType::MINUS)) {
            Token op = tokens[pos];
            pos++;
            ASTNode* right = term();
            result = new BinaryOp(result, op.type, right);
        }
        return result;
    }

    ASTNode* term() {
        return nullptr;
    }
};
