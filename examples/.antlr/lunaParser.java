// Generated from /home/rickymal/Área de trabalho/libuv-backend/examples/luna.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class lunaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, WORD=29, INT=30, STRING=31, WS=32;
	public static final int
		RULE_program = 0, RULE_typeModifier = 1, RULE_allocatorSize = 2, RULE_expression = 3, 
		RULE_primaryExpression = 4, RULE_atom = 5, RULE_memoryAllocation = 6, 
		RULE_functionDeclaration = 7, RULE_anonymysFunctionDeclaration = 8, RULE_wordWithParameter = 9, 
		RULE_conditionExpression = 10, RULE_ifStatement = 11, RULE_whileStatement = 12, 
		RULE_assignmentStatement = 13, RULE_forStatement = 14, RULE_returnCall = 15, 
		RULE_breakStatement = 16, RULE_continueStatement = 17, RULE_parameters = 18, 
		RULE_parameter = 19, RULE_modifier = 20, RULE_type = 21, RULE_typeParameters = 22, 
		RULE_block = 23, RULE_operationStatement = 24, RULE_statement = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "typeModifier", "allocatorSize", "expression", "primaryExpression", 
			"atom", "memoryAllocation", "functionDeclaration", "anonymysFunctionDeclaration", 
			"wordWithParameter", "conditionExpression", "ifStatement", "whileStatement", 
			"assignmentStatement", "forStatement", "returnCall", "breakStatement", 
			"continueStatement", "parameters", "parameter", "modifier", "type", "typeParameters", 
			"block", "operationStatement", "statement"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'const'", "'var'", "'i32'", "'i64'", "'+'", "'-'", "'*'", "'/'", 
			"'('", "')'", "'='", "';'", "'func'", "','", "'<'", "'>'", "'<='", "'>='", 
			"'if'", "'else'", "'while'", "'for'", "'return'", "'break'", "'continue'", 
			"'void'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "WORD", "INT", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "luna.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public lunaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(lunaParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 602415110L) != 0)) {
				{
				{
				setState(52);
				statement();
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(58);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeModifierContext extends ParserRuleContext {
		public TypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeModifier; }
	}

	public final TypeModifierContext typeModifier() throws RecognitionException {
		TypeModifierContext _localctx = new TypeModifierContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_typeModifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			_la = _input.LA(1);
			if ( !(_la==T__0 || _la==T__1) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AllocatorSizeContext extends ParserRuleContext {
		public AllocatorSizeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_allocatorSize; }
	}

	public final AllocatorSizeContext allocatorSize() throws RecognitionException {
		AllocatorSizeContext _localctx = new AllocatorSizeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_allocatorSize);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			_la = _input.LA(1);
			if ( !(_la==T__2 || _la==T__3) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public WordWithParameterContext wordWithParameter() {
			return getRuleContext(WordWithParameterContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(65);
				primaryExpression(0);
				}
				break;
			case 2:
				{
				setState(66);
				wordWithParameter();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(77);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(75);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(69);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(70);
						match(T__4);
						setState(71);
						expression(3);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(72);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(73);
						match(T__5);
						setState(74);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(79);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public AnonymysFunctionDeclarationContext anonymysFunctionDeclaration() {
			return getRuleContext(AnonymysFunctionDeclarationContext.class,0);
		}
		public List<PrimaryExpressionContext> primaryExpression() {
			return getRuleContexts(PrimaryExpressionContext.class);
		}
		public PrimaryExpressionContext primaryExpression(int i) {
			return getRuleContext(PrimaryExpressionContext.class,i);
		}
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		return primaryExpression(0);
	}

	private PrimaryExpressionContext primaryExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, _parentState);
		PrimaryExpressionContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_primaryExpression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(81);
				atom();
				}
				break;
			case 2:
				{
				setState(82);
				anonymysFunctionDeclaration();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(93);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(91);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(85);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(86);
						match(T__6);
						setState(87);
						primaryExpression(3);
						}
						break;
					case 2:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(88);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(89);
						match(T__7);
						setState(90);
						primaryExpression(2);
						}
						break;
					}
					} 
				}
				setState(95);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(lunaParser.INT, 0); }
		public TerminalNode STRING() { return getToken(lunaParser.STRING, 0); }
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_atom);
		try {
			setState(103);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				match(INT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(97);
				match(STRING);
				}
				break;
			case WORD:
				enterOuterAlt(_localctx, 3);
				{
				setState(98);
				match(WORD);
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 4);
				{
				setState(99);
				match(T__8);
				setState(100);
				expression(0);
				setState(101);
				match(T__9);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MemoryAllocationContext extends ParserRuleContext {
		public TypeModifierContext typeModifier() {
			return getRuleContext(TypeModifierContext.class,0);
		}
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AllocatorSizeContext allocatorSize() {
			return getRuleContext(AllocatorSizeContext.class,0);
		}
		public MemoryAllocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memoryAllocation; }
	}

	public final MemoryAllocationContext memoryAllocation() throws RecognitionException {
		MemoryAllocationContext _localctx = new MemoryAllocationContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_memoryAllocation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			typeModifier();
			setState(106);
			match(WORD);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2 || _la==T__3) {
				{
				setState(107);
				allocatorSize();
				}
			}

			setState(110);
			match(T__10);
			setState(111);
			expression(0);
			setState(113);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(112);
				match(T__11);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDeclarationContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public List<ModifierContext> modifier() {
			return getRuleContexts(ModifierContext.class);
		}
		public ModifierContext modifier(int i) {
			return getRuleContext(ModifierContext.class,i);
		}
		public FunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclaration; }
	}

	public final FunctionDeclarationContext functionDeclaration() throws RecognitionException {
		FunctionDeclarationContext _localctx = new FunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_functionDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(116); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(115);
					modifier();
					}
					}
					setState(118); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==WORD );
				}
			}

			setState(122);
			match(T__12);
			setState(123);
			match(WORD);
			setState(124);
			match(T__8);
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(125);
				parameters();
				}
			}

			setState(128);
			match(T__9);
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 603987992L) != 0)) {
				{
				setState(129);
				type();
				}
			}

			setState(132);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AnonymysFunctionDeclarationContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public AnonymysFunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_anonymysFunctionDeclaration; }
	}

	public final AnonymysFunctionDeclarationContext anonymysFunctionDeclaration() throws RecognitionException {
		AnonymysFunctionDeclarationContext _localctx = new AnonymysFunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_anonymysFunctionDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(134);
				match(T__12);
				}
			}

			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(137);
				match(WORD);
				}
			}

			setState(140);
			match(T__8);
			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(141);
				parameters();
				}
			}

			setState(144);
			match(T__9);
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 603987992L) != 0)) {
				{
				setState(145);
				type();
				}
			}

			setState(148);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WordWithParameterContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public WordWithParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wordWithParameter; }
	}

	public final WordWithParameterContext wordWithParameter() throws RecognitionException {
		WordWithParameterContext _localctx = new WordWithParameterContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_wordWithParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(WORD);
			setState(151);
			match(T__8);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3758105088L) != 0)) {
				{
				setState(152);
				expression(0);
				setState(157);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__13) {
					{
					{
					setState(153);
					match(T__13);
					setState(154);
					expression(0);
					}
					}
					setState(159);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(162);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionExpressionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ConditionExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionExpression; }
	}

	public final ConditionExpressionContext conditionExpression() throws RecognitionException {
		ConditionExpressionContext _localctx = new ConditionExpressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_conditionExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			expression(0);
			setState(165);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 491520L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(166);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public ConditionExpressionContext conditionExpression() {
			return getRuleContext(ConditionExpressionContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_ifStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(T__18);
			setState(169);
			conditionExpression();
			setState(170);
			block();
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__19) {
				{
				setState(171);
				match(T__19);
				setState(172);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public ConditionExpressionContext conditionExpression() {
			return getRuleContext(ConditionExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(T__20);
			setState(176);
			conditionExpression();
			setState(177);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentStatementContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentStatement; }
	}

	public final AssignmentStatementContext assignmentStatement() throws RecognitionException {
		AssignmentStatementContext _localctx = new AssignmentStatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_assignmentStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			match(WORD);
			setState(180);
			match(T__10);
			setState(181);
			expression(0);
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(182);
				match(T__11);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public MemoryAllocationContext memoryAllocation() {
			return getRuleContext(MemoryAllocationContext.class,0);
		}
		public ConditionExpressionContext conditionExpression() {
			return getRuleContext(ConditionExpressionContext.class,0);
		}
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			match(T__21);
			setState(186);
			match(T__8);
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0 || _la==T__1) {
				{
				setState(187);
				memoryAllocation();
				}
			}

			setState(190);
			match(T__11);
			setState(192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3758105088L) != 0)) {
				{
				setState(191);
				conditionExpression();
				}
			}

			setState(194);
			match(T__11);
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(195);
				assignmentStatement();
				}
			}

			setState(198);
			match(T__9);
			setState(199);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnCallContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnCall; }
	}

	public final ReturnCallContext returnCall() throws RecognitionException {
		ReturnCallContext _localctx = new ReturnCallContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_returnCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			match(T__22);
			setState(203);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(202);
				expression(0);
				}
				break;
			}
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(205);
				match(T__11);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakStatementContext extends ParserRuleContext {
		public BreakStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStatement; }
	}

	public final BreakStatementContext breakStatement() throws RecognitionException {
		BreakStatementContext _localctx = new BreakStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_breakStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(T__23);
			setState(209);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContinueStatementContext extends ParserRuleContext {
		public ContinueStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStatement; }
	}

	public final ContinueStatementContext continueStatement() throws RecognitionException {
		ContinueStatementContext _localctx = new ContinueStatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_continueStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(T__24);
			setState(212);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			parameter();
			setState(219);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__13) {
				{
				{
				setState(215);
				match(T__13);
				setState(216);
				parameter();
				}
				}
				setState(221);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(WORD);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 603987992L) != 0)) {
				{
				setState(223);
				type();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModifierContext extends ParserRuleContext {
		public WordWithParameterContext wordWithParameter() {
			return getRuleContext(WordWithParameterContext.class,0);
		}
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public ModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modifier; }
	}

	public final ModifierContext modifier() throws RecognitionException {
		ModifierContext _localctx = new ModifierContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_modifier);
		try {
			setState(228);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(226);
				wordWithParameter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(227);
				match(WORD);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(lunaParser.WORD, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TypeParametersContext typeParameters() {
			return getRuleContext(TypeParametersContext.class,0);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_type);
		int _la;
		try {
			setState(241);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				enterOuterAlt(_localctx, 1);
				{
				setState(230);
				match(T__2);
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 2);
				{
				setState(231);
				match(T__3);
				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 3);
				{
				setState(232);
				match(T__25);
				}
				break;
			case WORD:
				enterOuterAlt(_localctx, 4);
				{
				setState(233);
				match(WORD);
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 5);
				{
				setState(234);
				match(T__12);
				setState(235);
				match(T__8);
				setState(237);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 603987992L) != 0)) {
					{
					setState(236);
					typeParameters();
					}
				}

				setState(239);
				match(T__9);
				setState(240);
				type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeParametersContext extends ParserRuleContext {
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public TypeParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeParameters; }
	}

	public final TypeParametersContext typeParameters() throws RecognitionException {
		TypeParametersContext _localctx = new TypeParametersContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_typeParameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			type();
			setState(248);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__13) {
				{
				{
				setState(244);
				match(T__13);
				setState(245);
				type();
				}
				}
				setState(250);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			match(T__26);
			setState(255);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 602415110L) != 0)) {
				{
				{
				setState(252);
				statement();
				}
				}
				setState(257);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(258);
			match(T__27);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationStatementContext extends ParserRuleContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public BreakStatementContext breakStatement() {
			return getRuleContext(BreakStatementContext.class,0);
		}
		public ContinueStatementContext continueStatement() {
			return getRuleContext(ContinueStatementContext.class,0);
		}
		public OperationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operationStatement; }
	}

	public final OperationStatementContext operationStatement() throws RecognitionException {
		OperationStatementContext _localctx = new OperationStatementContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_operationStatement);
		try {
			setState(265);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__18:
				enterOuterAlt(_localctx, 1);
				{
				setState(260);
				ifStatement();
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 2);
				{
				setState(261);
				whileStatement();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 3);
				{
				setState(262);
				forStatement();
				}
				break;
			case T__23:
				enterOuterAlt(_localctx, 4);
				{
				setState(263);
				breakStatement();
				}
				break;
			case T__24:
				enterOuterAlt(_localctx, 5);
				{
				setState(264);
				continueStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public MemoryAllocationContext memoryAllocation() {
			return getRuleContext(MemoryAllocationContext.class,0);
		}
		public WordWithParameterContext wordWithParameter() {
			return getRuleContext(WordWithParameterContext.class,0);
		}
		public FunctionDeclarationContext functionDeclaration() {
			return getRuleContext(FunctionDeclarationContext.class,0);
		}
		public ReturnCallContext returnCall() {
			return getRuleContext(ReturnCallContext.class,0);
		}
		public OperationStatementContext operationStatement() {
			return getRuleContext(OperationStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_statement);
		try {
			setState(272);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(267);
				memoryAllocation();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(268);
				wordWithParameter();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(269);
				functionDeclaration();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(270);
				returnCall();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(271);
				operationStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 3:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 4:
			return primaryExpression_sempred((PrimaryExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean primaryExpression_sempred(PrimaryExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001 \u0113\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0001\u0000\u0005\u00006\b\u0000\n\u0000\f\u0000"+
		"9\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003D\b\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0005\u0003L\b\u0003\n\u0003\f\u0003O\t\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004T\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\\\b\u0004\n\u0004\f\u0004"+
		"_\t\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005h\b\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0003\u0006m\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006r\b\u0006\u0001\u0007\u0004\u0007u\b\u0007\u000b\u0007\f\u0007"+
		"v\u0003\u0007y\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0003\u0007\u007f\b\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u0083\b"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0003\b\u0088\b\b\u0001\b\u0003"+
		"\b\u008b\b\b\u0001\b\u0001\b\u0003\b\u008f\b\b\u0001\b\u0001\b\u0003\b"+
		"\u0093\b\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0005"+
		"\t\u009c\b\t\n\t\f\t\u009f\t\t\u0003\t\u00a1\b\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0003\u000b\u00ae\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00b8\b\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u00bd\b\u000e\u0001\u000e\u0001\u000e\u0003\u000e"+
		"\u00c1\b\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00c5\b\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0003\u000f\u00cc"+
		"\b\u000f\u0001\u000f\u0003\u000f\u00cf\b\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0005\u0012\u00da\b\u0012\n\u0012\f\u0012\u00dd\t\u0012\u0001"+
		"\u0013\u0001\u0013\u0003\u0013\u00e1\b\u0013\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u00e5\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00ee\b\u0015\u0001\u0015\u0001"+
		"\u0015\u0003\u0015\u00f2\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0005"+
		"\u0016\u00f7\b\u0016\n\u0016\f\u0016\u00fa\t\u0016\u0001\u0017\u0001\u0017"+
		"\u0005\u0017\u00fe\b\u0017\n\u0017\f\u0017\u0101\t\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0003"+
		"\u0018\u010a\b\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0003\u0019\u0111\b\u0019\u0001\u0019\u0000\u0002\u0006\b\u001a"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,.02\u0000\u0003\u0001\u0000\u0001\u0002\u0001\u0000"+
		"\u0003\u0004\u0001\u0000\u000f\u0012\u0127\u00007\u0001\u0000\u0000\u0000"+
		"\u0002<\u0001\u0000\u0000\u0000\u0004>\u0001\u0000\u0000\u0000\u0006C"+
		"\u0001\u0000\u0000\u0000\bS\u0001\u0000\u0000\u0000\ng\u0001\u0000\u0000"+
		"\u0000\fi\u0001\u0000\u0000\u0000\u000ex\u0001\u0000\u0000\u0000\u0010"+
		"\u0087\u0001\u0000\u0000\u0000\u0012\u0096\u0001\u0000\u0000\u0000\u0014"+
		"\u00a4\u0001\u0000\u0000\u0000\u0016\u00a8\u0001\u0000\u0000\u0000\u0018"+
		"\u00af\u0001\u0000\u0000\u0000\u001a\u00b3\u0001\u0000\u0000\u0000\u001c"+
		"\u00b9\u0001\u0000\u0000\u0000\u001e\u00c9\u0001\u0000\u0000\u0000 \u00d0"+
		"\u0001\u0000\u0000\u0000\"\u00d3\u0001\u0000\u0000\u0000$\u00d6\u0001"+
		"\u0000\u0000\u0000&\u00de\u0001\u0000\u0000\u0000(\u00e4\u0001\u0000\u0000"+
		"\u0000*\u00f1\u0001\u0000\u0000\u0000,\u00f3\u0001\u0000\u0000\u0000."+
		"\u00fb\u0001\u0000\u0000\u00000\u0109\u0001\u0000\u0000\u00002\u0110\u0001"+
		"\u0000\u0000\u000046\u00032\u0019\u000054\u0001\u0000\u0000\u000069\u0001"+
		"\u0000\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000\u0000\u0000"+
		"8:\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000:;\u0005\u0000\u0000"+
		"\u0001;\u0001\u0001\u0000\u0000\u0000<=\u0007\u0000\u0000\u0000=\u0003"+
		"\u0001\u0000\u0000\u0000>?\u0007\u0001\u0000\u0000?\u0005\u0001\u0000"+
		"\u0000\u0000@A\u0006\u0003\uffff\uffff\u0000AD\u0003\b\u0004\u0000BD\u0003"+
		"\u0012\t\u0000C@\u0001\u0000\u0000\u0000CB\u0001\u0000\u0000\u0000DM\u0001"+
		"\u0000\u0000\u0000EF\n\u0002\u0000\u0000FG\u0005\u0005\u0000\u0000GL\u0003"+
		"\u0006\u0003\u0003HI\n\u0001\u0000\u0000IJ\u0005\u0006\u0000\u0000JL\u0003"+
		"\u0006\u0003\u0002KE\u0001\u0000\u0000\u0000KH\u0001\u0000\u0000\u0000"+
		"LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000N\u0007\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PQ\u0006"+
		"\u0004\uffff\uffff\u0000QT\u0003\n\u0005\u0000RT\u0003\u0010\b\u0000S"+
		"P\u0001\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000T]\u0001\u0000\u0000"+
		"\u0000UV\n\u0002\u0000\u0000VW\u0005\u0007\u0000\u0000W\\\u0003\b\u0004"+
		"\u0003XY\n\u0001\u0000\u0000YZ\u0005\b\u0000\u0000Z\\\u0003\b\u0004\u0002"+
		"[U\u0001\u0000\u0000\u0000[X\u0001\u0000\u0000\u0000\\_\u0001\u0000\u0000"+
		"\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\t\u0001\u0000"+
		"\u0000\u0000_]\u0001\u0000\u0000\u0000`h\u0005\u001e\u0000\u0000ah\u0005"+
		"\u001f\u0000\u0000bh\u0005\u001d\u0000\u0000cd\u0005\t\u0000\u0000de\u0003"+
		"\u0006\u0003\u0000ef\u0005\n\u0000\u0000fh\u0001\u0000\u0000\u0000g`\u0001"+
		"\u0000\u0000\u0000ga\u0001\u0000\u0000\u0000gb\u0001\u0000\u0000\u0000"+
		"gc\u0001\u0000\u0000\u0000h\u000b\u0001\u0000\u0000\u0000ij\u0003\u0002"+
		"\u0001\u0000jl\u0005\u001d\u0000\u0000km\u0003\u0004\u0002\u0000lk\u0001"+
		"\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000"+
		"no\u0005\u000b\u0000\u0000oq\u0003\u0006\u0003\u0000pr\u0005\f\u0000\u0000"+
		"qp\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000r\r\u0001\u0000\u0000"+
		"\u0000su\u0003(\u0014\u0000ts\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000"+
		"\u0000vt\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wy\u0001\u0000"+
		"\u0000\u0000xt\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000yz\u0001"+
		"\u0000\u0000\u0000z{\u0005\r\u0000\u0000{|\u0005\u001d\u0000\u0000|~\u0005"+
		"\t\u0000\u0000}\u007f\u0003$\u0012\u0000~}\u0001\u0000\u0000\u0000~\u007f"+
		"\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0082"+
		"\u0005\n\u0000\u0000\u0081\u0083\u0003*\u0015\u0000\u0082\u0081\u0001"+
		"\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0084\u0001"+
		"\u0000\u0000\u0000\u0084\u0085\u0003.\u0017\u0000\u0085\u000f\u0001\u0000"+
		"\u0000\u0000\u0086\u0088\u0005\r\u0000\u0000\u0087\u0086\u0001\u0000\u0000"+
		"\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u008a\u0001\u0000\u0000"+
		"\u0000\u0089\u008b\u0005\u001d\u0000\u0000\u008a\u0089\u0001\u0000\u0000"+
		"\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000"+
		"\u0000\u008c\u008e\u0005\t\u0000\u0000\u008d\u008f\u0003$\u0012\u0000"+
		"\u008e\u008d\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000"+
		"\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0092\u0005\n\u0000\u0000\u0091"+
		"\u0093\u0003*\u0015\u0000\u0092\u0091\u0001\u0000\u0000\u0000\u0092\u0093"+
		"\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0095"+
		"\u0003.\u0017\u0000\u0095\u0011\u0001\u0000\u0000\u0000\u0096\u0097\u0005"+
		"\u001d\u0000\u0000\u0097\u00a0\u0005\t\u0000\u0000\u0098\u009d\u0003\u0006"+
		"\u0003\u0000\u0099\u009a\u0005\u000e\u0000\u0000\u009a\u009c\u0003\u0006"+
		"\u0003\u0000\u009b\u0099\u0001\u0000\u0000\u0000\u009c\u009f\u0001\u0000"+
		"\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000"+
		"\u0000\u0000\u009e\u00a1\u0001\u0000\u0000\u0000\u009f\u009d\u0001\u0000"+
		"\u0000\u0000\u00a0\u0098\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000"+
		"\u0000\u0000\u00a1\u00a2\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005\n\u0000"+
		"\u0000\u00a3\u0013\u0001\u0000\u0000\u0000\u00a4\u00a5\u0003\u0006\u0003"+
		"\u0000\u00a5\u00a6\u0007\u0002\u0000\u0000\u00a6\u00a7\u0003\u0006\u0003"+
		"\u0000\u00a7\u0015\u0001\u0000\u0000\u0000\u00a8\u00a9\u0005\u0013\u0000"+
		"\u0000\u00a9\u00aa\u0003\u0014\n\u0000\u00aa\u00ad\u0003.\u0017\u0000"+
		"\u00ab\u00ac\u0005\u0014\u0000\u0000\u00ac\u00ae\u0003.\u0017\u0000\u00ad"+
		"\u00ab\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae"+
		"\u0017\u0001\u0000\u0000\u0000\u00af\u00b0\u0005\u0015\u0000\u0000\u00b0"+
		"\u00b1\u0003\u0014\n\u0000\u00b1\u00b2\u0003.\u0017\u0000\u00b2\u0019"+
		"\u0001\u0000\u0000\u0000\u00b3\u00b4\u0005\u001d\u0000\u0000\u00b4\u00b5"+
		"\u0005\u000b\u0000\u0000\u00b5\u00b7\u0003\u0006\u0003\u0000\u00b6\u00b8"+
		"\u0005\f\u0000\u0000\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001"+
		"\u0000\u0000\u0000\u00b8\u001b\u0001\u0000\u0000\u0000\u00b9\u00ba\u0005"+
		"\u0016\u0000\u0000\u00ba\u00bc\u0005\t\u0000\u0000\u00bb\u00bd\u0003\f"+
		"\u0006\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000"+
		"\u0000\u0000\u00bd\u00be\u0001\u0000\u0000\u0000\u00be\u00c0\u0005\f\u0000"+
		"\u0000\u00bf\u00c1\u0003\u0014\n\u0000\u00c0\u00bf\u0001\u0000\u0000\u0000"+
		"\u00c0\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c2\u0001\u0000\u0000\u0000"+
		"\u00c2\u00c4\u0005\f\u0000\u0000\u00c3\u00c5\u0003\u001a\r\u0000\u00c4"+
		"\u00c3\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5"+
		"\u00c6\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005\n\u0000\u0000\u00c7\u00c8"+
		"\u0003.\u0017\u0000\u00c8\u001d\u0001\u0000\u0000\u0000\u00c9\u00cb\u0005"+
		"\u0017\u0000\u0000\u00ca\u00cc\u0003\u0006\u0003\u0000\u00cb\u00ca\u0001"+
		"\u0000\u0000\u0000\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00ce\u0001"+
		"\u0000\u0000\u0000\u00cd\u00cf\u0005\f\u0000\u0000\u00ce\u00cd\u0001\u0000"+
		"\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf\u001f\u0001\u0000"+
		"\u0000\u0000\u00d0\u00d1\u0005\u0018\u0000\u0000\u00d1\u00d2\u0005\f\u0000"+
		"\u0000\u00d2!\u0001\u0000\u0000\u0000\u00d3\u00d4\u0005\u0019\u0000\u0000"+
		"\u00d4\u00d5\u0005\f\u0000\u0000\u00d5#\u0001\u0000\u0000\u0000\u00d6"+
		"\u00db\u0003&\u0013\u0000\u00d7\u00d8\u0005\u000e\u0000\u0000\u00d8\u00da"+
		"\u0003&\u0013\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000\u00da\u00dd\u0001"+
		"\u0000\u0000\u0000\u00db\u00d9\u0001\u0000\u0000\u0000\u00db\u00dc\u0001"+
		"\u0000\u0000\u0000\u00dc%\u0001\u0000\u0000\u0000\u00dd\u00db\u0001\u0000"+
		"\u0000\u0000\u00de\u00e0\u0005\u001d\u0000\u0000\u00df\u00e1\u0003*\u0015"+
		"\u0000\u00e0\u00df\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000"+
		"\u0000\u00e1\'\u0001\u0000\u0000\u0000\u00e2\u00e5\u0003\u0012\t\u0000"+
		"\u00e3\u00e5\u0005\u001d\u0000\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000"+
		"\u00e4\u00e3\u0001\u0000\u0000\u0000\u00e5)\u0001\u0000\u0000\u0000\u00e6"+
		"\u00f2\u0005\u0003\u0000\u0000\u00e7\u00f2\u0005\u0004\u0000\u0000\u00e8"+
		"\u00f2\u0005\u001a\u0000\u0000\u00e9\u00f2\u0005\u001d\u0000\u0000\u00ea"+
		"\u00eb\u0005\r\u0000\u0000\u00eb\u00ed\u0005\t\u0000\u0000\u00ec\u00ee"+
		"\u0003,\u0016\u0000\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ed\u00ee\u0001"+
		"\u0000\u0000\u0000\u00ee\u00ef\u0001\u0000\u0000\u0000\u00ef\u00f0\u0005"+
		"\n\u0000\u0000\u00f0\u00f2\u0003*\u0015\u0000\u00f1\u00e6\u0001\u0000"+
		"\u0000\u0000\u00f1\u00e7\u0001\u0000\u0000\u0000\u00f1\u00e8\u0001\u0000"+
		"\u0000\u0000\u00f1\u00e9\u0001\u0000\u0000\u0000\u00f1\u00ea\u0001\u0000"+
		"\u0000\u0000\u00f2+\u0001\u0000\u0000\u0000\u00f3\u00f8\u0003*\u0015\u0000"+
		"\u00f4\u00f5\u0005\u000e\u0000\u0000\u00f5\u00f7\u0003*\u0015\u0000\u00f6"+
		"\u00f4\u0001\u0000\u0000\u0000\u00f7\u00fa\u0001\u0000\u0000\u0000\u00f8"+
		"\u00f6\u0001\u0000\u0000\u0000\u00f8\u00f9\u0001\u0000\u0000\u0000\u00f9"+
		"-\u0001\u0000\u0000\u0000\u00fa\u00f8\u0001\u0000\u0000\u0000\u00fb\u00ff"+
		"\u0005\u001b\u0000\u0000\u00fc\u00fe\u00032\u0019\u0000\u00fd\u00fc\u0001"+
		"\u0000\u0000\u0000\u00fe\u0101\u0001\u0000\u0000\u0000\u00ff\u00fd\u0001"+
		"\u0000\u0000\u0000\u00ff\u0100\u0001\u0000\u0000\u0000\u0100\u0102\u0001"+
		"\u0000\u0000\u0000\u0101\u00ff\u0001\u0000\u0000\u0000\u0102\u0103\u0005"+
		"\u001c\u0000\u0000\u0103/\u0001\u0000\u0000\u0000\u0104\u010a\u0003\u0016"+
		"\u000b\u0000\u0105\u010a\u0003\u0018\f\u0000\u0106\u010a\u0003\u001c\u000e"+
		"\u0000\u0107\u010a\u0003 \u0010\u0000\u0108\u010a\u0003\"\u0011\u0000"+
		"\u0109\u0104\u0001\u0000\u0000\u0000\u0109\u0105\u0001\u0000\u0000\u0000"+
		"\u0109\u0106\u0001\u0000\u0000\u0000\u0109\u0107\u0001\u0000\u0000\u0000"+
		"\u0109\u0108\u0001\u0000\u0000\u0000\u010a1\u0001\u0000\u0000\u0000\u010b"+
		"\u0111\u0003\f\u0006\u0000\u010c\u0111\u0003\u0012\t\u0000\u010d\u0111"+
		"\u0003\u000e\u0007\u0000\u010e\u0111\u0003\u001e\u000f\u0000\u010f\u0111"+
		"\u00030\u0018\u0000\u0110\u010b\u0001\u0000\u0000\u0000\u0110\u010c\u0001"+
		"\u0000\u0000\u0000\u0110\u010d\u0001\u0000\u0000\u0000\u0110\u010e\u0001"+
		"\u0000\u0000\u0000\u0110\u010f\u0001\u0000\u0000\u0000\u01113\u0001\u0000"+
		"\u0000\u0000$7CKMS[]glqvx~\u0082\u0087\u008a\u008e\u0092\u009d\u00a0\u00ad"+
		"\u00b7\u00bc\u00c0\u00c4\u00cb\u00ce\u00db\u00e0\u00e4\u00ed\u00f1\u00f8"+
		"\u00ff\u0109\u0110";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}