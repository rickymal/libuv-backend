#!/bin/bash

# Carrega os aliases definidos
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# Sobrescrevendo o alias para incluir dist
alias parser='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar:./dist:$CLASSPATH" org.antlr.v4.gui.TestRig'

rm -r dist/
clear
echo '--------------------------- Parsing luna ----------------------------'
parser lunaLexer.g4 lunaParser.g4 -o dist/

echo '--------------------------- Compiling luna --------------------------'
javac -d dist/ dist/luna*.java  # Certifique-se de compilar e gerar .class dentro de 'dist/'

echo '--------------------------- Obtaining tree and token --------------------------'
grun luna document -tree -tokens ./ship-calculus/computation.xml
