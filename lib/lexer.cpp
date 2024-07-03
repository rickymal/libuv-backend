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
        while (pos < src.size()) {
            char current = src[pos];
            if (isdigit(current)) {
                tokens.push_back({TokenType::INTEGER, readNumber()});
            } else if (current == '+') {
                tokens.push_back({TokenType::PLUS, std::string(1, current)});
                pos++;
            } // Add more conditions for other token types
        }
        tokens.push_back({TokenType::END, ""});
        return tokens;
    }

private:
    std::string src;
    size_t pos;

    std::string readNumber() {
        size_t start = pos;
        while (pos < src.size() && isdigit(src[pos])) pos++;
        return src.substr(start, pos - start);
    }
};
