// Generated from /home/rickymal/Área de trabalho/libuv-backend/language.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class nostalgiaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, COMMENT=15, COMMENT_SKIP=16, 
		WS=17, ID=18, NUMBER=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "COMMENT", "COMMENT_SKIP", 
			"WS", "ID", "NUMBER"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'func'", "'('", "')'", "';'", "'interface'", "'var'", "'='", "'const'", 
			"'.'", "'data'", "'i32'", "'string'", "'IPrintable'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "COMMENT", "COMMENT_SKIP", "WS", "ID", "NUMBER"
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


	public nostalgiaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "language.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0013\u009b\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0005\u000el\b\u000e\n\u000e\f\u000eo\t\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000ew\b\u000e\n\u000e\f\u000ez\t\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000e~\b\u000e\n\u000e\f\u000e\u0081\t\u000e\u0003\u000e\u0083\b\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0004\u0010"+
		"\u008a\b\u0010\u000b\u0010\f\u0010\u008b\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0005\u0011\u0092\b\u0011\n\u0011\f\u0011\u0095\t\u0011"+
		"\u0001\u0012\u0004\u0012\u0098\b\u0012\u000b\u0012\f\u0012\u0099\u0001"+
		"m\u0000\u0013\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\u0001\u0000"+
		"\u0005\u0002\u0000\n\n\r\r\u0003\u0000\t\n\r\r  \u0003\u0000AZ__az\u0004"+
		"\u000009AZ__az\u0001\u000009\u00a2\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013"+
		"\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017"+
		"\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b"+
		"\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f"+
		"\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000"+
		"\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0001\'\u0001\u0000\u0000"+
		"\u0000\u0003,\u0001\u0000\u0000\u0000\u0005.\u0001\u0000\u0000\u0000\u0007"+
		"0\u0001\u0000\u0000\u0000\t2\u0001\u0000\u0000\u0000\u000b<\u0001\u0000"+
		"\u0000\u0000\r@\u0001\u0000\u0000\u0000\u000fB\u0001\u0000\u0000\u0000"+
		"\u0011H\u0001\u0000\u0000\u0000\u0013J\u0001\u0000\u0000\u0000\u0015O"+
		"\u0001\u0000\u0000\u0000\u0017S\u0001\u0000\u0000\u0000\u0019Z\u0001\u0000"+
		"\u0000\u0000\u001be\u0001\u0000\u0000\u0000\u001d\u0082\u0001\u0000\u0000"+
		"\u0000\u001f\u0084\u0001\u0000\u0000\u0000!\u0089\u0001\u0000\u0000\u0000"+
		"#\u008f\u0001\u0000\u0000\u0000%\u0097\u0001\u0000\u0000\u0000\'(\u0005"+
		"f\u0000\u0000()\u0005u\u0000\u0000)*\u0005n\u0000\u0000*+\u0005c\u0000"+
		"\u0000+\u0002\u0001\u0000\u0000\u0000,-\u0005(\u0000\u0000-\u0004\u0001"+
		"\u0000\u0000\u0000./\u0005)\u0000\u0000/\u0006\u0001\u0000\u0000\u0000"+
		"01\u0005;\u0000\u00001\b\u0001\u0000\u0000\u000023\u0005i\u0000\u0000"+
		"34\u0005n\u0000\u000045\u0005t\u0000\u000056\u0005e\u0000\u000067\u0005"+
		"r\u0000\u000078\u0005f\u0000\u000089\u0005a\u0000\u00009:\u0005c\u0000"+
		"\u0000:;\u0005e\u0000\u0000;\n\u0001\u0000\u0000\u0000<=\u0005v\u0000"+
		"\u0000=>\u0005a\u0000\u0000>?\u0005r\u0000\u0000?\f\u0001\u0000\u0000"+
		"\u0000@A\u0005=\u0000\u0000A\u000e\u0001\u0000\u0000\u0000BC\u0005c\u0000"+
		"\u0000CD\u0005o\u0000\u0000DE\u0005n\u0000\u0000EF\u0005s\u0000\u0000"+
		"FG\u0005t\u0000\u0000G\u0010\u0001\u0000\u0000\u0000HI\u0005.\u0000\u0000"+
		"I\u0012\u0001\u0000\u0000\u0000JK\u0005d\u0000\u0000KL\u0005a\u0000\u0000"+
		"LM\u0005t\u0000\u0000MN\u0005a\u0000\u0000N\u0014\u0001\u0000\u0000\u0000"+
		"OP\u0005i\u0000\u0000PQ\u00053\u0000\u0000QR\u00052\u0000\u0000R\u0016"+
		"\u0001\u0000\u0000\u0000ST\u0005s\u0000\u0000TU\u0005t\u0000\u0000UV\u0005"+
		"r\u0000\u0000VW\u0005i\u0000\u0000WX\u0005n\u0000\u0000XY\u0005g\u0000"+
		"\u0000Y\u0018\u0001\u0000\u0000\u0000Z[\u0005I\u0000\u0000[\\\u0005P\u0000"+
		"\u0000\\]\u0005r\u0000\u0000]^\u0005i\u0000\u0000^_\u0005n\u0000\u0000"+
		"_`\u0005t\u0000\u0000`a\u0005a\u0000\u0000ab\u0005b\u0000\u0000bc\u0005"+
		"l\u0000\u0000cd\u0005e\u0000\u0000d\u001a\u0001\u0000\u0000\u0000ef\u0005"+
		",\u0000\u0000f\u001c\u0001\u0000\u0000\u0000gh\u0005/\u0000\u0000hi\u0005"+
		"*\u0000\u0000im\u0001\u0000\u0000\u0000jl\t\u0000\u0000\u0000kj\u0001"+
		"\u0000\u0000\u0000lo\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000"+
		"mk\u0001\u0000\u0000\u0000np\u0001\u0000\u0000\u0000om\u0001\u0000\u0000"+
		"\u0000pq\u0005*\u0000\u0000q\u0083\u0005/\u0000\u0000rs\u0005/\u0000\u0000"+
		"st\u0005/\u0000\u0000tx\u0001\u0000\u0000\u0000uw\b\u0000\u0000\u0000"+
		"vu\u0001\u0000\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000"+
		"\u0000xy\u0001\u0000\u0000\u0000y\u0083\u0001\u0000\u0000\u0000zx\u0001"+
		"\u0000\u0000\u0000{\u007f\u0005#\u0000\u0000|~\b\u0000\u0000\u0000}|\u0001"+
		"\u0000\u0000\u0000~\u0081\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000"+
		"\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0083\u0001\u0000\u0000"+
		"\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0082g\u0001\u0000\u0000\u0000"+
		"\u0082r\u0001\u0000\u0000\u0000\u0082{\u0001\u0000\u0000\u0000\u0083\u001e"+
		"\u0001\u0000\u0000\u0000\u0084\u0085\u0003\u001d\u000e\u0000\u0085\u0086"+
		"\u0001\u0000\u0000\u0000\u0086\u0087\u0006\u000f\u0000\u0000\u0087 \u0001"+
		"\u0000\u0000\u0000\u0088\u008a\u0007\u0001\u0000\u0000\u0089\u0088\u0001"+
		"\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000\u008b\u0089\u0001"+
		"\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u008d\u0001"+
		"\u0000\u0000\u0000\u008d\u008e\u0006\u0010\u0000\u0000\u008e\"\u0001\u0000"+
		"\u0000\u0000\u008f\u0093\u0007\u0002\u0000\u0000\u0090\u0092\u0007\u0003"+
		"\u0000\u0000\u0091\u0090\u0001\u0000\u0000\u0000\u0092\u0095\u0001\u0000"+
		"\u0000\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000"+
		"\u0000\u0000\u0094$\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000"+
		"\u0000\u0096\u0098\u0007\u0004\u0000\u0000\u0097\u0096\u0001\u0000\u0000"+
		"\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099\u0097\u0001\u0000\u0000"+
		"\u0000\u0099\u009a\u0001\u0000\u0000\u0000\u009a&\u0001\u0000\u0000\u0000"+
		"\b\u0000mx\u007f\u0082\u008b\u0093\u0099\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}