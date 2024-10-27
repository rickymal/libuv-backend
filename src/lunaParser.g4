parser grammar lunaParser;

options {
    tokenVocab = lunaLexer;
}
// Starting rule
document
    : statement+
    ;

statement
    : xmlElement
    ;


xmlOpenStructure
    : OPEN_ELEMENT QUALIFIED_IDENTIFIER_XML attributes*? CLOSE_ELEMENT 
    ;

xmlCloseStructure
    : OPEN_ELEMENT SLASH QUALIFIED_IDENTIFIER CLOSE_ELEMENT
    ;

xmlElement: xmlOpenStructure content xmlCloseStructure;


content
    : TEXT ENCLOSER
    ;

attributes
    : cName EQUAL sequenceId1
    | cName EQUAL objId1
    | cName EQUAL xmlElement
    ;

objId1
    : OPEN_KEY cName TWO_DOT sequenceId1
    | OPEN_KEY cName TWO_DOT objId1
    ;

sequenceId1
    : OPEN_BRACKET cName (COMMA cName)*? CLOSE_BRACKET
    ;


cName: QUALIFIED_IDENTIFIER;