parser grammar lunaParser;

options {
    tokenVocab = lunaLexer;
}

// Entry point
document: element+ EOF;

// Elements
// element: OPEN id1 attributes? CLOSE content* endTag;
element: OPEN id1 attributes CLOSE content* endTag;

// Content between tags
content: TEXT | element;

// Close tag
endTag: OPEN SLASH id1 CLOSE;

// ID with dot notation
id1: Id1 (DOT Id1)*;

// id2 can be a list, object, string, or id1
id2
    : element
    | OPEN_BRACKET id1 (COMMA id1)* CLOSE_BRACKET
    | OPEN_BRACE id1 COLON STRING CLOSE_BRACE
    | STRING
    // | element
    // | id1
    ;

// Attributes
attributes: attribute*;

attribute: id1 EQUALS id2;
