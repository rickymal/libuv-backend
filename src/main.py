import sys
import os 
# Calcular o caminho absoluto para o diretório raiz
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adicionar o diretório raiz ao sys.path
sys.path.insert(0, ROOT_DIR)

# Definição dos parsers básicos
from lib.finders import ForwardFinder, ListParser, LiteralFinder, ObjectParser, PatternParser, PrototypeContext, RegexFinder, extract


ctx_root = PrototypeContext(name='root')

# Parsers literais
open_bracket = LiteralFinder(pattern='<', name='open_bracket')
close_bracket = LiteralFinder(pattern='>', name='close_bracket')
slash = LiteralFinder(pattern='/', name='slash')
equal_sign = LiteralFinder(pattern='=', name='equal_sign')

ctx_root.set("PS:OPEN_BRACKET", open_bracket)
ctx_root.set("PS:CLOSE_BRACKET", close_bracket)
ctx_root.set("PS:SLASH", slash)
ctx_root.set("PS:EQUAL_SIGN", equal_sign)

# Parsers para identificadores e valores
identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_\.]*'
identifier_finder = RegexFinder(pattern=identifier_pattern, name='identifier')
ctx_root.set("PS:IDENTIFIER", identifier_finder)

# Parser para strings entre aspas duplas
string_pattern = r'"(?:\\.|[^"\\])*"'
string_finder = RegexFinder(pattern=string_pattern, name='string')
ctx_root.set("PS:STRING", string_finder)

list_parser = ListParser()
ctx_root.set("PS:LIST", list_parser)

object_parser = ObjectParser()
ctx_root.set("PS:OBJECT", object_parser)

# Criar o ForwardFinder para TAG
tag_placeholder = ForwardFinder(name='tag')
ctx_root.set("PS:TAG", tag_placeholder)

# Parser para valores (pode ser um identificador, string, lista, objeto ou tag)
value_pattern = "&STRING | &LIST | &OBJECT | &IDENTIFIER | &TAG"
value_parser = PatternParser(value_pattern, ctx_root)
value = value_parser.parse()
value.name = 'value'
ctx_root.set("PS:VALUE", value)

# Definir o LiteralFinder para ':'
colon = LiteralFinder(pattern=':', name='colon')
ctx_root.set("PS:COLON", colon)

# Parser para atributo que aceita '=' ou ':'
attribute_pattern = "&IDENTIFIER (&EQUAL_SIGN | &COLON) &VALUE"
attribute_parser = PatternParser(attribute_pattern, ctx_root)
attribute = attribute_parser.parse()
attribute.name = 'attribute'
ctx_root.set("PS:ATTRIBUTE", attribute)


attribute_parser = PatternParser(attribute_pattern, ctx_root)
attribute = attribute_parser.parse()
attribute.name = 'attribute'
ctx_root.set("PS:ATTRIBUTE", attribute)

# Parser para atributos múltiplos
attributes_pattern = "(&ATTRIBUTE)*"
attributes_parser = PatternParser(attributes_pattern, ctx_root)
attributes = attributes_parser.parse()
attributes.name = 'attributes'
ctx_root.set("PS:ATTRIBUTES", attributes)

# Parser para tag aberta (com atributos opcionais)
open_tag_pattern = "&OPEN_BRACKET &IDENTIFIER &ATTRIBUTES &CLOSE_BRACKET"
open_tag_parser = PatternParser(open_tag_pattern, ctx_root)
open_tag = open_tag_parser.parse()
open_tag.name = 'open_tag'
ctx_root.set("PS:OPEN_TAG", open_tag)

# Parser para tag fechada
close_tag_pattern = "&OPEN_BRACKET &SLASH &IDENTIFIER &CLOSE_BRACKET"
close_tag_parser = PatternParser(close_tag_pattern, ctx_root)
close_tag = close_tag_parser.parse()
close_tag.name = 'close_tag'
ctx_root.set("PS:CLOSE_TAG", close_tag)

# Parser para texto
text_pattern = r'[^<]+'
text_finder = RegexFinder(pattern=text_pattern, name='text')
ctx_root.set("PS:TEXT", text_finder)

# Parser para elementos dentro de uma tag (pode ser outra tag ou texto)
element_pattern = "&TAG | &TEXT"
element_parser = PatternParser(element_pattern, ctx_root)
element = element_parser.parse()
element.name = 'element'
ctx_root.set("PS:ELEMENT", element)

# Parser para o corpo de uma tag (zero ou mais elementos)
content_pattern = "(&ELEMENT)*"
content_parser = PatternParser(content_pattern, ctx_root)
content = content_parser.parse()
content.name = 'content'
ctx_root.set("PS:CONTENT", content)

# Parser para tag completa
tag_pattern = "&OPEN_TAG &CONTENT &CLOSE_TAG"
tag_parser = PatternParser(tag_pattern, ctx_root)
tag = tag_parser.parse()
tag.name = 'tag'
ctx_root.set("PS:TAG", tag)

# Atualizar o ForwardFinder
tag_placeholder.set_target(tag)

# Parser raiz
root_pattern = "&TAG"
root_parser = PatternParser(root_pattern, ctx_root)
root = root_parser.parse()
root.name = 'root'
root.on_find_token = [extract]

# Código de exemplo
code = """
<code>
    require Ship
    <wolfram.Math instance=[Ship, Algo] anotherParameter={identifier: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

# Remover espaços em branco iniciais e finais
text = code.strip()

# Scan do texto
result_token, pos = root.scan(text, context=ctx_root, pos=0)

if result_token:
    # print("Parsing bem-sucedido. O token resultante é:")
    print(result_token.to_yaml(indent=0))

    # # Gerar a representação Mermaid
    # mermaid_lines, _ = result_token.to_mermaid()
    # mermaid_output = "graph TD;\n" + "\n".join(mermaid_lines)
    # print("\nRepresentação Mermaid:\n")
    # print(mermaid_output)
else:
    print("Parsing falhou.")

