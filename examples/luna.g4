grammar luna;

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

WORD: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;

statement
    : memoryAllocation
    ;
