#ifndef INTERPRETER_H
#define INTERPRETER_H

#include "parser.h"  // Inclui as definições de Parser

// Declarar a classe Interpreter aqui
class Interpreter {
public:
    explicit Interpreter(ASTNode* root);
    int interpret();
private:
    ASTNode* root;
    int evaluate(ASTNode* node);
};

#endif
