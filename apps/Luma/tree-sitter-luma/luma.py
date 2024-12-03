from tree_sitter import Language, Parser
import pdb 
from bindings.python import tree_sitter_luma
from tree_sitter import Parser, Language



luma_language = Language(tree_sitter_luma.language())


parser = Parser(luma_language)

# Código fonte da sua linguagem
source_code = b"""
package main
<wolfram instance=[Ship, Algo] anotherParameter={name: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    <math>
      resistance(v) = a1 * v ** 2 where v <= v_critical;
      resistance(v) = a2 * v + a3 otherwise;
    </math>
</wolfram>
"""
pdb.set_trace()
# Analisar o código
tree = parser.parse(source_code)

tree.root_node.child.__name__

# Exibir a árvore sintática
print(tree.root_node.sexp())
