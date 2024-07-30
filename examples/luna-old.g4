grammar luna;

program: statement* EOF;

statement
    : memoryAllocation
    | funcDeclaration
    | typeDeclaration
    | expressionStatement
    ;

memoryAllocation
    : 'var' ID '=' expression ';'?
    | 'const' ID '=' expression ';'?
    ;

funcDeclaration
    : 'func' ID '(' params? ')' type? block
    | '(' params? ')' type? block
    ;

typeDeclaration
    : 'type' ID 'struct' '{' field* '}'
    ;

field
    : ID type ';'?
    ;

params
    : param (',' param)*
    ;

param
    : ID type
    ;

type
    : ID
    | arrayType
    ;

arrayType
    : '[' ']' type
    ;

block
    : '{' statement* '}'
    ;

expressionStatement
    : expression ';'?
    ;

expression
    : mathOperationIdentifier
    | identifier
    | vectorIdentifier
    ;

mathOperationIdentifier
    : identifier (('*' | '/') identifier)*
    ;

// operationExpression
//     : math3Expression
//     | math2Expression
//     | primary
//     ;

// math3Expression
//     : primary (('*' | '/') primary)*
//     ;

// math2Expression
//     : primary (('+' | '-') primary)*
//     ;

// // [1, 2, 3, 4, 5]
// arrayPrimary
//     : '[' primary (',' primary)* ']'
//     ;

vectorIdentifier: '[' identifier (',' identifier)* ']';

identifier
    : INT
    | STRING
    | ID
    ;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
