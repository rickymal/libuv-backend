# Generated from luna.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lunaParser import lunaParser
else:
    from lunaParser import lunaParser

# This class defines a complete generic visitor for a parse tree produced by lunaParser.

class lunaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lunaParser#program.
    def visitProgram(self, ctx:lunaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#typeModifier.
    def visitTypeModifier(self, ctx:lunaParser.TypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#allocatorSize.
    def visitAllocatorSize(self, ctx:lunaParser.AllocatorSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#elementLiteral.
    def visitElementLiteral(self, ctx:lunaParser.ElementLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#objectLiteral.
    def visitObjectLiteral(self, ctx:lunaParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#expression.
    def visitExpression(self, ctx:lunaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:lunaParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#atom.
    def visitAtom(self, ctx:lunaParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#memoryAllocation.
    def visitMemoryAllocation(self, ctx:lunaParser.MemoryAllocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:lunaParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#anonymysFunctionDeclaration.
    def visitAnonymysFunctionDeclaration(self, ctx:lunaParser.AnonymysFunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#wordWithParameter.
    def visitWordWithParameter(self, ctx:lunaParser.WordWithParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#conditionExpression.
    def visitConditionExpression(self, ctx:lunaParser.ConditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#ifStatement.
    def visitIfStatement(self, ctx:lunaParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#whileStatement.
    def visitWhileStatement(self, ctx:lunaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:lunaParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#forStatement.
    def visitForStatement(self, ctx:lunaParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#returnCall.
    def visitReturnCall(self, ctx:lunaParser.ReturnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#breakStatement.
    def visitBreakStatement(self, ctx:lunaParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#continueStatement.
    def visitContinueStatement(self, ctx:lunaParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#parameters.
    def visitParameters(self, ctx:lunaParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#parameter.
    def visitParameter(self, ctx:lunaParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#modifier.
    def visitModifier(self, ctx:lunaParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#typeSpec.
    def visitTypeSpec(self, ctx:lunaParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#typeParameters.
    def visitTypeParameters(self, ctx:lunaParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#block.
    def visitBlock(self, ctx:lunaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#operationStatement.
    def visitOperationStatement(self, ctx:lunaParser.OperationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:lunaParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:lunaParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:lunaParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#memoryDeclaration.
    def visitMemoryDeclaration(self, ctx:lunaParser.MemoryDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lunaParser#statement.
    def visitStatement(self, ctx:lunaParser.StatementContext):
        return self.visitChildren(ctx)



del lunaParser