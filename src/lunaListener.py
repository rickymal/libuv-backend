# Generated from luna.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lunaParser import lunaParser
else:
    from lunaParser import lunaParser

# This class defines a complete listener for a parse tree produced by lunaParser.
class lunaListener(ParseTreeListener):

    # Enter a parse tree produced by lunaParser#program.
    def enterProgram(self, ctx:lunaParser.ProgramContext):
        pass

    # Exit a parse tree produced by lunaParser#program.
    def exitProgram(self, ctx:lunaParser.ProgramContext):
        pass


    # Enter a parse tree produced by lunaParser#typeModifier.
    def enterTypeModifier(self, ctx:lunaParser.TypeModifierContext):
        pass

    # Exit a parse tree produced by lunaParser#typeModifier.
    def exitTypeModifier(self, ctx:lunaParser.TypeModifierContext):
        pass


    # Enter a parse tree produced by lunaParser#allocatorSize.
    def enterAllocatorSize(self, ctx:lunaParser.AllocatorSizeContext):
        pass

    # Exit a parse tree produced by lunaParser#allocatorSize.
    def exitAllocatorSize(self, ctx:lunaParser.AllocatorSizeContext):
        pass


    # Enter a parse tree produced by lunaParser#elementLiteral.
    def enterElementLiteral(self, ctx:lunaParser.ElementLiteralContext):
        pass

    # Exit a parse tree produced by lunaParser#elementLiteral.
    def exitElementLiteral(self, ctx:lunaParser.ElementLiteralContext):
        pass


    # Enter a parse tree produced by lunaParser#objectLiteral.
    def enterObjectLiteral(self, ctx:lunaParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by lunaParser#objectLiteral.
    def exitObjectLiteral(self, ctx:lunaParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by lunaParser#expression.
    def enterExpression(self, ctx:lunaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by lunaParser#expression.
    def exitExpression(self, ctx:lunaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by lunaParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:lunaParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by lunaParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:lunaParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by lunaParser#atom.
    def enterAtom(self, ctx:lunaParser.AtomContext):
        pass

    # Exit a parse tree produced by lunaParser#atom.
    def exitAtom(self, ctx:lunaParser.AtomContext):
        pass


    # Enter a parse tree produced by lunaParser#memoryAllocation.
    def enterMemoryAllocation(self, ctx:lunaParser.MemoryAllocationContext):
        pass

    # Exit a parse tree produced by lunaParser#memoryAllocation.
    def exitMemoryAllocation(self, ctx:lunaParser.MemoryAllocationContext):
        pass


    # Enter a parse tree produced by lunaParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:lunaParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by lunaParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:lunaParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by lunaParser#anonymysFunctionDeclaration.
    def enterAnonymysFunctionDeclaration(self, ctx:lunaParser.AnonymysFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by lunaParser#anonymysFunctionDeclaration.
    def exitAnonymysFunctionDeclaration(self, ctx:lunaParser.AnonymysFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by lunaParser#wordWithParameter.
    def enterWordWithParameter(self, ctx:lunaParser.WordWithParameterContext):
        pass

    # Exit a parse tree produced by lunaParser#wordWithParameter.
    def exitWordWithParameter(self, ctx:lunaParser.WordWithParameterContext):
        pass


    # Enter a parse tree produced by lunaParser#conditionExpression.
    def enterConditionExpression(self, ctx:lunaParser.ConditionExpressionContext):
        pass

    # Exit a parse tree produced by lunaParser#conditionExpression.
    def exitConditionExpression(self, ctx:lunaParser.ConditionExpressionContext):
        pass


    # Enter a parse tree produced by lunaParser#ifStatement.
    def enterIfStatement(self, ctx:lunaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by lunaParser#ifStatement.
    def exitIfStatement(self, ctx:lunaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by lunaParser#whileStatement.
    def enterWhileStatement(self, ctx:lunaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by lunaParser#whileStatement.
    def exitWhileStatement(self, ctx:lunaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by lunaParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:lunaParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by lunaParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:lunaParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by lunaParser#forStatement.
    def enterForStatement(self, ctx:lunaParser.ForStatementContext):
        pass

    # Exit a parse tree produced by lunaParser#forStatement.
    def exitForStatement(self, ctx:lunaParser.ForStatementContext):
        pass


    # Enter a parse tree produced by lunaParser#returnCall.
    def enterReturnCall(self, ctx:lunaParser.ReturnCallContext):
        pass

    # Exit a parse tree produced by lunaParser#returnCall.
    def exitReturnCall(self, ctx:lunaParser.ReturnCallContext):
        pass


    # Enter a parse tree produced by lunaParser#breakStatement.
    def enterBreakStatement(self, ctx:lunaParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by lunaParser#breakStatement.
    def exitBreakStatement(self, ctx:lunaParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by lunaParser#continueStatement.
    def enterContinueStatement(self, ctx:lunaParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by lunaParser#continueStatement.
    def exitContinueStatement(self, ctx:lunaParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by lunaParser#parameters.
    def enterParameters(self, ctx:lunaParser.ParametersContext):
        pass

    # Exit a parse tree produced by lunaParser#parameters.
    def exitParameters(self, ctx:lunaParser.ParametersContext):
        pass


    # Enter a parse tree produced by lunaParser#parameter.
    def enterParameter(self, ctx:lunaParser.ParameterContext):
        pass

    # Exit a parse tree produced by lunaParser#parameter.
    def exitParameter(self, ctx:lunaParser.ParameterContext):
        pass


    # Enter a parse tree produced by lunaParser#modifier.
    def enterModifier(self, ctx:lunaParser.ModifierContext):
        pass

    # Exit a parse tree produced by lunaParser#modifier.
    def exitModifier(self, ctx:lunaParser.ModifierContext):
        pass


    # Enter a parse tree produced by lunaParser#typeSpec.
    def enterTypeSpec(self, ctx:lunaParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by lunaParser#typeSpec.
    def exitTypeSpec(self, ctx:lunaParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by lunaParser#typeParameters.
    def enterTypeParameters(self, ctx:lunaParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by lunaParser#typeParameters.
    def exitTypeParameters(self, ctx:lunaParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by lunaParser#block.
    def enterBlock(self, ctx:lunaParser.BlockContext):
        pass

    # Exit a parse tree produced by lunaParser#block.
    def exitBlock(self, ctx:lunaParser.BlockContext):
        pass


    # Enter a parse tree produced by lunaParser#operationStatement.
    def enterOperationStatement(self, ctx:lunaParser.OperationStatementContext):
        pass

    # Exit a parse tree produced by lunaParser#operationStatement.
    def exitOperationStatement(self, ctx:lunaParser.OperationStatementContext):
        pass


    # Enter a parse tree produced by lunaParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:lunaParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by lunaParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:lunaParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by lunaParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:lunaParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by lunaParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:lunaParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by lunaParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:lunaParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by lunaParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:lunaParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by lunaParser#memoryDeclaration.
    def enterMemoryDeclaration(self, ctx:lunaParser.MemoryDeclarationContext):
        pass

    # Exit a parse tree produced by lunaParser#memoryDeclaration.
    def exitMemoryDeclaration(self, ctx:lunaParser.MemoryDeclarationContext):
        pass


    # Enter a parse tree produced by lunaParser#statement.
    def enterStatement(self, ctx:lunaParser.StatementContext):
        pass

    # Exit a parse tree produced by lunaParser#statement.
    def exitStatement(self, ctx:lunaParser.StatementContext):
        pass



del lunaParser