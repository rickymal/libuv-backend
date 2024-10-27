lexer grammar lunaLexer;


// Whitespace and Comments



OPEN_ELEMENT: '<' ;
WS3               : [\t\r\n]+ -> skip;
fragment LETTER: [a-zA-Z_À-ÿ];  // Incluindo suporte a letras acentuadas
fragment DIGIT: [0-9];
fragment QUALIFIED_IDENTIFIER: IDENTIFIER ('.' IDENTIFIER)*?; 
fragment IDENTIFIER: LETTER (LETTER | DIGIT)+;
QUALIFIED_IDENTIFIER_XML: QUALIFIED_IDENTIFIER -> pushMode(PROC_ISTR);  

// [a-zA-Z_À-ÿ] ([a-zA-Z_À-ÿ] | [0-9]))
mode PROC_ISTR;
LETTER_: LETTER;
DIGIT_: DIGIT;

OPEN_: OPEN_ELEMENT -> pushMode(PROC_ISTR);
CLOSE_ELEMENT: '>' -> pushMode(PROC_EXTR);
EQUAL: '=';
OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';
OPEN_KEY: '{';
CLOSE_KEY: '}';
TWO_DOT: ':';
SLASH: '/';
COMMA: ',';
DOT: '.';
WS2               : [ \t\r\n]+ -> skip;


mode PROC_EXTR;
WS1               : [\t\r\n]+ -> skip;
TEXT: (.)*;
ENCLOSER: '</' -> popMode, more;