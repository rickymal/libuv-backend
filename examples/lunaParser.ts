// Generated from luna.g4 by ANTLR 4.13.1
// noinspection ES6UnusedImports,JSUnusedGlobalSymbols,JSUnusedLocalSymbols

import {
	ATN,
	ATNDeserializer, DecisionState, DFA, FailedPredicateException,
	RecognitionException, NoViableAltException, BailErrorStrategy,
	Parser, ParserATNSimulator,
	RuleContext, ParserRuleContext, PredictionMode, PredictionContextCache,
	TerminalNode, RuleNode,
	Token, TokenStream,
	Interval, IntervalSet
} from 'antlr4';
import lunaListener from "./lunaListener.js";
// for running tests with parameters, TODO: discuss strategy for typed parameters in CI
// eslint-disable-next-line no-unused-vars
type int = number;

export default class lunaParser extends Parser {
	public static readonly T__0 = 1;
	public static readonly T__1 = 2;
	public static readonly T__2 = 3;
	public static readonly T__3 = 4;
	public static readonly T__4 = 5;
	public static readonly T__5 = 6;
	public static readonly T__6 = 7;
	public static readonly T__7 = 8;
	public static readonly T__8 = 9;
	public static readonly T__9 = 10;
	public static readonly T__10 = 11;
	public static readonly T__11 = 12;
	public static readonly T__12 = 13;
	public static readonly T__13 = 14;
	public static readonly T__14 = 15;
	public static readonly T__15 = 16;
	public static readonly T__16 = 17;
	public static readonly T__17 = 18;
	public static readonly T__18 = 19;
	public static readonly T__19 = 20;
	public static readonly T__20 = 21;
	public static readonly T__21 = 22;
	public static readonly T__22 = 23;
	public static readonly T__23 = 24;
	public static readonly T__24 = 25;
	public static readonly T__25 = 26;
	public static readonly T__26 = 27;
	public static readonly T__27 = 28;
	public static readonly T__28 = 29;
	public static readonly T__29 = 30;
	public static readonly T__30 = 31;
	public static readonly WORD = 32;
	public static readonly INT = 33;
	public static readonly STRING = 34;
	public static readonly WS = 35;
	public static readonly EOF = Token.EOF;
	public static readonly RULE_program = 0;
	public static readonly RULE_typeModifier = 1;
	public static readonly RULE_allocatorSize = 2;
	public static readonly RULE_expression = 3;
	public static readonly RULE_primaryExpression = 4;
	public static readonly RULE_atom = 5;
	public static readonly RULE_memoryAllocation = 6;
	public static readonly RULE_functionDeclaration = 7;
	public static readonly RULE_anonymysFunctionDeclaration = 8;
	public static readonly RULE_wordWithParameter = 9;
	public static readonly RULE_conditionExpression = 10;
	public static readonly RULE_ifStatement = 11;
	public static readonly RULE_whileStatement = 12;
	public static readonly RULE_assignmentStatement = 13;
	public static readonly RULE_forStatement = 14;
	public static readonly RULE_returnCall = 15;
	public static readonly RULE_breakStatement = 16;
	public static readonly RULE_continueStatement = 17;
	public static readonly RULE_parameters = 18;
	public static readonly RULE_parameter = 19;
	public static readonly RULE_modifier = 20;
	public static readonly RULE_type = 21;
	public static readonly RULE_typeParameters = 22;
	public static readonly RULE_block = 23;
	public static readonly RULE_operationStatement = 24;
	public static readonly RULE_statement = 25;
	public static readonly literalNames: (string | null)[] = [ null, "'const'", 
                                                            "'var'", "'i32'", 
                                                            "'i64'", "'+'", 
                                                            "'-'", "'*'", 
                                                            "'/'", "'('", 
                                                            "')'", "'='", 
                                                            "';'", "'func'", 
                                                            "','", "'<'", 
                                                            "'>'", "'<='", 
                                                            "'>='", "'!='", 
                                                            "'=='", "'%'", 
                                                            "'if'", "'else'", 
                                                            "'while'", "'for'", 
                                                            "'return'", 
                                                            "'break'", "'continue'", 
                                                            "'void'", "'{'", 
                                                            "'}'" ];
	public static readonly symbolicNames: (string | null)[] = [ null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             "WORD", "INT", 
                                                             "STRING", "WS" ];
	// tslint:disable:no-trailing-whitespace
	public static readonly ruleNames: string[] = [
		"program", "typeModifier", "allocatorSize", "expression", "primaryExpression", 
		"atom", "memoryAllocation", "functionDeclaration", "anonymysFunctionDeclaration", 
		"wordWithParameter", "conditionExpression", "ifStatement", "whileStatement", 
		"assignmentStatement", "forStatement", "returnCall", "breakStatement", 
		"continueStatement", "parameters", "parameter", "modifier", "type", "typeParameters", 
		"block", "operationStatement", "statement",
	];
	public get grammarFileName(): string { return "luna.g4"; }
	public get literalNames(): (string | null)[] { return lunaParser.literalNames; }
	public get symbolicNames(): (string | null)[] { return lunaParser.symbolicNames; }
	public get ruleNames(): string[] { return lunaParser.ruleNames; }
	public get serializedATN(): number[] { return lunaParser._serializedATN; }

	protected createFailedPredicateException(predicate?: string, message?: string): FailedPredicateException {
		return new FailedPredicateException(this, predicate, message);
	}

	constructor(input: TokenStream) {
		super(input);
		this._interp = new ParserATNSimulator(this, lunaParser._ATN, lunaParser.DecisionsToDFA, new PredictionContextCache());
	}
	// @RuleVersion(0)
	public program(): ProgramContext {
		let localctx: ProgramContext = new ProgramContext(this, this._ctx, this.state);
		this.enterRule(localctx, 0, lunaParser.RULE_program);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 55;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while (((((_la - 1)) & ~0x1F) === 0 && ((1 << (_la - 1)) & 2409631747) !== 0)) {
				{
				{
				this.state = 52;
				this.statement();
				}
				}
				this.state = 57;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			this.state = 58;
			this.match(lunaParser.EOF);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public typeModifier(): TypeModifierContext {
		let localctx: TypeModifierContext = new TypeModifierContext(this, this._ctx, this.state);
		this.enterRule(localctx, 2, lunaParser.RULE_typeModifier);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 60;
			_la = this._input.LA(1);
			if(!(_la===1 || _la===2)) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public allocatorSize(): AllocatorSizeContext {
		let localctx: AllocatorSizeContext = new AllocatorSizeContext(this, this._ctx, this.state);
		this.enterRule(localctx, 4, lunaParser.RULE_allocatorSize);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 62;
			_la = this._input.LA(1);
			if(!(_la===3 || _la===4)) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}

	public expression(): ExpressionContext;
	public expression(_p: number): ExpressionContext;
	// @RuleVersion(0)
	public expression(_p?: number): ExpressionContext {
		if (_p === undefined) {
			_p = 0;
		}

		let _parentctx: ParserRuleContext = this._ctx;
		let _parentState: number = this.state;
		let localctx: ExpressionContext = new ExpressionContext(this, this._ctx, _parentState);
		let _prevctx: ExpressionContext = localctx;
		let _startState: number = 6;
		this.enterRecursionRule(localctx, 6, lunaParser.RULE_expression, _p);
		try {
			let _alt: number;
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 67;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 1, this._ctx) ) {
			case 1:
				{
				this.state = 65;
				this.primaryExpression(0);
				}
				break;
			case 2:
				{
				this.state = 66;
				this.wordWithParameter();
				}
				break;
			}
			this._ctx.stop = this._input.LT(-1);
			this.state = 77;
			this._errHandler.sync(this);
			_alt = this._interp.adaptivePredict(this._input, 3, this._ctx);
			while (_alt !== 2 && _alt !== ATN.INVALID_ALT_NUMBER) {
				if (_alt === 1) {
					if (this._parseListeners != null) {
						this.triggerExitRuleEvent();
					}
					_prevctx = localctx;
					{
					this.state = 75;
					this._errHandler.sync(this);
					switch ( this._interp.adaptivePredict(this._input, 2, this._ctx) ) {
					case 1:
						{
						localctx = new ExpressionContext(this, _parentctx, _parentState);
						this.pushNewRecursionContext(localctx, _startState, lunaParser.RULE_expression);
						this.state = 69;
						if (!(this.precpred(this._ctx, 2))) {
							throw this.createFailedPredicateException("this.precpred(this._ctx, 2)");
						}
						this.state = 70;
						this.match(lunaParser.T__4);
						this.state = 71;
						this.expression(3);
						}
						break;
					case 2:
						{
						localctx = new ExpressionContext(this, _parentctx, _parentState);
						this.pushNewRecursionContext(localctx, _startState, lunaParser.RULE_expression);
						this.state = 72;
						if (!(this.precpred(this._ctx, 1))) {
							throw this.createFailedPredicateException("this.precpred(this._ctx, 1)");
						}
						this.state = 73;
						this.match(lunaParser.T__5);
						this.state = 74;
						this.expression(2);
						}
						break;
					}
					}
				}
				this.state = 79;
				this._errHandler.sync(this);
				_alt = this._interp.adaptivePredict(this._input, 3, this._ctx);
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.unrollRecursionContexts(_parentctx);
		}
		return localctx;
	}

	public primaryExpression(): PrimaryExpressionContext;
	public primaryExpression(_p: number): PrimaryExpressionContext;
	// @RuleVersion(0)
	public primaryExpression(_p?: number): PrimaryExpressionContext {
		if (_p === undefined) {
			_p = 0;
		}

		let _parentctx: ParserRuleContext = this._ctx;
		let _parentState: number = this.state;
		let localctx: PrimaryExpressionContext = new PrimaryExpressionContext(this, this._ctx, _parentState);
		let _prevctx: PrimaryExpressionContext = localctx;
		let _startState: number = 8;
		this.enterRecursionRule(localctx, 8, lunaParser.RULE_primaryExpression, _p);
		try {
			let _alt: number;
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 83;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 4, this._ctx) ) {
			case 1:
				{
				this.state = 81;
				this.atom();
				}
				break;
			case 2:
				{
				this.state = 82;
				this.anonymysFunctionDeclaration();
				}
				break;
			}
			this._ctx.stop = this._input.LT(-1);
			this.state = 93;
			this._errHandler.sync(this);
			_alt = this._interp.adaptivePredict(this._input, 6, this._ctx);
			while (_alt !== 2 && _alt !== ATN.INVALID_ALT_NUMBER) {
				if (_alt === 1) {
					if (this._parseListeners != null) {
						this.triggerExitRuleEvent();
					}
					_prevctx = localctx;
					{
					this.state = 91;
					this._errHandler.sync(this);
					switch ( this._interp.adaptivePredict(this._input, 5, this._ctx) ) {
					case 1:
						{
						localctx = new PrimaryExpressionContext(this, _parentctx, _parentState);
						this.pushNewRecursionContext(localctx, _startState, lunaParser.RULE_primaryExpression);
						this.state = 85;
						if (!(this.precpred(this._ctx, 2))) {
							throw this.createFailedPredicateException("this.precpred(this._ctx, 2)");
						}
						this.state = 86;
						this.match(lunaParser.T__6);
						this.state = 87;
						this.primaryExpression(3);
						}
						break;
					case 2:
						{
						localctx = new PrimaryExpressionContext(this, _parentctx, _parentState);
						this.pushNewRecursionContext(localctx, _startState, lunaParser.RULE_primaryExpression);
						this.state = 88;
						if (!(this.precpred(this._ctx, 1))) {
							throw this.createFailedPredicateException("this.precpred(this._ctx, 1)");
						}
						this.state = 89;
						this.match(lunaParser.T__7);
						this.state = 90;
						this.primaryExpression(2);
						}
						break;
					}
					}
				}
				this.state = 95;
				this._errHandler.sync(this);
				_alt = this._interp.adaptivePredict(this._input, 6, this._ctx);
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.unrollRecursionContexts(_parentctx);
		}
		return localctx;
	}
	// @RuleVersion(0)
	public atom(): AtomContext {
		let localctx: AtomContext = new AtomContext(this, this._ctx, this.state);
		this.enterRule(localctx, 10, lunaParser.RULE_atom);
		try {
			this.state = 103;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 33:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 96;
				this.match(lunaParser.INT);
				}
				break;
			case 34:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 97;
				this.match(lunaParser.STRING);
				}
				break;
			case 32:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 98;
				this.match(lunaParser.WORD);
				}
				break;
			case 9:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 99;
				this.match(lunaParser.T__8);
				this.state = 100;
				this.expression(0);
				this.state = 101;
				this.match(lunaParser.T__9);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public memoryAllocation(): MemoryAllocationContext {
		let localctx: MemoryAllocationContext = new MemoryAllocationContext(this, this._ctx, this.state);
		this.enterRule(localctx, 12, lunaParser.RULE_memoryAllocation);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 105;
			this.typeModifier();
			this.state = 106;
			this.match(lunaParser.WORD);
			this.state = 108;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===3 || _la===4) {
				{
				this.state = 107;
				this.allocatorSize();
				}
			}

			this.state = 110;
			this.match(lunaParser.T__10);
			this.state = 111;
			this.expression(0);
			this.state = 113;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 9, this._ctx) ) {
			case 1:
				{
				this.state = 112;
				this.match(lunaParser.T__11);
				}
				break;
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public functionDeclaration(): FunctionDeclarationContext {
		let localctx: FunctionDeclarationContext = new FunctionDeclarationContext(this, this._ctx, this.state);
		this.enterRule(localctx, 14, lunaParser.RULE_functionDeclaration);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 120;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===32) {
				{
				this.state = 116;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
				do {
					{
					{
					this.state = 115;
					this.modifier();
					}
					}
					this.state = 118;
					this._errHandler.sync(this);
					_la = this._input.LA(1);
				} while (_la===32);
				}
			}

			this.state = 122;
			this.match(lunaParser.T__12);
			this.state = 123;
			this.match(lunaParser.WORD);
			this.state = 124;
			this.match(lunaParser.T__8);
			this.state = 126;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===32) {
				{
				this.state = 125;
				this.parameters();
				}
			}

			this.state = 128;
			this.match(lunaParser.T__9);
			this.state = 130;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (((((_la - 3)) & ~0x1F) === 0 && ((1 << (_la - 3)) & 603980803) !== 0)) {
				{
				this.state = 129;
				this.type_();
				}
			}

			this.state = 132;
			this.block();
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public anonymysFunctionDeclaration(): AnonymysFunctionDeclarationContext {
		let localctx: AnonymysFunctionDeclarationContext = new AnonymysFunctionDeclarationContext(this, this._ctx, this.state);
		this.enterRule(localctx, 16, lunaParser.RULE_anonymysFunctionDeclaration);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 135;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===13) {
				{
				this.state = 134;
				this.match(lunaParser.T__12);
				}
			}

			this.state = 138;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===32) {
				{
				this.state = 137;
				this.match(lunaParser.WORD);
				}
			}

			this.state = 140;
			this.match(lunaParser.T__8);
			this.state = 142;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===32) {
				{
				this.state = 141;
				this.parameters();
				}
			}

			this.state = 144;
			this.match(lunaParser.T__9);
			this.state = 146;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (((((_la - 3)) & ~0x1F) === 0 && ((1 << (_la - 3)) & 603980803) !== 0)) {
				{
				this.state = 145;
				this.type_();
				}
			}

			this.state = 148;
			this.block();
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public wordWithParameter(): WordWithParameterContext {
		let localctx: WordWithParameterContext = new WordWithParameterContext(this, this._ctx, this.state);
		this.enterRule(localctx, 18, lunaParser.RULE_wordWithParameter);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 150;
			this.match(lunaParser.WORD);
			this.state = 151;
			this.match(lunaParser.T__8);
			this.state = 160;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (((((_la - 9)) & ~0x1F) === 0 && ((1 << (_la - 9)) & 58720273) !== 0)) {
				{
				this.state = 152;
				this.expression(0);
				this.state = 157;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
				while (_la===14) {
					{
					{
					this.state = 153;
					this.match(lunaParser.T__13);
					this.state = 154;
					this.expression(0);
					}
					}
					this.state = 159;
					this._errHandler.sync(this);
					_la = this._input.LA(1);
				}
				}
			}

			this.state = 162;
			this.match(lunaParser.T__9);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public conditionExpression(): ConditionExpressionContext {
		let localctx: ConditionExpressionContext = new ConditionExpressionContext(this, this._ctx, this.state);
		this.enterRule(localctx, 20, lunaParser.RULE_conditionExpression);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 164;
			this.expression(0);
			this.state = 165;
			_la = this._input.LA(1);
			if(!((((_la) & ~0x1F) === 0 && ((1 << _la) & 4161536) !== 0))) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			this.state = 166;
			this.expression(0);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public ifStatement(): IfStatementContext {
		let localctx: IfStatementContext = new IfStatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 22, lunaParser.RULE_ifStatement);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 168;
			this.match(lunaParser.T__21);
			this.state = 169;
			this.conditionExpression();
			this.state = 170;
			this.block();
			this.state = 173;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===23) {
				{
				this.state = 171;
				this.match(lunaParser.T__22);
				this.state = 172;
				this.block();
				}
			}

			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public whileStatement(): WhileStatementContext {
		let localctx: WhileStatementContext = new WhileStatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 24, lunaParser.RULE_whileStatement);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 175;
			this.match(lunaParser.T__23);
			this.state = 176;
			this.conditionExpression();
			this.state = 177;
			this.block();
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public assignmentStatement(): AssignmentStatementContext {
		let localctx: AssignmentStatementContext = new AssignmentStatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 26, lunaParser.RULE_assignmentStatement);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 179;
			this.match(lunaParser.WORD);
			this.state = 180;
			this.match(lunaParser.T__10);
			this.state = 181;
			this.expression(0);
			this.state = 183;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===12) {
				{
				this.state = 182;
				this.match(lunaParser.T__11);
				}
			}

			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public forStatement(): ForStatementContext {
		let localctx: ForStatementContext = new ForStatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 28, lunaParser.RULE_forStatement);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 185;
			this.match(lunaParser.T__24);
			this.state = 186;
			this.match(lunaParser.T__8);
			this.state = 188;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===1 || _la===2) {
				{
				this.state = 187;
				this.memoryAllocation();
				}
			}

			this.state = 190;
			this.match(lunaParser.T__11);
			this.state = 192;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (((((_la - 9)) & ~0x1F) === 0 && ((1 << (_la - 9)) & 58720273) !== 0)) {
				{
				this.state = 191;
				this.conditionExpression();
				}
			}

			this.state = 194;
			this.match(lunaParser.T__11);
			this.state = 196;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===32) {
				{
				this.state = 195;
				this.assignmentStatement();
				}
			}

			this.state = 198;
			this.match(lunaParser.T__9);
			this.state = 199;
			this.block();
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public returnCall(): ReturnCallContext {
		let localctx: ReturnCallContext = new ReturnCallContext(this, this._ctx, this.state);
		this.enterRule(localctx, 30, lunaParser.RULE_returnCall);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 201;
			this.match(lunaParser.T__25);
			this.state = 203;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 25, this._ctx) ) {
			case 1:
				{
				this.state = 202;
				this.expression(0);
				}
				break;
			}
			this.state = 206;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===12) {
				{
				this.state = 205;
				this.match(lunaParser.T__11);
				}
			}

			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public breakStatement(): BreakStatementContext {
		let localctx: BreakStatementContext = new BreakStatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 32, lunaParser.RULE_breakStatement);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 208;
			this.match(lunaParser.T__26);
			this.state = 209;
			this.match(lunaParser.T__11);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public continueStatement(): ContinueStatementContext {
		let localctx: ContinueStatementContext = new ContinueStatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 34, lunaParser.RULE_continueStatement);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 211;
			this.match(lunaParser.T__27);
			this.state = 212;
			this.match(lunaParser.T__11);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public parameters(): ParametersContext {
		let localctx: ParametersContext = new ParametersContext(this, this._ctx, this.state);
		this.enterRule(localctx, 36, lunaParser.RULE_parameters);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 214;
			this.parameter();
			this.state = 219;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while (_la===14) {
				{
				{
				this.state = 215;
				this.match(lunaParser.T__13);
				this.state = 216;
				this.parameter();
				}
				}
				this.state = 221;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public parameter(): ParameterContext {
		let localctx: ParameterContext = new ParameterContext(this, this._ctx, this.state);
		this.enterRule(localctx, 38, lunaParser.RULE_parameter);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 222;
			this.match(lunaParser.WORD);
			this.state = 224;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (((((_la - 3)) & ~0x1F) === 0 && ((1 << (_la - 3)) & 603980803) !== 0)) {
				{
				this.state = 223;
				this.type_();
				}
			}

			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public modifier(): ModifierContext {
		let localctx: ModifierContext = new ModifierContext(this, this._ctx, this.state);
		this.enterRule(localctx, 40, lunaParser.RULE_modifier);
		try {
			this.state = 228;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 29, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 226;
				this.wordWithParameter();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 227;
				this.match(lunaParser.WORD);
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public type_(): TypeContext {
		let localctx: TypeContext = new TypeContext(this, this._ctx, this.state);
		this.enterRule(localctx, 42, lunaParser.RULE_type);
		let _la: number;
		try {
			this.state = 241;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 3:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 230;
				this.match(lunaParser.T__2);
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 231;
				this.match(lunaParser.T__3);
				}
				break;
			case 29:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 232;
				this.match(lunaParser.T__28);
				}
				break;
			case 32:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 233;
				this.match(lunaParser.WORD);
				}
				break;
			case 13:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 234;
				this.match(lunaParser.T__12);
				this.state = 235;
				this.match(lunaParser.T__8);
				this.state = 237;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
				if (((((_la - 3)) & ~0x1F) === 0 && ((1 << (_la - 3)) & 603980803) !== 0)) {
					{
					this.state = 236;
					this.typeParameters();
					}
				}

				this.state = 239;
				this.match(lunaParser.T__9);
				this.state = 240;
				this.type_();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public typeParameters(): TypeParametersContext {
		let localctx: TypeParametersContext = new TypeParametersContext(this, this._ctx, this.state);
		this.enterRule(localctx, 44, lunaParser.RULE_typeParameters);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 243;
			this.type_();
			this.state = 248;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while (_la===14) {
				{
				{
				this.state = 244;
				this.match(lunaParser.T__13);
				this.state = 245;
				this.type_();
				}
				}
				this.state = 250;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public block(): BlockContext {
		let localctx: BlockContext = new BlockContext(this, this._ctx, this.state);
		this.enterRule(localctx, 46, lunaParser.RULE_block);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 251;
			this.match(lunaParser.T__29);
			this.state = 255;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while (((((_la - 1)) & ~0x1F) === 0 && ((1 << (_la - 1)) & 2409631747) !== 0)) {
				{
				{
				this.state = 252;
				this.statement();
				}
				}
				this.state = 257;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			this.state = 258;
			this.match(lunaParser.T__30);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public operationStatement(): OperationStatementContext {
		let localctx: OperationStatementContext = new OperationStatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 48, lunaParser.RULE_operationStatement);
		try {
			this.state = 265;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 22:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 260;
				this.ifStatement();
				}
				break;
			case 24:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 261;
				this.whileStatement();
				}
				break;
			case 25:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 262;
				this.forStatement();
				}
				break;
			case 27:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 263;
				this.breakStatement();
				}
				break;
			case 28:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 264;
				this.continueStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public statement(): StatementContext {
		let localctx: StatementContext = new StatementContext(this, this._ctx, this.state);
		this.enterRule(localctx, 50, lunaParser.RULE_statement);
		try {
			this.state = 272;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 35, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 267;
				this.memoryAllocation();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 268;
				this.wordWithParameter();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 269;
				this.functionDeclaration();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 270;
				this.returnCall();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 271;
				this.operationStatement();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}

	public sempred(localctx: RuleContext, ruleIndex: number, predIndex: number): boolean {
		switch (ruleIndex) {
		case 3:
			return this.expression_sempred(localctx as ExpressionContext, predIndex);
		case 4:
			return this.primaryExpression_sempred(localctx as PrimaryExpressionContext, predIndex);
		}
		return true;
	}
	private expression_sempred(localctx: ExpressionContext, predIndex: number): boolean {
		switch (predIndex) {
		case 0:
			return this.precpred(this._ctx, 2);
		case 1:
			return this.precpred(this._ctx, 1);
		}
		return true;
	}
	private primaryExpression_sempred(localctx: PrimaryExpressionContext, predIndex: number): boolean {
		switch (predIndex) {
		case 2:
			return this.precpred(this._ctx, 2);
		case 3:
			return this.precpred(this._ctx, 1);
		}
		return true;
	}

	public static readonly _serializedATN: number[] = [4,1,35,275,2,0,7,0,2,
	1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,
	10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,
	7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,
	24,2,25,7,25,1,0,5,0,54,8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,
	3,1,3,1,3,3,3,68,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,76,8,3,10,3,12,3,79,9,
	3,1,4,1,4,1,4,3,4,84,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,92,8,4,10,4,12,4,95,
	9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,104,8,5,1,6,1,6,1,6,3,6,109,8,6,1,6,
	1,6,1,6,3,6,114,8,6,1,7,4,7,117,8,7,11,7,12,7,118,3,7,121,8,7,1,7,1,7,1,
	7,1,7,3,7,127,8,7,1,7,1,7,3,7,131,8,7,1,7,1,7,1,8,3,8,136,8,8,1,8,3,8,139,
	8,8,1,8,1,8,3,8,143,8,8,1,8,1,8,3,8,147,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
	5,9,156,8,9,10,9,12,9,159,9,9,3,9,161,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
	11,1,11,1,11,1,11,1,11,3,11,174,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
	1,13,3,13,184,8,13,1,14,1,14,1,14,3,14,189,8,14,1,14,1,14,3,14,193,8,14,
	1,14,1,14,3,14,197,8,14,1,14,1,14,1,14,1,15,1,15,3,15,204,8,15,1,15,3,15,
	207,8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,5,18,218,8,18,10,
	18,12,18,221,9,18,1,19,1,19,3,19,225,8,19,1,20,1,20,3,20,229,8,20,1,21,
	1,21,1,21,1,21,1,21,1,21,1,21,3,21,238,8,21,1,21,1,21,3,21,242,8,21,1,22,
	1,22,1,22,5,22,247,8,22,10,22,12,22,250,9,22,1,23,1,23,5,23,254,8,23,10,
	23,12,23,257,9,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,266,8,24,1,25,
	1,25,1,25,1,25,1,25,3,25,273,8,25,1,25,0,2,6,8,26,0,2,4,6,8,10,12,14,16,
	18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,3,1,0,1,2,1,0,3,4,
	1,0,15,21,295,0,55,1,0,0,0,2,60,1,0,0,0,4,62,1,0,0,0,6,67,1,0,0,0,8,83,
	1,0,0,0,10,103,1,0,0,0,12,105,1,0,0,0,14,120,1,0,0,0,16,135,1,0,0,0,18,
	150,1,0,0,0,20,164,1,0,0,0,22,168,1,0,0,0,24,175,1,0,0,0,26,179,1,0,0,0,
	28,185,1,0,0,0,30,201,1,0,0,0,32,208,1,0,0,0,34,211,1,0,0,0,36,214,1,0,
	0,0,38,222,1,0,0,0,40,228,1,0,0,0,42,241,1,0,0,0,44,243,1,0,0,0,46,251,
	1,0,0,0,48,265,1,0,0,0,50,272,1,0,0,0,52,54,3,50,25,0,53,52,1,0,0,0,54,
	57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,
	5,0,0,1,59,1,1,0,0,0,60,61,7,0,0,0,61,3,1,0,0,0,62,63,7,1,0,0,63,5,1,0,
	0,0,64,65,6,3,-1,0,65,68,3,8,4,0,66,68,3,18,9,0,67,64,1,0,0,0,67,66,1,0,
	0,0,68,77,1,0,0,0,69,70,10,2,0,0,70,71,5,5,0,0,71,76,3,6,3,3,72,73,10,1,
	0,0,73,74,5,6,0,0,74,76,3,6,3,2,75,69,1,0,0,0,75,72,1,0,0,0,76,79,1,0,0,
	0,77,75,1,0,0,0,77,78,1,0,0,0,78,7,1,0,0,0,79,77,1,0,0,0,80,81,6,4,-1,0,
	81,84,3,10,5,0,82,84,3,16,8,0,83,80,1,0,0,0,83,82,1,0,0,0,84,93,1,0,0,0,
	85,86,10,2,0,0,86,87,5,7,0,0,87,92,3,8,4,3,88,89,10,1,0,0,89,90,5,8,0,0,
	90,92,3,8,4,2,91,85,1,0,0,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,
	94,1,0,0,0,94,9,1,0,0,0,95,93,1,0,0,0,96,104,5,33,0,0,97,104,5,34,0,0,98,
	104,5,32,0,0,99,100,5,9,0,0,100,101,3,6,3,0,101,102,5,10,0,0,102,104,1,
	0,0,0,103,96,1,0,0,0,103,97,1,0,0,0,103,98,1,0,0,0,103,99,1,0,0,0,104,11,
	1,0,0,0,105,106,3,2,1,0,106,108,5,32,0,0,107,109,3,4,2,0,108,107,1,0,0,
	0,108,109,1,0,0,0,109,110,1,0,0,0,110,111,5,11,0,0,111,113,3,6,3,0,112,
	114,5,12,0,0,113,112,1,0,0,0,113,114,1,0,0,0,114,13,1,0,0,0,115,117,3,40,
	20,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,
	121,1,0,0,0,120,116,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,5,13,
	0,0,123,124,5,32,0,0,124,126,5,9,0,0,125,127,3,36,18,0,126,125,1,0,0,0,
	126,127,1,0,0,0,127,128,1,0,0,0,128,130,5,10,0,0,129,131,3,42,21,0,130,
	129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,133,3,46,23,0,133,15,1,
	0,0,0,134,136,5,13,0,0,135,134,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,
	137,139,5,32,0,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,142,
	5,9,0,0,141,143,3,36,18,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,
	0,144,146,5,10,0,0,145,147,3,42,21,0,146,145,1,0,0,0,146,147,1,0,0,0,147,
	148,1,0,0,0,148,149,3,46,23,0,149,17,1,0,0,0,150,151,5,32,0,0,151,160,5,
	9,0,0,152,157,3,6,3,0,153,154,5,14,0,0,154,156,3,6,3,0,155,153,1,0,0,0,
	156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,161,1,0,0,0,159,157,
	1,0,0,0,160,152,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,163,5,10,0,
	0,163,19,1,0,0,0,164,165,3,6,3,0,165,166,7,2,0,0,166,167,3,6,3,0,167,21,
	1,0,0,0,168,169,5,22,0,0,169,170,3,20,10,0,170,173,3,46,23,0,171,172,5,
	23,0,0,172,174,3,46,23,0,173,171,1,0,0,0,173,174,1,0,0,0,174,23,1,0,0,0,
	175,176,5,24,0,0,176,177,3,20,10,0,177,178,3,46,23,0,178,25,1,0,0,0,179,
	180,5,32,0,0,180,181,5,11,0,0,181,183,3,6,3,0,182,184,5,12,0,0,183,182,
	1,0,0,0,183,184,1,0,0,0,184,27,1,0,0,0,185,186,5,25,0,0,186,188,5,9,0,0,
	187,189,3,12,6,0,188,187,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,192,
	5,12,0,0,191,193,3,20,10,0,192,191,1,0,0,0,192,193,1,0,0,0,193,194,1,0,
	0,0,194,196,5,12,0,0,195,197,3,26,13,0,196,195,1,0,0,0,196,197,1,0,0,0,
	197,198,1,0,0,0,198,199,5,10,0,0,199,200,3,46,23,0,200,29,1,0,0,0,201,203,
	5,26,0,0,202,204,3,6,3,0,203,202,1,0,0,0,203,204,1,0,0,0,204,206,1,0,0,
	0,205,207,5,12,0,0,206,205,1,0,0,0,206,207,1,0,0,0,207,31,1,0,0,0,208,209,
	5,27,0,0,209,210,5,12,0,0,210,33,1,0,0,0,211,212,5,28,0,0,212,213,5,12,
	0,0,213,35,1,0,0,0,214,219,3,38,19,0,215,216,5,14,0,0,216,218,3,38,19,0,
	217,215,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,37,
	1,0,0,0,221,219,1,0,0,0,222,224,5,32,0,0,223,225,3,42,21,0,224,223,1,0,
	0,0,224,225,1,0,0,0,225,39,1,0,0,0,226,229,3,18,9,0,227,229,5,32,0,0,228,
	226,1,0,0,0,228,227,1,0,0,0,229,41,1,0,0,0,230,242,5,3,0,0,231,242,5,4,
	0,0,232,242,5,29,0,0,233,242,5,32,0,0,234,235,5,13,0,0,235,237,5,9,0,0,
	236,238,3,44,22,0,237,236,1,0,0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,
	5,10,0,0,240,242,3,42,21,0,241,230,1,0,0,0,241,231,1,0,0,0,241,232,1,0,
	0,0,241,233,1,0,0,0,241,234,1,0,0,0,242,43,1,0,0,0,243,248,3,42,21,0,244,
	245,5,14,0,0,245,247,3,42,21,0,246,244,1,0,0,0,247,250,1,0,0,0,248,246,
	1,0,0,0,248,249,1,0,0,0,249,45,1,0,0,0,250,248,1,0,0,0,251,255,5,30,0,0,
	252,254,3,50,25,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,
	1,0,0,0,256,258,1,0,0,0,257,255,1,0,0,0,258,259,5,31,0,0,259,47,1,0,0,0,
	260,266,3,22,11,0,261,266,3,24,12,0,262,266,3,28,14,0,263,266,3,32,16,0,
	264,266,3,34,17,0,265,260,1,0,0,0,265,261,1,0,0,0,265,262,1,0,0,0,265,263,
	1,0,0,0,265,264,1,0,0,0,266,49,1,0,0,0,267,273,3,12,6,0,268,273,3,18,9,
	0,269,273,3,14,7,0,270,273,3,30,15,0,271,273,3,48,24,0,272,267,1,0,0,0,
	272,268,1,0,0,0,272,269,1,0,0,0,272,270,1,0,0,0,272,271,1,0,0,0,273,51,
	1,0,0,0,36,55,67,75,77,83,91,93,103,108,113,118,120,126,130,135,138,142,
	146,157,160,173,183,188,192,196,203,206,219,224,228,237,241,248,255,265,
	272];

	private static __ATN: ATN;
	public static get _ATN(): ATN {
		if (!lunaParser.__ATN) {
			lunaParser.__ATN = new ATNDeserializer().deserialize(lunaParser._serializedATN);
		}

		return lunaParser.__ATN;
	}


	static DecisionsToDFA = lunaParser._ATN.decisionToState.map( (ds: DecisionState, index: number) => new DFA(ds, index) );

}

export class ProgramContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public EOF(): TerminalNode {
		return this.getToken(lunaParser.EOF, 0);
	}
	public statement_list(): StatementContext[] {
		return this.getTypedRuleContexts(StatementContext) as StatementContext[];
	}
	public statement(i: number): StatementContext {
		return this.getTypedRuleContext(StatementContext, i) as StatementContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_program;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterProgram) {
	 		listener.enterProgram(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitProgram) {
	 		listener.exitProgram(this);
		}
	}
}


export class TypeModifierContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_typeModifier;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterTypeModifier) {
	 		listener.enterTypeModifier(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitTypeModifier) {
	 		listener.exitTypeModifier(this);
		}
	}
}


export class AllocatorSizeContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_allocatorSize;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterAllocatorSize) {
	 		listener.enterAllocatorSize(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitAllocatorSize) {
	 		listener.exitAllocatorSize(this);
		}
	}
}


export class ExpressionContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public primaryExpression(): PrimaryExpressionContext {
		return this.getTypedRuleContext(PrimaryExpressionContext, 0) as PrimaryExpressionContext;
	}
	public wordWithParameter(): WordWithParameterContext {
		return this.getTypedRuleContext(WordWithParameterContext, 0) as WordWithParameterContext;
	}
	public expression_list(): ExpressionContext[] {
		return this.getTypedRuleContexts(ExpressionContext) as ExpressionContext[];
	}
	public expression(i: number): ExpressionContext {
		return this.getTypedRuleContext(ExpressionContext, i) as ExpressionContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_expression;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterExpression) {
	 		listener.enterExpression(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitExpression) {
	 		listener.exitExpression(this);
		}
	}
}


export class PrimaryExpressionContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public atom(): AtomContext {
		return this.getTypedRuleContext(AtomContext, 0) as AtomContext;
	}
	public anonymysFunctionDeclaration(): AnonymysFunctionDeclarationContext {
		return this.getTypedRuleContext(AnonymysFunctionDeclarationContext, 0) as AnonymysFunctionDeclarationContext;
	}
	public primaryExpression_list(): PrimaryExpressionContext[] {
		return this.getTypedRuleContexts(PrimaryExpressionContext) as PrimaryExpressionContext[];
	}
	public primaryExpression(i: number): PrimaryExpressionContext {
		return this.getTypedRuleContext(PrimaryExpressionContext, i) as PrimaryExpressionContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_primaryExpression;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterPrimaryExpression) {
	 		listener.enterPrimaryExpression(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitPrimaryExpression) {
	 		listener.exitPrimaryExpression(this);
		}
	}
}


export class AtomContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public INT(): TerminalNode {
		return this.getToken(lunaParser.INT, 0);
	}
	public STRING(): TerminalNode {
		return this.getToken(lunaParser.STRING, 0);
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public expression(): ExpressionContext {
		return this.getTypedRuleContext(ExpressionContext, 0) as ExpressionContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_atom;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterAtom) {
	 		listener.enterAtom(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitAtom) {
	 		listener.exitAtom(this);
		}
	}
}


export class MemoryAllocationContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public typeModifier(): TypeModifierContext {
		return this.getTypedRuleContext(TypeModifierContext, 0) as TypeModifierContext;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public expression(): ExpressionContext {
		return this.getTypedRuleContext(ExpressionContext, 0) as ExpressionContext;
	}
	public allocatorSize(): AllocatorSizeContext {
		return this.getTypedRuleContext(AllocatorSizeContext, 0) as AllocatorSizeContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_memoryAllocation;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterMemoryAllocation) {
	 		listener.enterMemoryAllocation(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitMemoryAllocation) {
	 		listener.exitMemoryAllocation(this);
		}
	}
}


export class FunctionDeclarationContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public block(): BlockContext {
		return this.getTypedRuleContext(BlockContext, 0) as BlockContext;
	}
	public parameters(): ParametersContext {
		return this.getTypedRuleContext(ParametersContext, 0) as ParametersContext;
	}
	public type_(): TypeContext {
		return this.getTypedRuleContext(TypeContext, 0) as TypeContext;
	}
	public modifier_list(): ModifierContext[] {
		return this.getTypedRuleContexts(ModifierContext) as ModifierContext[];
	}
	public modifier(i: number): ModifierContext {
		return this.getTypedRuleContext(ModifierContext, i) as ModifierContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_functionDeclaration;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterFunctionDeclaration) {
	 		listener.enterFunctionDeclaration(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitFunctionDeclaration) {
	 		listener.exitFunctionDeclaration(this);
		}
	}
}


export class AnonymysFunctionDeclarationContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public block(): BlockContext {
		return this.getTypedRuleContext(BlockContext, 0) as BlockContext;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public parameters(): ParametersContext {
		return this.getTypedRuleContext(ParametersContext, 0) as ParametersContext;
	}
	public type_(): TypeContext {
		return this.getTypedRuleContext(TypeContext, 0) as TypeContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_anonymysFunctionDeclaration;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterAnonymysFunctionDeclaration) {
	 		listener.enterAnonymysFunctionDeclaration(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitAnonymysFunctionDeclaration) {
	 		listener.exitAnonymysFunctionDeclaration(this);
		}
	}
}


export class WordWithParameterContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public expression_list(): ExpressionContext[] {
		return this.getTypedRuleContexts(ExpressionContext) as ExpressionContext[];
	}
	public expression(i: number): ExpressionContext {
		return this.getTypedRuleContext(ExpressionContext, i) as ExpressionContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_wordWithParameter;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterWordWithParameter) {
	 		listener.enterWordWithParameter(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitWordWithParameter) {
	 		listener.exitWordWithParameter(this);
		}
	}
}


export class ConditionExpressionContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public expression_list(): ExpressionContext[] {
		return this.getTypedRuleContexts(ExpressionContext) as ExpressionContext[];
	}
	public expression(i: number): ExpressionContext {
		return this.getTypedRuleContext(ExpressionContext, i) as ExpressionContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_conditionExpression;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterConditionExpression) {
	 		listener.enterConditionExpression(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitConditionExpression) {
	 		listener.exitConditionExpression(this);
		}
	}
}


export class IfStatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public conditionExpression(): ConditionExpressionContext {
		return this.getTypedRuleContext(ConditionExpressionContext, 0) as ConditionExpressionContext;
	}
	public block_list(): BlockContext[] {
		return this.getTypedRuleContexts(BlockContext) as BlockContext[];
	}
	public block(i: number): BlockContext {
		return this.getTypedRuleContext(BlockContext, i) as BlockContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_ifStatement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterIfStatement) {
	 		listener.enterIfStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitIfStatement) {
	 		listener.exitIfStatement(this);
		}
	}
}


export class WhileStatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public conditionExpression(): ConditionExpressionContext {
		return this.getTypedRuleContext(ConditionExpressionContext, 0) as ConditionExpressionContext;
	}
	public block(): BlockContext {
		return this.getTypedRuleContext(BlockContext, 0) as BlockContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_whileStatement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterWhileStatement) {
	 		listener.enterWhileStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitWhileStatement) {
	 		listener.exitWhileStatement(this);
		}
	}
}


export class AssignmentStatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public expression(): ExpressionContext {
		return this.getTypedRuleContext(ExpressionContext, 0) as ExpressionContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_assignmentStatement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterAssignmentStatement) {
	 		listener.enterAssignmentStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitAssignmentStatement) {
	 		listener.exitAssignmentStatement(this);
		}
	}
}


export class ForStatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public block(): BlockContext {
		return this.getTypedRuleContext(BlockContext, 0) as BlockContext;
	}
	public memoryAllocation(): MemoryAllocationContext {
		return this.getTypedRuleContext(MemoryAllocationContext, 0) as MemoryAllocationContext;
	}
	public conditionExpression(): ConditionExpressionContext {
		return this.getTypedRuleContext(ConditionExpressionContext, 0) as ConditionExpressionContext;
	}
	public assignmentStatement(): AssignmentStatementContext {
		return this.getTypedRuleContext(AssignmentStatementContext, 0) as AssignmentStatementContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_forStatement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterForStatement) {
	 		listener.enterForStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitForStatement) {
	 		listener.exitForStatement(this);
		}
	}
}


export class ReturnCallContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public expression(): ExpressionContext {
		return this.getTypedRuleContext(ExpressionContext, 0) as ExpressionContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_returnCall;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterReturnCall) {
	 		listener.enterReturnCall(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitReturnCall) {
	 		listener.exitReturnCall(this);
		}
	}
}


export class BreakStatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_breakStatement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterBreakStatement) {
	 		listener.enterBreakStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitBreakStatement) {
	 		listener.exitBreakStatement(this);
		}
	}
}


export class ContinueStatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_continueStatement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterContinueStatement) {
	 		listener.enterContinueStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitContinueStatement) {
	 		listener.exitContinueStatement(this);
		}
	}
}


export class ParametersContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public parameter_list(): ParameterContext[] {
		return this.getTypedRuleContexts(ParameterContext) as ParameterContext[];
	}
	public parameter(i: number): ParameterContext {
		return this.getTypedRuleContext(ParameterContext, i) as ParameterContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_parameters;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterParameters) {
	 		listener.enterParameters(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitParameters) {
	 		listener.exitParameters(this);
		}
	}
}


export class ParameterContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public type_(): TypeContext {
		return this.getTypedRuleContext(TypeContext, 0) as TypeContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_parameter;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterParameter) {
	 		listener.enterParameter(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitParameter) {
	 		listener.exitParameter(this);
		}
	}
}


export class ModifierContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public wordWithParameter(): WordWithParameterContext {
		return this.getTypedRuleContext(WordWithParameterContext, 0) as WordWithParameterContext;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_modifier;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterModifier) {
	 		listener.enterModifier(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitModifier) {
	 		listener.exitModifier(this);
		}
	}
}


export class TypeContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public WORD(): TerminalNode {
		return this.getToken(lunaParser.WORD, 0);
	}
	public type_(): TypeContext {
		return this.getTypedRuleContext(TypeContext, 0) as TypeContext;
	}
	public typeParameters(): TypeParametersContext {
		return this.getTypedRuleContext(TypeParametersContext, 0) as TypeParametersContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_type;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterType) {
	 		listener.enterType(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitType) {
	 		listener.exitType(this);
		}
	}
}


export class TypeParametersContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public type__list(): TypeContext[] {
		return this.getTypedRuleContexts(TypeContext) as TypeContext[];
	}
	public type_(i: number): TypeContext {
		return this.getTypedRuleContext(TypeContext, i) as TypeContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_typeParameters;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterTypeParameters) {
	 		listener.enterTypeParameters(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitTypeParameters) {
	 		listener.exitTypeParameters(this);
		}
	}
}


export class BlockContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public statement_list(): StatementContext[] {
		return this.getTypedRuleContexts(StatementContext) as StatementContext[];
	}
	public statement(i: number): StatementContext {
		return this.getTypedRuleContext(StatementContext, i) as StatementContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_block;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterBlock) {
	 		listener.enterBlock(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitBlock) {
	 		listener.exitBlock(this);
		}
	}
}


export class OperationStatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public ifStatement(): IfStatementContext {
		return this.getTypedRuleContext(IfStatementContext, 0) as IfStatementContext;
	}
	public whileStatement(): WhileStatementContext {
		return this.getTypedRuleContext(WhileStatementContext, 0) as WhileStatementContext;
	}
	public forStatement(): ForStatementContext {
		return this.getTypedRuleContext(ForStatementContext, 0) as ForStatementContext;
	}
	public breakStatement(): BreakStatementContext {
		return this.getTypedRuleContext(BreakStatementContext, 0) as BreakStatementContext;
	}
	public continueStatement(): ContinueStatementContext {
		return this.getTypedRuleContext(ContinueStatementContext, 0) as ContinueStatementContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_operationStatement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterOperationStatement) {
	 		listener.enterOperationStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitOperationStatement) {
	 		listener.exitOperationStatement(this);
		}
	}
}


export class StatementContext extends ParserRuleContext {
	constructor(parser?: lunaParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public memoryAllocation(): MemoryAllocationContext {
		return this.getTypedRuleContext(MemoryAllocationContext, 0) as MemoryAllocationContext;
	}
	public wordWithParameter(): WordWithParameterContext {
		return this.getTypedRuleContext(WordWithParameterContext, 0) as WordWithParameterContext;
	}
	public functionDeclaration(): FunctionDeclarationContext {
		return this.getTypedRuleContext(FunctionDeclarationContext, 0) as FunctionDeclarationContext;
	}
	public returnCall(): ReturnCallContext {
		return this.getTypedRuleContext(ReturnCallContext, 0) as ReturnCallContext;
	}
	public operationStatement(): OperationStatementContext {
		return this.getTypedRuleContext(OperationStatementContext, 0) as OperationStatementContext;
	}
    public get ruleIndex(): number {
    	return lunaParser.RULE_statement;
	}
	public enterRule(listener: lunaListener): void {
	    if(listener.enterStatement) {
	 		listener.enterStatement(this);
		}
	}
	public exitRule(listener: lunaListener): void {
	    if(listener.exitStatement) {
	 		listener.exitStatement(this);
		}
	}
}
