// Generated from luna.g4 by ANTLR 4.13.1

import {ParseTreeListener} from "antlr4";


import { ProgramContext } from "./lunaParser";
import { TypeModifierContext } from "./lunaParser";
import { AllocatorSizeContext } from "./lunaParser";
import { ExpressionContext } from "./lunaParser";
import { PrimaryExpressionContext } from "./lunaParser";
import { AtomContext } from "./lunaParser";
import { MemoryAllocationContext } from "./lunaParser";
import { FunctionDeclarationContext } from "./lunaParser";
import { AnonymysFunctionDeclarationContext } from "./lunaParser";
import { WordWithParameterContext } from "./lunaParser";
import { ConditionExpressionContext } from "./lunaParser";
import { IfStatementContext } from "./lunaParser";
import { WhileStatementContext } from "./lunaParser";
import { AssignmentStatementContext } from "./lunaParser";
import { ForStatementContext } from "./lunaParser";
import { ReturnCallContext } from "./lunaParser";
import { BreakStatementContext } from "./lunaParser";
import { ContinueStatementContext } from "./lunaParser";
import { ParametersContext } from "./lunaParser";
import { ParameterContext } from "./lunaParser";
import { ModifierContext } from "./lunaParser";
import { TypeContext } from "./lunaParser";
import { TypeParametersContext } from "./lunaParser";
import { BlockContext } from "./lunaParser";
import { OperationStatementContext } from "./lunaParser";
import { StatementContext } from "./lunaParser";


/**
 * This interface defines a complete listener for a parse tree produced by
 * `lunaParser`.
 */
export default class lunaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by `lunaParser.program`.
	 * @param ctx the parse tree
	 */
	enterProgram?: (ctx: ProgramContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.program`.
	 * @param ctx the parse tree
	 */
	exitProgram?: (ctx: ProgramContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.typeModifier`.
	 * @param ctx the parse tree
	 */
	enterTypeModifier?: (ctx: TypeModifierContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.typeModifier`.
	 * @param ctx the parse tree
	 */
	exitTypeModifier?: (ctx: TypeModifierContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.allocatorSize`.
	 * @param ctx the parse tree
	 */
	enterAllocatorSize?: (ctx: AllocatorSizeContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.allocatorSize`.
	 * @param ctx the parse tree
	 */
	exitAllocatorSize?: (ctx: AllocatorSizeContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.expression`.
	 * @param ctx the parse tree
	 */
	enterExpression?: (ctx: ExpressionContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.expression`.
	 * @param ctx the parse tree
	 */
	exitExpression?: (ctx: ExpressionContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.primaryExpression`.
	 * @param ctx the parse tree
	 */
	enterPrimaryExpression?: (ctx: PrimaryExpressionContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.primaryExpression`.
	 * @param ctx the parse tree
	 */
	exitPrimaryExpression?: (ctx: PrimaryExpressionContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.atom`.
	 * @param ctx the parse tree
	 */
	enterAtom?: (ctx: AtomContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.atom`.
	 * @param ctx the parse tree
	 */
	exitAtom?: (ctx: AtomContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.memoryAllocation`.
	 * @param ctx the parse tree
	 */
	enterMemoryAllocation?: (ctx: MemoryAllocationContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.memoryAllocation`.
	 * @param ctx the parse tree
	 */
	exitMemoryAllocation?: (ctx: MemoryAllocationContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.functionDeclaration`.
	 * @param ctx the parse tree
	 */
	enterFunctionDeclaration?: (ctx: FunctionDeclarationContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.functionDeclaration`.
	 * @param ctx the parse tree
	 */
	exitFunctionDeclaration?: (ctx: FunctionDeclarationContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.anonymysFunctionDeclaration`.
	 * @param ctx the parse tree
	 */
	enterAnonymysFunctionDeclaration?: (ctx: AnonymysFunctionDeclarationContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.anonymysFunctionDeclaration`.
	 * @param ctx the parse tree
	 */
	exitAnonymysFunctionDeclaration?: (ctx: AnonymysFunctionDeclarationContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.wordWithParameter`.
	 * @param ctx the parse tree
	 */
	enterWordWithParameter?: (ctx: WordWithParameterContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.wordWithParameter`.
	 * @param ctx the parse tree
	 */
	exitWordWithParameter?: (ctx: WordWithParameterContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.conditionExpression`.
	 * @param ctx the parse tree
	 */
	enterConditionExpression?: (ctx: ConditionExpressionContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.conditionExpression`.
	 * @param ctx the parse tree
	 */
	exitConditionExpression?: (ctx: ConditionExpressionContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.ifStatement`.
	 * @param ctx the parse tree
	 */
	enterIfStatement?: (ctx: IfStatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.ifStatement`.
	 * @param ctx the parse tree
	 */
	exitIfStatement?: (ctx: IfStatementContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.whileStatement`.
	 * @param ctx the parse tree
	 */
	enterWhileStatement?: (ctx: WhileStatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.whileStatement`.
	 * @param ctx the parse tree
	 */
	exitWhileStatement?: (ctx: WhileStatementContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.assignmentStatement`.
	 * @param ctx the parse tree
	 */
	enterAssignmentStatement?: (ctx: AssignmentStatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.assignmentStatement`.
	 * @param ctx the parse tree
	 */
	exitAssignmentStatement?: (ctx: AssignmentStatementContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.forStatement`.
	 * @param ctx the parse tree
	 */
	enterForStatement?: (ctx: ForStatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.forStatement`.
	 * @param ctx the parse tree
	 */
	exitForStatement?: (ctx: ForStatementContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.returnCall`.
	 * @param ctx the parse tree
	 */
	enterReturnCall?: (ctx: ReturnCallContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.returnCall`.
	 * @param ctx the parse tree
	 */
	exitReturnCall?: (ctx: ReturnCallContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.breakStatement`.
	 * @param ctx the parse tree
	 */
	enterBreakStatement?: (ctx: BreakStatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.breakStatement`.
	 * @param ctx the parse tree
	 */
	exitBreakStatement?: (ctx: BreakStatementContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.continueStatement`.
	 * @param ctx the parse tree
	 */
	enterContinueStatement?: (ctx: ContinueStatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.continueStatement`.
	 * @param ctx the parse tree
	 */
	exitContinueStatement?: (ctx: ContinueStatementContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.parameters`.
	 * @param ctx the parse tree
	 */
	enterParameters?: (ctx: ParametersContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.parameters`.
	 * @param ctx the parse tree
	 */
	exitParameters?: (ctx: ParametersContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.parameter`.
	 * @param ctx the parse tree
	 */
	enterParameter?: (ctx: ParameterContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.parameter`.
	 * @param ctx the parse tree
	 */
	exitParameter?: (ctx: ParameterContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.modifier`.
	 * @param ctx the parse tree
	 */
	enterModifier?: (ctx: ModifierContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.modifier`.
	 * @param ctx the parse tree
	 */
	exitModifier?: (ctx: ModifierContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.type`.
	 * @param ctx the parse tree
	 */
	enterType?: (ctx: TypeContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.type`.
	 * @param ctx the parse tree
	 */
	exitType?: (ctx: TypeContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.typeParameters`.
	 * @param ctx the parse tree
	 */
	enterTypeParameters?: (ctx: TypeParametersContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.typeParameters`.
	 * @param ctx the parse tree
	 */
	exitTypeParameters?: (ctx: TypeParametersContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.block`.
	 * @param ctx the parse tree
	 */
	enterBlock?: (ctx: BlockContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.block`.
	 * @param ctx the parse tree
	 */
	exitBlock?: (ctx: BlockContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.operationStatement`.
	 * @param ctx the parse tree
	 */
	enterOperationStatement?: (ctx: OperationStatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.operationStatement`.
	 * @param ctx the parse tree
	 */
	exitOperationStatement?: (ctx: OperationStatementContext) => void;
	/**
	 * Enter a parse tree produced by `lunaParser.statement`.
	 * @param ctx the parse tree
	 */
	enterStatement?: (ctx: StatementContext) => void;
	/**
	 * Exit a parse tree produced by `lunaParser.statement`.
	 * @param ctx the parse tree
	 */
	exitStatement?: (ctx: StatementContext) => void;
}

