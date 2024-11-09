grammar malech;

program: (statement)+;

functionDeclaration
    : 'func' functionName '(' functionParams? ')' returnType? ';'?
    | 'interface' interfaceName ';'?
    ;

memoryAllocationStatement
    : 'var' variableName type? '=' expression ';'?
    | 'const' variableName '=' expression ';'?
    ;

statement
    : memoryAllocationStatement
    | funcCall
    | functionDeclaration
    ;

funcCall
    : (variableName | '(' expression ')') '.' functionName ( '(' exprList? ')' | exprList )
    | functionName (variableName | '(' exprList? ')')
    ;

functionName : ID;
variableName : ID;
typeName     : ID;
interfaceName : ID;

functionParams : ID type;
returnType    : type;

type
    : ID
    ;

expression
    : NUMBER
    | '(' expression ')'
    | funcCall
    ;

exprList : expression (',' expression)*;

COMMENT
    : '/*' .*? '*/'
    | '//' ~[\r\n]*
    | '#' ~[\r\n]*
    ;

COMMENT_SKIP : COMMENT -> skip;

WS      : [ \t\r\n]+ -> skip ;
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER     : [0-9]+ ;
