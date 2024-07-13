#include <iostream>
#include <string>
#include <vector>
#include <sstream>

// #include "lexer.h"

enum class TokenType {
    INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, IDENTIFIER, ASSIGN, END
};

struct Token {
    TokenType type;
    std::string value;
};

class Lexer {
public:
    Lexer(const std::string& src) : src(src), pos(0) {}

    std::vector<Token> tokenize() {
        std::vector<Token> tokens;
        std::cout << "Quantidade: " << src.size() << std::endl;
        while (pos < src.size()) {
            std::cout << "Defining pos:" << pos << std::endl;
            char current = src[pos];
            if (isdigit(current)) {
                tokens.push_back({TokenType::INTEGER, readNumber()});
            } else if (current == '+') {
                tokens.push_back({TokenType::PLUS, std::string(1, current)});
                pos++;
            } else if (current == "-") {
                tokens.push_back({TokenType::MINUS, std::string(1, current)});
                pos++;
            }
        }
        tokens.push_back({TokenType::END, ""});
        return tokens;
    }

private:
    std::string src;
    size_t pos; // identifier "size_t" is undefinedC/C++(20)

        std::string readNumber() {
        size_t start = pos;
        while (pos < src.size() && isdigit(src[pos])) pos++;
        return src.substr(start, pos - start);
    }
};



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


class Interpreter
{
public:
    Interpreter(ASTNode *root) : root(root) {}

    int interpret()
    {
        return evaluate(root);
    }

private:
    ASTNode *root;

    int evaluate(ASTNode *node)
    {
        if (auto binOp = dynamic_cast<BinaryOp *>(node))
        {
            int left = evaluate(binOp->left);
            int right = evaluate(binOp->right);
            switch (binOp->op)
            {
            case TokenType::PLUS:
                return left + right;
            case TokenType::MINUS:
                return left - right;
                // Adicione outras operações conforme necessário
            }
        }
        else if (auto num = dynamic_cast<Number *>(node))
        {
            return num->value; // Não precisa de conversão
        }
        return 0;
    }   
};
