'''
    O conceito
    De modificador na verdade é bem simples, significa que serão metadados guardados no token principal
    todo nodo será composto de um identificador, modificadores (geradores de metadados) e acessares que 
    são parametros do nodo.

    A ideia é que o token identificador da ação execute são ação também (e opcionalmente) baseado nos modificadores. Modificadores podem ser identificadores.

    Um ponto importante é que os tokens que já criavos com os identificadore permanecerão, eles só não hernarão diretamente de ASTNode mas sim de outras classe que representam os conceitos acima (ou em vez de herança podemos usar composição também, não vejo problema).
'''

# Declaração de um tipo nativo 'i32' com o modificador 'native'
Token(NATIVE, 'native')
Token(TYPE, 'type')
Token(IDENTIFIER, 'i32')
Token(END_COMMNAND, ';')

# Declaração de uma função nativa 'type' que retorna uma string
Token(NATIVE, 'native')
Token(IDENTIFIER, 'func')
Token(IDENTIFIER, 'type')
Token(OPEN_BRACKET, '(')
Token(IDENTIFIER, 'data')
Token(IDENTIFIER, 'i32')
Token(CLOSE_BRACKET, ')')
Token(IDENTIFIER, 'string')
Token(END_COMMNAND, ';')

# Declaração de uma função nativa 'print' que aceita qualquer tipo imprimível
Token(NATIVE, 'native')
Token(IDENTIFIER, 'func')
Token(IDENTIFIER, 'print')
Token(OPEN_BRACKET, '(')
Token(IDENTIFIER, 'data')
Token(IDENTIFIER, 'IPrintable')
Token(CLOSE_BRACKET, ')')
Token(IDENTIFIER, 'void')
Token(END_COMMNAND, ';')

# Declaração explícita de variável com tipo 'i32'
Token(VAR, 'var')
Token(IDENTIFIER, 'x1')
Token(IDENTIFIER, 'i32')
Token(EQUAL, '=')
Token(INTEGER, 23)

# Declaração implícita de variável com inferência de tipo
Token(VAR, 'var')
Token(IDENTIFIER, 'x2')
Token(EQUAL, '=')
Token(INTEGER, 23)

# Declaração de constante
Token(CONST, 'const')
Token(IDENTIFIER, 'x3')
Token(EQUAL, '=')
Token(INTEGER, 32)

# Chamadas de função 'print' em diversas formas
Token(PRINT, 'print')
Token(IDENTIFIER, 'x1')

Token(IDENTIFIER, 'x2')
Token(PUNCTUATION, '.')
Token(PRINT, 'print')
Token(OPEN_BRACKET, '(')
Token(CLOSE_BRACKET, ')')

Token(PRINT, 'print')
Token(OPEN_BRACKET, '(')
Token(IDENTIFIER, 'x2')
Token(CLOSE_BRACKET, ')')

Token(PRINT, 'print')
Token(IDENTIFIER, 'x3')

Token(IDENTIFIER, 'x3')
Token(PUNCTUATION, '.')
Token(TYPE, 'type')
Token(OPEN_BRACKET, '(')
Token(CLOSE_BRACKET, ')')

Token(PRINT, 'print')
Token(TYPE, 'type')
Token(OPEN_BRACKET, '(')
Token(IDENTIFIER, 'x3')
Token(CLOSE_BRACKET, ')')
