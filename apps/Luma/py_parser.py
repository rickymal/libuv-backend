from pyparsing import Word, Literal, nums, infixNotation, opAssoc

# Definindo os elementos básicos
integer = Word(nums)
plus = Literal("+")
minus = Literal("-")

# Criando a gramática
expr = integer + (plus | minus) + integer

# Testando a gramática
result = expr.parseString("3 + 4")
print(result)  # Saída: ['3', '+', '4']
