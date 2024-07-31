grammar luna;

// Variable Declarations
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
functionDeclaration: (modifier+)? 'func' WORD '(' parameters? ')' type? block;
anonymysFunctionDeclaration: 'func'? WORD? '(' parameters? ')' type? block;
wordWithParameter: 
    WORD '(' (expression (',' expression)*)? ')'
;

conditionExpression: expression ('<' | '>' | '<=' | '>=') expression;

// Control Flow Structures
ifStatement
    : 'if' conditionExpression block ('else' block)?
    ;

whileStatement
    : 'while' conditionExpression block
    ;

assignmentStatement: WORD '=' expression ';'?;

forStatement
    : 'for' '(' memoryAllocation? ';' conditionExpression? ';' assignmentStatement? ')' block
    ;

returnCall: 'return' expression? ';'?;
breakStatement: 'break' ';';
continueStatement: 'continue' ';';

parameters: parameter (',' parameter)*;
parameter: WORD type?;

modifier:
    wordWithParameter
    | WORD
;

type: 'i32' | 'i64' | 'void' | WORD | 'func' '(' typeParameters? ')' type ; 
typeParameters: type (',' type)*;

block: '{' statement* '}';

operationStatement: 
    ifStatement
    | whileStatement
    | forStatement
    | breakStatement
    | continueStatement
    ;

statement
    : memoryAllocation
    | wordWithParameter
    | functionDeclaration
    | returnCall
    | operationStatement
    ;

WORD: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';
WS: [ \t\r\n]+ -> skip;
