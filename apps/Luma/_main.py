# Cria o contexto raiz para o parser chamado 'root'.
# Este contexto irá conter todos os parsers para diferentes tokens e padrões.
# PrototypeContext simula o conceito de protótipo como no JavaScript.
# Possui métodos como 'chain_new_context' para criar um novo contexto com acesso a todas as variáveis do contexto pai,
# mas o pai não vê as variáveis do contexto filho.
# Também possui métodos 'set' e 'get' para armazenar e recuperar valores.
# Isso é importante para atribuir exclusividade aos Finders, permitindo criar um contexto filho
# onde um padrão pode aproveitar a exclusividade, garantindo melhor consistência na geração do parser.
# O parâmetro 'name' é apenas para identificação (útil para depuração).

# from apps.Luma.ast import ClassicInputStream, EndOfFileFinder, LiteralFinder, PatternFinder, PrototypeContext, RegexFinder

from dataclasses import dataclass
from lib.ast import EndOfFileFinder, InputDeliver, LiteralFinder, PatternFinder, Personality, PrototypeContext, RegexFinder, YAMLExporter

ctx_root = PrototypeContext(name='root')




# LiteralFinder é um objeto usado para buscar ocorrências exatas de padrões.

# Define parsers literais para vários símbolos.
open_bracket = LiteralFinder(pattern='<', contexts=(ctx_root,))
close_bracket = LiteralFinder(pattern='>', contexts=(ctx_root,))
slash = LiteralFinder(pattern='/', contexts=(ctx_root,))
equal_sign = LiteralFinder(pattern='=', contexts=(ctx_root,))
colon = LiteralFinder(pattern=':', contexts=(ctx_root,))
open_key = LiteralFinder(pattern='{', contexts=(ctx_root,))
close_key = LiteralFinder(pattern='}', contexts=(ctx_root,))
comma = LiteralFinder(pattern=',', contexts=(ctx_root,))

# Adiciona esses parsers ao contexto raiz com suas respectivas chaves.
ctx_root.set("OPEN_BRACKET", open_bracket)
ctx_root.set("CLOSE_BRACKET", close_bracket)
ctx_root.set("SLASH", slash)
ctx_root.set("EQUAL_SIGN", equal_sign)
ctx_root.set("COLON", colon)
ctx_root.set("OPEN_KEY", open_key)
ctx_root.set("CLOSE_KEY", close_key)
ctx_root.set("COMMA", comma)

# Cria um parser para identificadores usando expressões regulares.
# Um identificador começa com uma letra ou underscore, seguido por qualquer número de letras, dígitos, underscores ou pontos.
# Semelhante ao LiteralFinder, mas usa regex para correspondência de padrões.
# Todos os finders possuem métodos em comum; eles retornam uma lista de dicionários que incluem:
# linha e coluna inicial onde foi encontrado, linha e coluna final e o valor em si.
# Finders também possuem parâmetros opcionais chamados 'dim' (dimensões).
# Imagine que os finders são construídos para criar uma árvore sintática (que será melhor explicada abaixo).
# No entanto, a árvore criada terá uma estrutura flexível de hipergrafo ou hiperarcos (a definir ainda),
# onde não importa onde os nós estejam; podemos conectá-los em qualquer ponto através das dimensões.
# Isso facilita do uso por parte do interpretador.
# Por exemplo, suponha que eu queira que meu interpretador leia apenas Finders de natureza 'statement'.
# Posso criar uma dimensão para especificar ao interpretador que desejo que ele leia apenas os nós na dimensão 'statement'.
# Todos os nós com identificadores estarão facilmente conectados, como se fosse uma dimensão à parte da árvore.
# Podemos ter um nó neto que se conecta diretamente a um nó avô, por exemplo.
# Portanto, temos por 'default' a dimensão física, que é a dimensão com a qual trabalhamos por padrão,
# e podemos adicionar mais dimensões passando uma tupla com as dimensões em um parâmetro chamado 'dim'.
# Basicamente, cada 'finder' é um nó; a construção padrão abaixo conectará os nós na dimensão física,
# que terá o nome 'default', por exemplo.

identifier_finder = RegexFinder(pattern=r'[a-zA-Z_][a-zA-Z0-9_\.]*', contexts = (ctx_root,))

# Adiciona o 'identifier_finder' ao contexto raiz com a chave 'A_IDENTIFIER'.
ctx_root.set("A_IDENTIFIER", identifier_finder)

# Cria um parser para literais de string delimitados por aspas duplas, suportando caracteres escapados.
# O parâmetro 'dim' especifica que este finder pertence à dimensão 'uma_dimensão'.
# Neste caso específico, foi adicionado apenas para exemplificar o conceito de dimensão.
string_finder = RegexFinder(pattern=r'"(?:\\.|[^"\\])*"', dim=("uma_dimensão",), contexts = (ctx_root,))

# Adiciona o 'string_finder' ao contexto raiz com a chave 'STRING'.
ctx_root.set("STRING", string_finder)

# Define 'B_IDENTIFIER' como um padrão que corresponde a 'LIST', 'OBJECT' ou 'A_IDENTIFIER'.
b_identifier = PatternFinder(pattern="&LIST|&OBJECT|&A_IDENTIFIER", contexts=(ctx_root,))

# Adiciona 'b_identifier' ao contexto raiz.
ctx_root.set("B_IDENTIFIER", b_identifier)

# Define 'LIST' como um padrão para listas delimitadas por colchetes.
# O asterisco indica que pode haver mais de uma ocorrência.
# A interrogação mostra que o finder é opcional; ele pode aparecer ou não.
# O parêntese faz com que os comandos de asterisco e interrogação sejam aplicados ao conjunto de finders dentro do parentese
# neste caso COMMA e B_IDENTIFIER.
list_identifier = PatternFinder(pattern="&OPEN_BRACKET &B_IDENTIFIER (&COMMA &B_IDENTIFIER)*? &CLOSE_BRACKET", contexts=(ctx_root,))

# Adiciona 'list_identifier' ao contexto raiz sob a chave 'LIST'.
ctx_root.set("LIST", list_identifier)

# Define 'OBJECT' como um padrão para pares chave-valor delimitados por chaves.
object_pattern = PatternFinder(pattern="&OPEN_KEY (&A_IDENTIFIER &COLON &B_IDENTIFIER)*? &CLOSE_KEY", contexts=(ctx_root,))

# Adiciona 'object_pattern' ao contexto raiz sob a chave 'OBJECT'.
ctx_root.set("OBJECT", object_pattern)

# Cria um 'attribute_parser' que corresponde a uma atribuição de atributo.
# Um atributo consiste em um 'A_IDENTIFIER', seguido por '=' ou ':', e então um 'B_IDENTIFIER'.
attribute_parser = PatternFinder(pattern="&A_IDENTIFIER (&EQUAL_SIGN|&COLON) &B_IDENTIFIER", contexts=(ctx_root,))

# Cria um novo contexto interno como filho de 'ctx_root' para parsing de XML.
# O contexto filho tem acesso a todas as variáveis do contexto pai, mas pode ter suas próprias substituições e seus próprios finders exclusivos.
internal_context_xml = ctx_root.chain_new_context(name='internal')

# Adiciona 'attribute_parser' ao contexto interno com a chave 'ATTRIBUTE'.
internal_context_xml.set("ATTRIBUTE", attribute_parser)

# Define um padrão para múltiplos atributos (zero ou mais 'ATTRIBUTE's).
attributes_pattern = "(&ATTRIBUTE)*"

# Cria um 'attributes_parser' usando o padrão.
attributes_parser = PatternFinder(pattern=attributes_pattern, contexts=(internal_context_xml, ))

# Adiciona 'attributes_parser' ao contexto interno sob a chave 'ATTRIBUTES'.
internal_context_xml.set("ATTRIBUTES", attributes_parser)

# Adiciona um 'EndOfFileFinder' ao contexto raiz para reconhecer o fim da entrada da string ou do stream passado como parâmetro.
ctx_root.set("EOF", EndOfFileFinder(pattern = '', contexts = (ctx_root,)))

# --- Parsing XML ---

# Define 'OPEN_TAG' como um padrão para tags de abertura de XML, possivelmente com atributos.
# Usa o contexto 'internal_context_xml' para fornecer o parsing de atributos.
# Perceba que passamos sempre tuplas de contextos; ou seja, podemos ter mais de um contexto.
# No caso de passarmos o parâmetro neste finder em específico, ele irá utilizar apenas os contextos passados.
# Porém, como 'internal_context_xml' é filho do 'ctx_root', ele terá acesso a todas as declarações de 'ctx_root'.
# Assim que sairmos do finder 'OPEN_TAG', voltaremos a usar o contexto 'ctx_root'.
open_tag = PatternFinder(pattern="&OPEN_BRACKET &B_IDENTIFIER &ATTRIBUTES? &CLOSE_BRACKET", contexts=(internal_context_xml,))

# Adiciona 'open_tag' ao contexto raiz.
ctx_root.set("OPEN_TAG", open_tag)

# Define 'PROGRAM' como um ou mais 'XML_STATEMENT's ou 'REQUIRE_STATEMENT's.
program = PatternFinder(pattern="(&XML_STATEMENT|&REQUIRE_STATEMENT)*", contexts=(ctx_root,))

# Adiciona 'program' ao contexto raiz.
ctx_root.set("PROGRAM", program)

# Define 'CLOSE_TAG' como um padrão para tags de fechamento de XML.
# Aqui temos um exemplo de finder com personalidade (a título de exemplificação).
# As personalidades serão explicadas adiante.

close_tag = PatternFinder(pattern="&OPEN_BRACKET &SLASH &B_IDENTIFIER &CLOSE_BRACKET", personality=Personality.LAZY, contexts=(ctx_root,))

# Adiciona 'close_tag' ao contexto raiz.
ctx_root.set("CLOSE_TAG", close_tag)

# Define 'XML_STATEMENT' como um 'OPEN_TAG' seguido por um 'PROGRAM' e um 'CLOSE_TAG'.
xml_statement = PatternFinder(pattern="&OPEN_TAG &PROGRAM &CLOSE_TAG", contexts=(ctx_root,))

# Adiciona 'xml_statement' ao contexto raiz.
ctx_root.set("XML_STATEMENT", xml_statement)

# Cria um parser para a palavra-chave 'require'.
require_literal = LiteralFinder(pattern="require", contexts=(ctx_root,))

# Adiciona 'require_literal' ao contexto raiz.
ctx_root.set("REQUIRE_LITERAL", require_literal)

# Define 'REQUIRE_STATEMENT' como 'require' seguido por um 'B_IDENTIFIER'.
require_statement = PatternFinder(pattern="&REQUIRE_LITERAL &B_IDENTIFIER", contexts=(ctx_root,))

# Adiciona 'require_statement' ao contexto raiz.
ctx_root.set("REQUIRE_STATEMENT", require_statement)

# Define o parser raiz que irá analisar toda a entrada.
# Ele corresponde a um 'PROGRAM' seguido por 'EOF'.
# O contexto passado é 'ctx_root', então todas as definições estão disponíveis.
root_parser: PatternFinder = PatternFinder(pattern="&PROGRAM &EOF", contexts=(ctx_root,))

"""
Aqui você tem um exemplo onde pode passar o contexto.
Como a nova aplicação iniciará com 'root_parser', isso significa que todo o contexto passado no parâmetro 'context'
estará disponível para todos os filhos, já que este é o nó pai de todos.
"""

# Código de exemplo para analisar.
code = """
<code>
    require Ship
    <wolfram.Math instance=[Ship, Algo] anotherParameter={identifier: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

# Remove espaços em branco iniciais e finais do 'code' e armazena o resultado em 'text'.
text = code.strip()



# Classe responsável por fornecer os dados para o 'root_parser'.
"""
Imagine que o 'root_parser' irá fazer validações com lookahead de tamanho dinâmico para identificar
quais finders deverão ser utilizados na sequência. Ele irá solicitar ao 'input_stream' os dados necessários.
Essa classe e os finders estarão em constante interação para criar a árvore sintática.

É comum que haja indecisão sobre qual finder utilizar, e isso é bem visível no 'PatternFinder'. Exemplos:
Supondo que (&I1 | &I2) seja o ponto de entrada (root): nessa situação, não sabemos ainda qual identificador escolher.
Nesse caso, nossa lógica tem que "desmontar" (provavelmente terá um método interno no 'PatternFinder' chamado 'umount')
até os finders primitivos que são os de regex e os literais, e depois aplicar a lógica de decisão para saber qual
escolher baseado no lookahead de tamanho dinâmico (não há porque se preocupar com otimizaçao por enquanto).

Outro exemplo:
(&I1 | &I2) &I3? &I4* &I5: Nesse caso, I1 ou I2 podem assumir a primeira posição, I3 pode ser opcional (posição 2),
I4 pode aparecer zero ou mais vezes (posição 2 por que o I3 não aparece as vezes ou posição 3), e I5 é obrigatório no final (podendo assumir no mínimo a posição 4 caso não tenha I3 ou adiante). Essas posições que eu falo são posições virtuais, visto que o finde pode ser desmontado em posições menores, então aqui temos posição, que chamaremos de endereço, mas seŕa como se fosse endereço virtual (que nem endereço virtual em memória RAM), o real só saberemos após toda a desmontagem, é como se fosse memória virtual, não igual. 
Nessas situações, a lógica deve ter um sistema de delegação de finders: por exemplo, ao ler o texto a ser parseado
caractere a caractere, podemos ter múltiplas opções (após o 'umount'). Dependendo da personalidade do finder, ele pode:
- Continuar lendo junto com o seguinte (personality.COLLABORATIVE)
- Delegar para o outro finder assim que ele for capaz de ler (personality.LAZY ou personality.DELEGATOR) 
- Ler até não poder mais (personality.BOSSY)
- Outros comportamentos (podem haver outras opções)

Uma das personalidades será o default

"""
transpiler=YAMLExporter()
input_stream=InputDeliver(text = text)


# &PROGRAM &EOF
@dataclass
class Token:
    value: str
    pos: int
    is_optional: bool 
    is_sequential: bool 
    is_grouped: bool 
    is_identifier: bool 
    has_or_operand: bool
    scan: any
    ctx: PrototypeContext


# Identificar os tokens:



node_root = PrototypeContext(name = 'root')
def extrat_base_info(root_parser, pos, node_root):
    lof_tokens = []
    pos = 0
    for value in root_parser.pattern.split(" "):
        is_identifier = value.startswith("&")
        is_optional = "?" in value
        is_sequential = "*" in value
        has_or_operand = "|" in value
        is_grouped = value.startswith("(") and value.endswith(")")
        token = Token(value = value, pos = pos, is_optional = is_optional, is_sequential = is_sequential, is_grouped = is_grouped, has_or_operand = has_or_operand, scan = lambda : print("OI"), is_identifier = is_identifier, ctx=node_root)
        lof_tokens.append(token)
        pos += 1

    return lof_tokens

tokens = extrat_base_info(root_parser, node_root)


for token in lof_tokens:
    if token.is_grouped:
        # se for um grupo ou seja tá entre parentese temos que extrair o conteudo entre parentese
        


# Inicializa o parser com os parâmetros fornecidos.
# Contém o 'root_parser', o 'input_stream' que será da classe 'ASTStreamingText' e o 'transpiler'.
# O 'transpiler' pode ser um interpretador ou um compilador; fica a critério do uso.
# O 'input_stream' e o 'root_parser' estarão em constante interação, onde o 'input_stream' fornece os dados conforme o 'root_parser' solicita.

