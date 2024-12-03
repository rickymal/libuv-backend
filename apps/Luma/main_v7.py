
# Supondo que a classe Grammar e os métodos associados estejam implementados adequadamente.

# Definição da gramática
grammar = Grammar(name='custom_xml')

# Correção na definição de extras para ignorar espaços em branco
grammar.extra([r'\s'])


glr = GeneralizedLrParsing(max_look_ahead = 1) # Um parsing padrão 
hmb = DirectedGraph() # Esse é um que eu inventei, presente nas versões antigas dessa lib 


# Definição da regra principal
rg = grammar.rule(name="xml_rule", parser = glr) # O sistema apenas olhará o token atual e umn a frente (0 = atual e 1 = o seguinte)


from dataclasses import dataclass 

@dataclass
class Priority:
    pass


# Definição de tokens básicos
a_identifier = lambda: rg.pattern('a_identifier', r'[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*')
open_tag = rg.literal(''<', Priority(precedence = 2)) # Determina que em classo de conflito, open_tag sempre terá prioridade
slash = rg.literal('/')
close_tag = rg.literal('>')
equal = rg.literal('=')
colon = rg.literal(':')
comma = rg.literal(',')
open_brace = rg.literal('{')
close_brace = rg.literal('}')
open_bracket = rg.literal('open_bracket', '[')
close_bracket = rg.literal('close_bracket', ']')

# Correção na expressão regular de 'a_identifier'

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
