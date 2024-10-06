/*
 [The "BSD licence"]
 Copyright (c) 2013 Terence Parr
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/** XML lexer derived from ANTLR v4 ref guide book example */

// $antlr-format alignTrailingComments true, columnLimit 150, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine true, allowShortBlocksOnASingleLine true, minEmptyLines 0, alignSemicolons ownLine
// $antlr-format alignColons trailing, singleLineOverrulesHangingColon true, alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar lunaLexer;

// Default "mode": Everything OUTSIDE of a tag


COMMENT : '<!--' .*? '-->';
CDATA   : '<![CDATA[' .*? ']]>';
/** Scarf all DTD stuff, Entity Declarations like <!ENTITY ...>,
 *  and Notation Declarations <!NOTATION ...>
 */
DTD       : '<!' .*? '>' -> skip;
EntityRef : '&' Id1 ';';
CharRef   : '&#' DIGIT+ ';' | '&#x' HEXDIGIT+ ';';
SEA_WS    : (' ' | '\t' | '\r'? '\n')+;

OPEN         : '<'       -> pushMode(INSIDE);
XMLDeclOpen  : '<?xml' S -> pushMode(INSIDE);
SPECIAL_OPEN : '<?' Id1 -> more, pushMode(PROC_INSTR);

TEXT: ~[<&]+; // match any 16 bit char other than < and &

// ----------------- Everything INSIDE of a tag ---------------------
mode INSIDE;

CLOSE         : '>'  -> popMode;
SPECIAL_CLOSE : '?>' -> popMode; // close <?xml...?>
SLASH_CLOSE   : '/>' -> popMode;
SLASH         : '/';
EQUALS        : '=';

S             : [ \t\r\n] -> skip;
Id1
    : [a-zA-Z_À-ÿ][a-zA-Z_0-9À-ÿ]* ('.' [a-zA-Z_À-ÿ][a-zA-Z_0-9À-ÿ]*)*
    ;
Id2
    : STRING
    | Id1                        // Identificador simples
    | '[' Id1 (',' Id1)* ']'      // Lista de identificadores
    | '{' Id1 ':' STRING '}'     // Objeto chave-valor
                  // String simples
    ;

STRING        : '"' ~[<"]* '"' | '\'' ~[<']* '\'';   

fragment HEXDIGIT: [a-fA-F0-9];

fragment DIGIT: [0-9];

// ----------------- Handle <? ... ?> ---------------------
mode PROC_INSTR;

PI     : '?>' -> popMode; // close <?...?>
IGNORE : .    -> more;