import pdb

class ASTNode:
    pass

class BinaryOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def eat(self, token_type):
        pdb.set_trace()
        if self.current_token.type == token_type:
            self.current_token = self.tokens[self.position]
            self.position += 1
        else:
            raise Exception(f'Unexpected token: {self.current_token.type}, expected: {token_type}')

    def factor(self):
        token = self.current_token
        if token.type == 'INTEGER':
            self.eat('INTEGER')
            return Num(token.value)
        raise Exception('Syntax error')

    # generate the tree
    def expr(self):
        
        node = self.factor()
        self.eat('INTEGER')

        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')

            node = BinaryOp(left=node, op=token.type, right=self.factor())

        return node
