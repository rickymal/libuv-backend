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
		T__17=18, WORD=19, INT=20, STRING=21, WS=22;
	public static final int
		RULE_program = 0, RULE_typeModifier = 1, RULE_allocatorSize = 2, RULE_expression = 3, 
		RULE_primaryExpression = 4, RULE_atom = 5, RULE_memoryAllocation = 6, 
		RULE_functionDeclaration = 7, RULE_anonymysFunctionDeclaration = 8, RULE_wordWithParameter = 9, 
		RULE_returnCall = 10, RULE_parameters = 11, RULE_parameter = 12, RULE_modifier = 13, 
		RULE_type = 14, RULE_typeParameters = 15, RULE_block = 16, RULE_statement = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "typeModifier", "allocatorSize", "expression", "primaryExpression", 
			"atom", "memoryAllocation", "functionDeclaration", "anonymysFunctionDeclaration", 
			"wordWithParameter", "returnCall", "parameters", "parameter", "modifier", 
			"type", "typeParameters", "block", "statement"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'const'", "'var'", "'i32'", "'i64'", "'+'", "'-'", "'*'", "'/'", 
			"'('", "')'", "'='", "';'", "'func'", "'return'", "','", "'void'", "'{'", 
			"'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "WORD", "INT", "STRING", "WS"
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
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 671750L) != 0)) {
				{
				{
				setState(36);
				statement();
				}
				}
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(42);
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
			setState(44);
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
			setState(46);
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
			setState(51);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(49);
				primaryExpression(0);
				}
				break;
			case 2:
				{
				setState(50);
				wordWithParameter();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(61);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(59);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(53);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(54);
						match(T__4);
						setState(55);
						expression(3);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(56);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(57);
						match(T__5);
						setState(58);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(63);
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
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(65);
				atom();
				}
				break;
			case 2:
				{
				setState(66);
				anonymysFunctionDeclaration();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(77);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(75);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(69);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(70);
						match(T__6);
						setState(71);
						primaryExpression(3);
						}
						break;
					case 2:
						{
						_localctx = new PrimaryExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_primaryExpression);
						setState(72);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(73);
						match(T__7);
						setState(74);
						primaryExpression(2);
						}
						break;
					}
					} 
				}
				setState(79);
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
			setState(87);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(80);
				match(INT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(81);
				match(STRING);
				}
				break;
			case WORD:
				enterOuterAlt(_localctx, 3);
				{
				setState(82);
				match(WORD);
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 4);
				{
				setState(83);
				match(T__8);
				setState(84);
				expression(0);
				setState(85);
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
			setState(89);
			typeModifier();
			setState(90);
			match(WORD);
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2 || _la==T__3) {
				{
				setState(91);
				allocatorSize();
				}
			}

			setState(94);
			match(T__10);
			setState(95);
			expression(0);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(96);
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
			{
			setState(100); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(99);
				modifier();
				}
				}
				setState(102); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WORD );
			}
			setState(104);
			match(T__12);
			setState(105);
			match(WORD);
			setState(106);
			match(T__8);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(107);
				parameters();
				}
			}

			setState(110);
			match(T__9);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 598040L) != 0)) {
				{
				setState(111);
				type();
				}
			}

			setState(114);
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
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(116);
				match(T__12);
				}
			}

			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(119);
				match(WORD);
				}
			}

			setState(122);
			match(T__8);
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WORD) {
				{
				setState(123);
				parameters();
				}
			}

			setState(126);
			match(T__9);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 598040L) != 0)) {
				{
				setState(127);
				type();
				}
			}

			setState(130);
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
		public TerminalNode INT() { return getToken(lunaParser.INT, 0); }
		public TerminalNode STRING() { return getToken(lunaParser.STRING, 0); }
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
			setState(132);
			match(WORD);
			setState(133);
			match(T__8);
			setState(134);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(135);
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
		enterRule(_localctx, 20, RULE_returnCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(T__13);
			setState(139);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(138);
				expression(0);
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
		enterRule(_localctx, 22, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			parameter();
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14) {
				{
				{
				setState(142);
				match(T__14);
				setState(143);
				parameter();
				}
				}
				setState(148);
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
		enterRule(_localctx, 24, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(WORD);
			setState(150);
			type();
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
		enterRule(_localctx, 26, RULE_modifier);
		try {
			setState(154);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(152);
				wordWithParameter();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(153);
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
		enterRule(_localctx, 28, RULE_type);
		int _la;
		try {
			setState(167);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				enterOuterAlt(_localctx, 1);
				{
				setState(156);
				match(T__2);
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 2);
				{
				setState(157);
				match(T__3);
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 3);
				{
				setState(158);
				match(T__15);
				}
				break;
			case WORD:
				enterOuterAlt(_localctx, 4);
				{
				setState(159);
				match(WORD);
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 5);
				{
				setState(160);
				match(T__12);
				setState(161);
				match(T__8);
				setState(163);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 598040L) != 0)) {
					{
					setState(162);
					typeParameters();
					}
				}

				setState(165);
				match(T__9);
				setState(166);
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
		enterRule(_localctx, 30, RULE_typeParameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			type();
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14) {
				{
				{
				setState(170);
				match(T__14);
				setState(171);
				type();
				}
				}
				setState(176);
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
		enterRule(_localctx, 32, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(T__16);
			setState(181);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 671750L) != 0)) {
				{
				{
				setState(178);
				statement();
				}
				}
				setState(183);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(184);
			match(T__17);
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
		public FunctionDeclarationContext functionDeclaration() {
			return getRuleContext(FunctionDeclarationContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ReturnCallContext returnCall() {
			return getRuleContext(ReturnCallContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_statement);
		try {
			setState(190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				memoryAllocation();
				}
				break;
			case WORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				functionDeclaration();
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 3);
				{
				setState(188);
				block();
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 4);
				{
				setState(189);
				returnCall();
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
		"\u0004\u0001\u0016\u00c1\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0005"+
		"\u0000&\b\u0000\n\u0000\f\u0000)\t\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u00034\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0005\u0003<\b\u0003\n\u0003\f\u0003?\t"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004D\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005"+
		"\u0004L\b\u0004\n\u0004\f\u0004O\t\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005X\b"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006]\b\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0003\u0006b\b\u0006\u0001\u0007\u0004"+
		"\u0007e\b\u0007\u000b\u0007\f\u0007f\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0003\u0007m\b\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"q\b\u0007\u0001\u0007\u0001\u0007\u0001\b\u0003\bv\b\b\u0001\b\u0003\b"+
		"y\b\b\u0001\b\u0001\b\u0003\b}\b\b\u0001\b\u0001\b\u0003\b\u0081\b\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0003"+
		"\n\u008c\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u0091\b\u000b"+
		"\n\u000b\f\u000b\u0094\t\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r"+
		"\u0003\r\u009b\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00a4\b\u000e\u0001\u000e\u0001"+
		"\u000e\u0003\u000e\u00a8\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005"+
		"\u000f\u00ad\b\u000f\n\u000f\f\u000f\u00b0\t\u000f\u0001\u0010\u0001\u0010"+
		"\u0005\u0010\u00b4\b\u0010\n\u0010\f\u0010\u00b7\t\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00bf"+
		"\b\u0011\u0001\u0011\u0000\u0002\u0006\b\u0012\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"\u0000"+
		"\u0003\u0001\u0000\u0001\u0002\u0001\u0000\u0003\u0004\u0001\u0000\u0014"+
		"\u0015\u00ce\u0000\'\u0001\u0000\u0000\u0000\u0002,\u0001\u0000\u0000"+
		"\u0000\u0004.\u0001\u0000\u0000\u0000\u00063\u0001\u0000\u0000\u0000\b"+
		"C\u0001\u0000\u0000\u0000\nW\u0001\u0000\u0000\u0000\fY\u0001\u0000\u0000"+
		"\u0000\u000ed\u0001\u0000\u0000\u0000\u0010u\u0001\u0000\u0000\u0000\u0012"+
		"\u0084\u0001\u0000\u0000\u0000\u0014\u0089\u0001\u0000\u0000\u0000\u0016"+
		"\u008d\u0001\u0000\u0000\u0000\u0018\u0095\u0001\u0000\u0000\u0000\u001a"+
		"\u009a\u0001\u0000\u0000\u0000\u001c\u00a7\u0001\u0000\u0000\u0000\u001e"+
		"\u00a9\u0001\u0000\u0000\u0000 \u00b1\u0001\u0000\u0000\u0000\"\u00be"+
		"\u0001\u0000\u0000\u0000$&\u0003\"\u0011\u0000%$\u0001\u0000\u0000\u0000"+
		"&)\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000\'(\u0001\u0000\u0000"+
		"\u0000(*\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000*+\u0005\u0000"+
		"\u0000\u0001+\u0001\u0001\u0000\u0000\u0000,-\u0007\u0000\u0000\u0000"+
		"-\u0003\u0001\u0000\u0000\u0000./\u0007\u0001\u0000\u0000/\u0005\u0001"+
		"\u0000\u0000\u000001\u0006\u0003\uffff\uffff\u000014\u0003\b\u0004\u0000"+
		"24\u0003\u0012\t\u000030\u0001\u0000\u0000\u000032\u0001\u0000\u0000\u0000"+
		"4=\u0001\u0000\u0000\u000056\n\u0002\u0000\u000067\u0005\u0005\u0000\u0000"+
		"7<\u0003\u0006\u0003\u000389\n\u0001\u0000\u00009:\u0005\u0006\u0000\u0000"+
		":<\u0003\u0006\u0003\u0002;5\u0001\u0000\u0000\u0000;8\u0001\u0000\u0000"+
		"\u0000<?\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=>\u0001\u0000"+
		"\u0000\u0000>\u0007\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000"+
		"@A\u0006\u0004\uffff\uffff\u0000AD\u0003\n\u0005\u0000BD\u0003\u0010\b"+
		"\u0000C@\u0001\u0000\u0000\u0000CB\u0001\u0000\u0000\u0000DM\u0001\u0000"+
		"\u0000\u0000EF\n\u0002\u0000\u0000FG\u0005\u0007\u0000\u0000GL\u0003\b"+
		"\u0004\u0003HI\n\u0001\u0000\u0000IJ\u0005\b\u0000\u0000JL\u0003\b\u0004"+
		"\u0002KE\u0001\u0000\u0000\u0000KH\u0001\u0000\u0000\u0000LO\u0001\u0000"+
		"\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\t\u0001"+
		"\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PX\u0005\u0014\u0000\u0000"+
		"QX\u0005\u0015\u0000\u0000RX\u0005\u0013\u0000\u0000ST\u0005\t\u0000\u0000"+
		"TU\u0003\u0006\u0003\u0000UV\u0005\n\u0000\u0000VX\u0001\u0000\u0000\u0000"+
		"WP\u0001\u0000\u0000\u0000WQ\u0001\u0000\u0000\u0000WR\u0001\u0000\u0000"+
		"\u0000WS\u0001\u0000\u0000\u0000X\u000b\u0001\u0000\u0000\u0000YZ\u0003"+
		"\u0002\u0001\u0000Z\\\u0005\u0013\u0000\u0000[]\u0003\u0004\u0002\u0000"+
		"\\[\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000"+
		"\u0000^_\u0005\u000b\u0000\u0000_a\u0003\u0006\u0003\u0000`b\u0005\f\u0000"+
		"\u0000a`\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000b\r\u0001\u0000"+
		"\u0000\u0000ce\u0003\u001a\r\u0000dc\u0001\u0000\u0000\u0000ef\u0001\u0000"+
		"\u0000\u0000fd\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000gh\u0001"+
		"\u0000\u0000\u0000hi\u0005\r\u0000\u0000ij\u0005\u0013\u0000\u0000jl\u0005"+
		"\t\u0000\u0000km\u0003\u0016\u000b\u0000lk\u0001\u0000\u0000\u0000lm\u0001"+
		"\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000np\u0005\n\u0000\u0000oq\u0003"+
		"\u001c\u000e\u0000po\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000"+
		"qr\u0001\u0000\u0000\u0000rs\u0003 \u0010\u0000s\u000f\u0001\u0000\u0000"+
		"\u0000tv\u0005\r\u0000\u0000ut\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000"+
		"\u0000vx\u0001\u0000\u0000\u0000wy\u0005\u0013\u0000\u0000xw\u0001\u0000"+
		"\u0000\u0000xy\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z|\u0005"+
		"\t\u0000\u0000{}\u0003\u0016\u000b\u0000|{\u0001\u0000\u0000\u0000|}\u0001"+
		"\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~\u0080\u0005\n\u0000\u0000"+
		"\u007f\u0081\u0003\u001c\u000e\u0000\u0080\u007f\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0003 \u0010\u0000\u0083\u0011\u0001\u0000\u0000\u0000\u0084"+
		"\u0085\u0005\u0013\u0000\u0000\u0085\u0086\u0005\t\u0000\u0000\u0086\u0087"+
		"\u0007\u0002\u0000\u0000\u0087\u0088\u0005\n\u0000\u0000\u0088\u0013\u0001"+
		"\u0000\u0000\u0000\u0089\u008b\u0005\u000e\u0000\u0000\u008a\u008c\u0003"+
		"\u0006\u0003\u0000\u008b\u008a\u0001\u0000\u0000\u0000\u008b\u008c\u0001"+
		"\u0000\u0000\u0000\u008c\u0015\u0001\u0000\u0000\u0000\u008d\u0092\u0003"+
		"\u0018\f\u0000\u008e\u008f\u0005\u000f\u0000\u0000\u008f\u0091\u0003\u0018"+
		"\f\u0000\u0090\u008e\u0001\u0000\u0000\u0000\u0091\u0094\u0001\u0000\u0000"+
		"\u0000\u0092\u0090\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000"+
		"\u0000\u0093\u0017\u0001\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000"+
		"\u0000\u0095\u0096\u0005\u0013\u0000\u0000\u0096\u0097\u0003\u001c\u000e"+
		"\u0000\u0097\u0019\u0001\u0000\u0000\u0000\u0098\u009b\u0003\u0012\t\u0000"+
		"\u0099\u009b\u0005\u0013\u0000\u0000\u009a\u0098\u0001\u0000\u0000\u0000"+
		"\u009a\u0099\u0001\u0000\u0000\u0000\u009b\u001b\u0001\u0000\u0000\u0000"+
		"\u009c\u00a8\u0005\u0003\u0000\u0000\u009d\u00a8\u0005\u0004\u0000\u0000"+
		"\u009e\u00a8\u0005\u0010\u0000\u0000\u009f\u00a8\u0005\u0013\u0000\u0000"+
		"\u00a0\u00a1\u0005\r\u0000\u0000\u00a1\u00a3\u0005\t\u0000\u0000\u00a2"+
		"\u00a4\u0003\u001e\u000f\u0000\u00a3\u00a2\u0001\u0000\u0000\u0000\u00a3"+
		"\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5"+
		"\u00a6\u0005\n\u0000\u0000\u00a6\u00a8\u0003\u001c\u000e\u0000\u00a7\u009c"+
		"\u0001\u0000\u0000\u0000\u00a7\u009d\u0001\u0000\u0000\u0000\u00a7\u009e"+
		"\u0001\u0000\u0000\u0000\u00a7\u009f\u0001\u0000\u0000\u0000\u00a7\u00a0"+
		"\u0001\u0000\u0000\u0000\u00a8\u001d\u0001\u0000\u0000\u0000\u00a9\u00ae"+
		"\u0003\u001c\u000e\u0000\u00aa\u00ab\u0005\u000f\u0000\u0000\u00ab\u00ad"+
		"\u0003\u001c\u000e\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ad\u00b0"+
		"\u0001\u0000\u0000\u0000\u00ae\u00ac\u0001\u0000\u0000\u0000\u00ae\u00af"+
		"\u0001\u0000\u0000\u0000\u00af\u001f\u0001\u0000\u0000\u0000\u00b0\u00ae"+
		"\u0001\u0000\u0000\u0000\u00b1\u00b5\u0005\u0011\u0000\u0000\u00b2\u00b4"+
		"\u0003\"\u0011\u0000\u00b3\u00b2\u0001\u0000\u0000\u0000\u00b4\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b8\u0001\u0000\u0000\u0000\u00b7\u00b5\u0001"+
		"\u0000\u0000\u0000\u00b8\u00b9\u0005\u0012\u0000\u0000\u00b9!\u0001\u0000"+
		"\u0000\u0000\u00ba\u00bf\u0003\f\u0006\u0000\u00bb\u00bf\u0003\u000e\u0007"+
		"\u0000\u00bc\u00bf\u0003 \u0010\u0000\u00bd\u00bf\u0003\u0014\n\u0000"+
		"\u00be\u00ba\u0001\u0000\u0000\u0000\u00be\u00bb\u0001\u0000\u0000\u0000"+
		"\u00be\u00bc\u0001\u0000\u0000\u0000\u00be\u00bd\u0001\u0000\u0000\u0000"+
		"\u00bf#\u0001\u0000\u0000\u0000\u0019\'3;=CKMW\\aflpux|\u0080\u008b\u0092"+
		"\u009a\u00a3\u00a7\u00ae\u00b5\u00be";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}