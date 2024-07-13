class FunctionCall(ASTNode):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

class VariableDeclaration(ASTNode):
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class ConstantDeclaration(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class NativeFunction(ASTNode):
    # A Razão para argumentos esse ASTNodes é porque precisamos considerar 
    def __init__(self, name : str, arguments : list[ASTNode]):
        self.name = name
        self.arguments = arguments


    def call(self, function):
        self.function = function

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def parse(self):
        nodes = []
        while self.current_token is not None:
            if self.current_token.type in ['VAR', 'CONST']:
                nodes.append(self.parse_declaration())
            elif self.current_token.type == "NATIVE":
                pass
            elif self.current_token.type == 'PRINT':
                nodes.append(self.parse_print_statement())
            else:
                # Handle other statements or raise an error
                pass
            if self.current_token:
                self.eat(self.current_token.type)  # Move to the next token
        return nodes

    def parse_declaration(self):
        # Add detailed parsing logic for variable and constant declarations
        pass

    def parse_print_statement(self):
        # Add parsing logic for print statements
        pass

    # Existing methods like `eat`, `factor`, etc.

