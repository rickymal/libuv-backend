parser grammar lunaParser;

options {
    tokenVocab = lunaLexer;
}
// Regras do Parser

document
    : element+ EOF
    ;

element
    : codeBlock
    | htmlBlock
    ;

htmlBlock
    : OPEN name attribute* CLOSE
    ;

name
    : Id1
    ;

codeBlock: Id1;
attribute
    : Id1 EQUALS Id2
    ;