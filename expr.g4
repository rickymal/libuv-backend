grammar expr;

program: (statement)+;

comments: '#'+ | \/\* EVERTHING \*\/

parameterOperator
    : 'native' | 'async'


// Declarações de funções e tipos nativos
functionDeclaration
    : parameterOperator* (aqui quero dizer que pode ter um parameterOperator ou mais de um na sequencia) // ex: native func ..., ou async native func ...

// Declarações e comandos
statement
    : varDeclaration // Variável ou constante
    | funcCall       // Chamada de função
    ;

// Declaração de variáveis e constantes
varDeclaration
    : functionDeclaration 
    ;

// Chamada de função
funcCall
    : (variableName | expression) '.' functionName '(' exprList? ')' // Método de objeto
    | functionName variableName                                      // Função com parâmetro único
    | functionName '(' exprList? ')'                                 // Função com parâmetros
    ;

// Tipos de dados e parâmetros de função
functionName : ID ;
variableName : ID ;
typeName     : ID ;

functionParams
    : 'data' type 
    ;

returnType
    : type
    ;

type
    : 'i32'
    | 'string'
    | 'IPrintable'
    | ID            // Para suportar tipos definidos pelo usuário
    ;

// Expressões
expression
    : INT           // Inteiros
    | '(' expression ')' // Expressões entre parênteses
    | funcCall      // Chamadas de função como expressões
    ;

// Lista de expressões para parâmetros de função
exprList : expression (',' expression)* ;

// Tokens
NEWLINE : [\r\n]+ -> skip ;
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INT     : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
EVERTHING : *;