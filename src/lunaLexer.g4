lexer grammar lunaLexer;

// Default mode
OPEN: '<' -> pushMode(INSIDE);
TEXT: ~[<]+; // Match any text except '<'

// Mode for inside a tag
mode INSIDE;
OPEN_: OPEN -> pushMode(INSIDE);
CLOSE: '>' -> popMode;
SLASH_CLOSE: '/>' -> popMode;
SLASH: '/';
EQUALS: '=';
DOT: '.';
Id1: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' (~["\\] | '\\' .)* '"' | '\'' (~['\\] | '\\' .)* '\'';
OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';
COMMA: ',';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';
COLON: ':';
S: [ \t\r\n]+ -> skip; // Skip whitespace
