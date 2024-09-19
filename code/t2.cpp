enum Token {
    tok_eof = -1,
    tok_def = -2,
    tok_identifier = -3,
    tok_number = -4,
};

static std::string IdentifierStr;
static int NumVal;

int gettok() {
    static int LastChar = ' ';

    // Ignora espaços em branco
    while (isspace(LastChar))
        LastChar = getchar();

    if (isalpha(LastChar)) { // Identificadores
        IdentifierStr = LastChar;
        while (isalnum((LastChar = getchar())))
            IdentifierStr += LastChar;

        if (IdentifierStr == "def")
            return tok_def;
        return tok_identifier;
    }

    if (isdigit(LastChar)) { // Números
        std::string NumStr;
        do {
            NumStr += LastChar;
            LastChar = getchar();
        } while (isdigit(LastChar));

        NumVal = std::stoi(NumStr);
        return tok_number;
    }

    if (LastChar == '#') { // Comentários
        do
            LastChar = getchar();
        while (LastChar != EOF && LastChar != '\n' && LastChar != '\r');

        if (LastChar != EOF)
            return gettok();
    }

    if (LastChar == EOF)
        return tok_eof;

    // Símbolos individuais
    int ThisChar = LastChar;
    LastChar = getchar();
    return ThisChar;
}


class ExprAST {
public:
    virtual ~ExprAST() = default;
    virtual llvm::Value* codegen() = 0;
};

class NumberExprAST : public ExprAST {
    int Val;
public:
    NumberExprAST(int Val) : Val(Val) {}
    llvm::Value* codegen() override;
};

class VariableExprAST : public ExprAST {
    std::string Name;
public:
    VariableExprAST(const std::string &Name) : Name(Name) {}
    llvm::Value* codegen() override;
};

class BinaryExprAST : public ExprAST {
    char Op;
    std::unique_ptr<ExprAST> LHS, RHS;
public:
    BinaryExprAST(char Op, std::unique_ptr<ExprAST> LHS,
                  std::unique_ptr<ExprAST> RHS)
        : Op(Op), LHS(std::move(LHS)), RHS(std::move(RHS)) {}
    llvm::Value* codegen() override;
};

class CallExprAST : public ExprAST {
    std::string Callee;
    std::vector<std::unique_ptr<ExprAST>> Args;
public:
    CallExprAST(const std::string &Callee,
                std::vector<std::unique_ptr<ExprAST>> Args)
        : Callee(Callee), Args(std::move(Args)) {}
    llvm::Value* codegen() override;
};


static std::unique_ptr<ExprAST> ParseExpression();

static std::unique_ptr<ExprAST> ParseNumberExpr() {
    auto Result = std::make_unique<NumberExprAST>(NumVal);
    getNextToken(); // Consome o número
    return std::move(Result);
}

static std::unique_ptr<ExprAST> ParseParenExpr() {
    getNextToken(); // Consome '('
    auto V = ParseExpression();
    if (!V)
        return nullptr;

    if (CurTok != ')')
        return LogError("expected ')'");
    getNextToken(); // Consome ')'
    return V;
}

// Implementação de outras funções de parsing...

