import pdb

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        print("Method visited: ", method_name)
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def visit_BinaryOp(self, node):
        if node.op == 'PLUS':
            return self.visit(node.left) + self.visit(node.right)
        elif node.op == 'MINUS':
            return self.visit(node.left) - self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

    def interpret(self):
        tree = self.parser.expr()
        pdb.set_trace()
        return self.visit(tree)
