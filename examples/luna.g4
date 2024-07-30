grammar luna;

// variable declarations
program: statement* EOF;

typeModifier: 'const' | 'var';

allocatorSize: ('i32' | 'i64');

expression: 
    primaryExpression
    | wordWithParameter
    | expression '+' expression
    | expression '-' expression
    ;

primaryExpression:
    atom
    | anonymysFunctionDeclaration
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
functionDeclaration: (modifier+) 'func' WORD '(' parameters? ')' type? block;
anonymysFunctionDeclaration: 'func'? WORD? '(' parameters? ')' type? block;
wordWithParameter: 
    WORD '(' (INT | STRING) ')'
;
returnCall: 'return' expression?;
parameters: parameter (',' parameter)*;
parameter: WORD type;

modifier:
    wordWithParameter
    | WORD
;


type: 'i32' | 'i64' | 'void' | WORD | 'func' '(' typeParameters? ')' type ; 
typeParameters: type (',' type)*;


block: '{' statement* '}';

WORD: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';
WS: [ \t\r\n]+ -> skip;

statement
    : memoryAllocation
    | functionDeclaration
    | block
    | returnCall
    ;
