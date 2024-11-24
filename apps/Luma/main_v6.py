from lib_v6 import Grammar


# Definição da gramática
grammar = Grammar(name='custom_xml')

# Correção na definição de extras para ignorar espaços em branco
grammar.extra([r'\s'])

# Definição da regra principal
rg = grammar.rule(name="xml_rule")

# Definição de tokens básicos
open_tag = rg.literal('open_tag', '<')
slash = rg.literal('slash', '/')
close_tag = rg.literal('close_tag', '>')
equal = rg.literal('equal', '=')
colon = rg.literal('colon', ':')
comma = rg.literal('comma', ',')
open_brace = rg.literal('open_brace', '{')
close_brace = rg.literal('close_brace', '}')
open_bracket = rg.literal('open_bracket', '[')
close_bracket = rg.literal('close_bracket', ']')

# Correção na expressão regular de 'a_identifier'
a_identifier = rg.pattern('a_identifier', r'[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*')

# Definição de 'pair' para objetos
pair = rg.and_(
    a_identifier,
    colon,
    a_identifier,
)

# Definição de 'object_rg' para objetos
object_rg = rg.and_(
    open_brace,
    pair,
    rg.repeat(
        rg.and_(
            comma,
            pair
        )
    ),
    close_brace,
)

# Definição de 'array_rg' para arrays
array_rg = rg.and_(
    open_bracket,
    a_identifier,
    rg.repeat(
        rg.and_(
            comma,
            a_identifier
        )
    ),
    close_bracket,
)

# Para recursão
def element():
    return rg.and_(
        open_tag,
        a_identifier,
        rg.repeat(
            attribute
        ),
        close_tag,
        rg.repeat(
            rg.lazy(element)  # Uso de avaliação preguiçosa para recursão
        ),
        rg.optional(
            rg.and_(
                open_tag,
                slash,
                a_identifier,
                close_tag,
            )
        )
    )

# Definição de 'value' com suporte a elementos aninhados
value = rg.or_(
    array_rg,
    object_rg,
    a_identifier,
    rg.lazy(element),  # Avaliação preguiçosa para permitir recursão
)

# Definição de 'attribute'
attribute = rg.and_(
    a_identifier,
    equal,
    value
)

# Definição do código a ser analisado
code = "<wolfram.Math instance=[Ship, Algo] anotherParameter={name: Henrique} thirdParameter=<anotherXmlThing></anotherXmlThing>>"

# Execução da gramática
parsed_result = element().run_as_document(code)

# Exibição do resultado (opcional)
print(parsed_result)

