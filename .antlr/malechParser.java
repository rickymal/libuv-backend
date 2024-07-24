// Generated from /home/rickymal/Área de trabalho/libuv-backend/malech.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class malechParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, COMMENT=11, COMMENT_SKIP=12, WS=13, ID=14, NUMBER=15;
	public static final int
		RULE_program = 0, RULE_functionDeclaration = 1, RULE_memoryAllocationStatement = 2, 
		RULE_statement = 3, RULE_funcCall = 4, RULE_functionName = 5, RULE_variableName = 6, 
		RULE_typeName = 7, RULE_interfaceName = 8, RULE_functionParams = 9, RULE_returnType = 10, 
		RULE_type = 11, RULE_expression = 12, RULE_exprList = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "functionDeclaration", "memoryAllocationStatement", "statement", 
			"funcCall", "functionName", "variableName", "typeName", "interfaceName", 
			"functionParams", "returnType", "type", "expression", "exprList"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'func'", "'('", "')'", "';'", "'interface'", "'var'", "'='", "'const'", 
			"'.'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "COMMENT", 
			"COMMENT_SKIP", "WS", "ID", "NUMBER"
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
	public String getGrammarFileName() { return "malech.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public malechParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
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
			setState(29); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(28);
				statement();
				}
				}
				setState(31); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 16742L) != 0) );
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
		public FunctionNameContext functionName() {
			return getRuleContext(FunctionNameContext.class,0);
		}
		public FunctionParamsContext functionParams() {
			return getRuleContext(FunctionParamsContext.class,0);
		}
		public ReturnTypeContext returnType() {
			return getRuleContext(ReturnTypeContext.class,0);
		}
		public InterfaceNameContext interfaceName() {
			return getRuleContext(InterfaceNameContext.class,0);
		}
		public FunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclaration; }
	}

	public final FunctionDeclarationContext functionDeclaration() throws RecognitionException {
		FunctionDeclarationContext _localctx = new FunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_functionDeclaration);
		int _la;
		try {
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(33);
				match(T__0);
				setState(34);
				functionName();
				setState(35);
				match(T__1);
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(36);
					functionParams();
					}
				}

				setState(39);
				match(T__2);
				setState(41);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(40);
					returnType();
					}
					break;
				}
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(43);
					match(T__3);
					}
				}

				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				match(T__4);
				setState(47);
				interfaceName();
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(48);
					match(T__3);
					}
				}

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
	public static class MemoryAllocationStatementContext extends ParserRuleContext {
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public MemoryAllocationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memoryAllocationStatement; }
	}

	public final MemoryAllocationStatementContext memoryAllocationStatement() throws RecognitionException {
		MemoryAllocationStatementContext _localctx = new MemoryAllocationStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_memoryAllocationStatement);
		int _la;
		try {
			setState(70);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				match(T__5);
				setState(54);
				variableName();
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(55);
					type();
					}
				}

				setState(58);
				match(T__6);
				setState(59);
				expression();
				setState(61);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(60);
					match(T__3);
					}
				}

				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 2);
				{
				setState(63);
				match(T__7);
				setState(64);
				variableName();
				setState(65);
				match(T__6);
				setState(66);
				expression();
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(67);
					match(T__3);
					}
				}

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
		public MemoryAllocationStatementContext memoryAllocationStatement() {
			return getRuleContext(MemoryAllocationStatementContext.class,0);
		}
		public FuncCallContext funcCall() {
			return getRuleContext(FuncCallContext.class,0);
		}
		public FunctionDeclarationContext functionDeclaration() {
			return getRuleContext(FunctionDeclarationContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				memoryAllocationStatement();
				}
				break;
			case T__1:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				funcCall();
				}
				break;
			case T__0:
			case T__4:
				enterOuterAlt(_localctx, 3);
				{
				setState(74);
				functionDeclaration();
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
	public static class FuncCallContext extends ParserRuleContext {
		public FunctionNameContext functionName() {
			return getRuleContext(FunctionNameContext.class,0);
		}
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprListContext exprList() {
			return getRuleContext(ExprListContext.class,0);
		}
		public FuncCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcCall; }
	}

	public final FuncCallContext funcCall() throws RecognitionException {
		FuncCallContext _localctx = new FuncCallContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funcCall);
		int _la;
		try {
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(77);
					variableName();
					}
					break;
				case T__1:
					{
					setState(78);
					match(T__1);
					setState(79);
					expression();
					setState(80);
					match(T__2);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(84);
				match(T__8);
				setState(85);
				functionName();
				setState(92);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
				case 1:
					{
					setState(86);
					match(T__1);
					setState(88);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 49156L) != 0)) {
						{
						setState(87);
						exprList();
						}
					}

					setState(90);
					match(T__2);
					}
					break;
				case 2:
					{
					setState(91);
					exprList();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(94);
				functionName();
				setState(101);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(95);
					variableName();
					}
					break;
				case T__1:
					{
					setState(96);
					match(T__1);
					setState(98);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 49156L) != 0)) {
						{
						setState(97);
						exprList();
						}
					}

					setState(100);
					match(T__2);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
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
	public static class FunctionNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(malechParser.ID, 0); }
		public FunctionNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionName; }
	}

	public final FunctionNameContext functionName() throws RecognitionException {
		FunctionNameContext _localctx = new FunctionNameContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_functionName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(ID);
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
	public static class VariableNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(malechParser.ID, 0); }
		public VariableNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableName; }
	}

	public final VariableNameContext variableName() throws RecognitionException {
		VariableNameContext _localctx = new VariableNameContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_variableName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(ID);
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
	public static class TypeNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(malechParser.ID, 0); }
		public TypeNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeName; }
	}

	public final TypeNameContext typeName() throws RecognitionException {
		TypeNameContext _localctx = new TypeNameContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_typeName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(ID);
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
	public static class InterfaceNameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(malechParser.ID, 0); }
		public InterfaceNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_interfaceName; }
	}

	public final InterfaceNameContext interfaceName() throws RecognitionException {
		InterfaceNameContext _localctx = new InterfaceNameContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_interfaceName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(ID);
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
	public static class FunctionParamsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(malechParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public FunctionParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionParams; }
	}

	public final FunctionParamsContext functionParams() throws RecognitionException {
		FunctionParamsContext _localctx = new FunctionParamsContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_functionParams);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(ID);
			setState(114);
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
	public static class ReturnTypeContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ReturnTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnType; }
	}

	public final ReturnTypeContext returnType() throws RecognitionException {
		ReturnTypeContext _localctx = new ReturnTypeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_returnType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
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
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(malechParser.ID, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(ID);
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
		public TerminalNode NUMBER() { return getToken(malechParser.NUMBER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public FuncCallContext funcCall() {
			return getRuleContext(FuncCallContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expression);
		try {
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				match(NUMBER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				match(T__1);
				setState(122);
				expression();
				setState(123);
				match(T__2);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(125);
				funcCall();
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
	public static class ExprListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ExprListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprList; }
	}

	public final ExprListContext exprList() throws RecognitionException {
		ExprListContext _localctx = new ExprListContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_exprList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			expression();
			setState(133);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(129);
					match(T__9);
					setState(130);
					expression();
					}
					} 
				}
				setState(135);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
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

	public static final String _serializedATN =
		"\u0004\u0001\u000f\u0089\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0004\u0000\u001e\b\u0000"+
		"\u000b\u0000\f\u0000\u001f\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001&\b\u0001\u0001\u0001\u0001\u0001\u0003\u0001*\b\u0001\u0001"+
		"\u0001\u0003\u0001-\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u00012\b\u0001\u0003\u00014\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u00029\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		">\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002E\b\u0002\u0003\u0002G\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003L\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004S\b\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004Y\b\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004]\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004c\b\u0004\u0001\u0004\u0003\u0004f\b\u0004\u0003\u0004h\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u007f\b"+
		"\f\u0001\r\u0001\r\u0001\r\u0005\r\u0084\b\r\n\r\f\r\u0087\t\r\u0001\r"+
		"\u0000\u0000\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u0000\u0000\u008f\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u00023\u0001\u0000\u0000\u0000\u0004F\u0001\u0000\u0000\u0000\u0006K"+
		"\u0001\u0000\u0000\u0000\bg\u0001\u0000\u0000\u0000\ni\u0001\u0000\u0000"+
		"\u0000\fk\u0001\u0000\u0000\u0000\u000em\u0001\u0000\u0000\u0000\u0010"+
		"o\u0001\u0000\u0000\u0000\u0012q\u0001\u0000\u0000\u0000\u0014t\u0001"+
		"\u0000\u0000\u0000\u0016v\u0001\u0000\u0000\u0000\u0018~\u0001\u0000\u0000"+
		"\u0000\u001a\u0080\u0001\u0000\u0000\u0000\u001c\u001e\u0003\u0006\u0003"+
		"\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000"+
		"\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000"+
		" \u0001\u0001\u0000\u0000\u0000!\"\u0005\u0001\u0000\u0000\"#\u0003\n"+
		"\u0005\u0000#%\u0005\u0002\u0000\u0000$&\u0003\u0012\t\u0000%$\u0001\u0000"+
		"\u0000\u0000%&\u0001\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000\')\u0005"+
		"\u0003\u0000\u0000(*\u0003\u0014\n\u0000)(\u0001\u0000\u0000\u0000)*\u0001"+
		"\u0000\u0000\u0000*,\u0001\u0000\u0000\u0000+-\u0005\u0004\u0000\u0000"+
		",+\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-4\u0001\u0000\u0000"+
		"\u0000./\u0005\u0005\u0000\u0000/1\u0003\u0010\b\u000002\u0005\u0004\u0000"+
		"\u000010\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u000024\u0001\u0000"+
		"\u0000\u00003!\u0001\u0000\u0000\u00003.\u0001\u0000\u0000\u00004\u0003"+
		"\u0001\u0000\u0000\u000056\u0005\u0006\u0000\u000068\u0003\f\u0006\u0000"+
		"79\u0003\u0016\u000b\u000087\u0001\u0000\u0000\u000089\u0001\u0000\u0000"+
		"\u00009:\u0001\u0000\u0000\u0000:;\u0005\u0007\u0000\u0000;=\u0003\u0018"+
		"\f\u0000<>\u0005\u0004\u0000\u0000=<\u0001\u0000\u0000\u0000=>\u0001\u0000"+
		"\u0000\u0000>G\u0001\u0000\u0000\u0000?@\u0005\b\u0000\u0000@A\u0003\f"+
		"\u0006\u0000AB\u0005\u0007\u0000\u0000BD\u0003\u0018\f\u0000CE\u0005\u0004"+
		"\u0000\u0000DC\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EG\u0001"+
		"\u0000\u0000\u0000F5\u0001\u0000\u0000\u0000F?\u0001\u0000\u0000\u0000"+
		"G\u0005\u0001\u0000\u0000\u0000HL\u0003\u0004\u0002\u0000IL\u0003\b\u0004"+
		"\u0000JL\u0003\u0002\u0001\u0000KH\u0001\u0000\u0000\u0000KI\u0001\u0000"+
		"\u0000\u0000KJ\u0001\u0000\u0000\u0000L\u0007\u0001\u0000\u0000\u0000"+
		"MS\u0003\f\u0006\u0000NO\u0005\u0002\u0000\u0000OP\u0003\u0018\f\u0000"+
		"PQ\u0005\u0003\u0000\u0000QS\u0001\u0000\u0000\u0000RM\u0001\u0000\u0000"+
		"\u0000RN\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TU\u0005\t\u0000"+
		"\u0000U\\\u0003\n\u0005\u0000VX\u0005\u0002\u0000\u0000WY\u0003\u001a"+
		"\r\u0000XW\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000YZ\u0001\u0000"+
		"\u0000\u0000Z]\u0005\u0003\u0000\u0000[]\u0003\u001a\r\u0000\\V\u0001"+
		"\u0000\u0000\u0000\\[\u0001\u0000\u0000\u0000]h\u0001\u0000\u0000\u0000"+
		"^e\u0003\n\u0005\u0000_f\u0003\f\u0006\u0000`b\u0005\u0002\u0000\u0000"+
		"ac\u0003\u001a\r\u0000ba\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000"+
		"cd\u0001\u0000\u0000\u0000df\u0005\u0003\u0000\u0000e_\u0001\u0000\u0000"+
		"\u0000e`\u0001\u0000\u0000\u0000fh\u0001\u0000\u0000\u0000gR\u0001\u0000"+
		"\u0000\u0000g^\u0001\u0000\u0000\u0000h\t\u0001\u0000\u0000\u0000ij\u0005"+
		"\u000e\u0000\u0000j\u000b\u0001\u0000\u0000\u0000kl\u0005\u000e\u0000"+
		"\u0000l\r\u0001\u0000\u0000\u0000mn\u0005\u000e\u0000\u0000n\u000f\u0001"+
		"\u0000\u0000\u0000op\u0005\u000e\u0000\u0000p\u0011\u0001\u0000\u0000"+
		"\u0000qr\u0005\u000e\u0000\u0000rs\u0003\u0016\u000b\u0000s\u0013\u0001"+
		"\u0000\u0000\u0000tu\u0003\u0016\u000b\u0000u\u0015\u0001\u0000\u0000"+
		"\u0000vw\u0005\u000e\u0000\u0000w\u0017\u0001\u0000\u0000\u0000x\u007f"+
		"\u0005\u000f\u0000\u0000yz\u0005\u0002\u0000\u0000z{\u0003\u0018\f\u0000"+
		"{|\u0005\u0003\u0000\u0000|\u007f\u0001\u0000\u0000\u0000}\u007f\u0003"+
		"\b\u0004\u0000~x\u0001\u0000\u0000\u0000~y\u0001\u0000\u0000\u0000~}\u0001"+
		"\u0000\u0000\u0000\u007f\u0019\u0001\u0000\u0000\u0000\u0080\u0085\u0003"+
		"\u0018\f\u0000\u0081\u0082\u0005\n\u0000\u0000\u0082\u0084\u0003\u0018"+
		"\f\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0084\u0087\u0001\u0000\u0000"+
		"\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000"+
		"\u0000\u0086\u001b\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000"+
		"\u0000\u0013\u001f%),138=DFKRX\\beg~\u0085";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}