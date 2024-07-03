#include "parser.h"

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
