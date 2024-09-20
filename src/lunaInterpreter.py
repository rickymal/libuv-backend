# LunaInterpreter.py

from lunaVisitor import lunaVisitor
from lunaParser import lunaParser

class lunaInterpreter(lunaVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: lunaParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx: lunaParser.StatementContext):
        if ctx.memoryAllocation():
            self.visit(ctx.memoryAllocation())
        elif ctx.memoryDeclaration():
            self.visit(ctx.memoryDeclaration())
        elif ctx.wordWithParameter():
            self.visit(ctx.wordWithParameter())
        elif ctx.returnCall():
            self.visit(ctx.returnCall())
        elif ctx.operationStatement():
            self.visit(ctx.operationStatement())
        elif ctx.typeDeclaration():
            self.visit(ctx.typeDeclaration())
        elif ctx.interfaceDeclaration():
            self.visit(ctx.interfaceDeclaration())
        else:
            print("Declaração não reconhecida.")


    def visitOperationStatement(self, ctx: lunaParser.OperationStatementContext):
        if ctx.ifStatement():
            self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            self.visit(ctx.forStatement())
        elif ctx.breakStatement():
            self.visit(ctx.breakStatement())
        elif ctx.continueStatement():
            self.visit(ctx.continueStatement())
        else:
            print("Operação não reconhecida.")

    def visitWordWithParameter(self, ctx: lunaParser.WordWithParameterContext):
        function_name = ctx.WORD().getText()
        if function_name == 'print':
            args = []
            if ctx.expression():
                for expr in ctx.expression():
                    value = self.visit(expr)
                    args.append(value)
            print(*args)
        else:
            print(f"Função '{function_name}' não implementada.")

    def visitExpression(self, ctx: lunaParser.ExpressionContext):
        if len(ctx.expression()) == 2:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.getChild(1).getText()
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            else:
                print(f"Operador '{operator}' não implementado.")
        else:
            return self.visit(ctx.primaryExpression())

    def visitPrimaryExpression(self, ctx: lunaParser.PrimaryExpressionContext):
        if len(ctx.primaryExpression()) == 2:
            left = self.visit(ctx.primaryExpression(0))
            right = self.visit(ctx.primaryExpression(1))
            operator = ctx.getChild(1).getText()
            if operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            else:
                print(f"Operador '{operator}' não implementado.")
        elif ctx.atom():
            return self.visit(ctx.atom())
        else:
            print("Expressão primária não reconhecida.")

    def visitAtom(self, ctx: lunaParser.AtomContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.STRING():
            text = ctx.STRING().getText()
            # Remover as aspas iniciais e finais
            return text[1:-1]
        elif ctx.WORD():
            var_name = ctx.WORD().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                print(f"Variável '{var_name}' não definida.")
                return None
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            print("Átomo não reconhecido.")

    def visitMemoryAllocation(self, ctx: lunaParser.MemoryAllocationContext):
        var_name = ctx.WORD().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitMemoryDeclaration(self, ctx: lunaParser.MemoryDeclarationContext):
        var_name = ctx.WORD().getText()
        self.variables[var_name] = None


    def visitIfStatement(self, ctx: lunaParser.IfStatementContext):
        condition = self.visit(ctx.conditionExpression())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.block(1):
            self.visit(ctx.block(2))


    def visitConditionExpression(self, ctx: lunaParser.ConditionExpressionContext):
        left = self.visit(ctx.expression(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.expression(1))
        if operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '<=':
            return left <= right
        elif operator == '>=':
            return left >= right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        else:
            print(f"Operador de condição '{operator}' não implementado.")
            return False
        
    def visitBlock(self, ctx: lunaParser.BlockContext):
        for statement in ctx.statement():
            self.visit(statement)


