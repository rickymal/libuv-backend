grammar lunav2;

program: statement* EOF;

typeModifier: 'const' | 'var';

allocatorSize: ('i32' | 'i64');

expression: 
    primaryExpression
    | expression '+' expression
    | expression '-' expression
    ;

primaryExpression:
    atom
    | primaryExpression '*' primaryExpression
    | primaryExpression '/' primaryExpression
    ;

atom:
    INT
    | STRING
    | WORD
    | '(' expression ')'
    ;

memoryAllocation: typeModifier WORD allocatorSize? '=' expression ';'?;

functionDeclaration: 
    'func' WORD '(' parameters? ')' returnType? block
    | asyncModifier? 'func' funcModifier* WORD '(' parameters? ')' returnType? block
    ;

asyncModifier: 'async' ('(' 'use:' libuvConfig ')')?;
funcModifier: 'private' | 'stream';

libuvConfig: WORD ('.' WORD)?;

parameters: parameter (',' parameter)*;
parameter: WORD type;

returnType: 'func' '(' parameters? ')' type | type;

type: 'i32' | 'i64' | 'string' | 'void' | WORD;

block: '{' statement* '}';

statement:
    memoryAllocation
    | functionCall
    | block
    | returnStatement
    ;

functionCall: WORD '(' arguments? ')' ';';
arguments: expression (',' expression)*;

returnStatement: 'return' expression? ';';

WORD: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
