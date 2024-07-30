// Generated from /home/rickymal/Área de trabalho/libuv-backend/examples/luna.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MyLanguageLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		ID=18, INT=19, STRING=20, WS=21;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"ID", "INT", "STRING", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'var'", "'='", "';'", "'func'", "'('", "')'", "'type'", "'struct'", 
			"'{'", "'}'", "','", "'['", "']'", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "ID", "INT", "STRING", "WS"
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


	public MyLanguageLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "luna.g4"; }

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
		"\u0004\u0000\u0015v\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0005\u0011]\b\u0011\n\u0011"+
		"\f\u0011`\t\u0011\u0001\u0012\u0004\u0012c\b\u0012\u000b\u0012\f\u0012"+
		"d\u0001\u0013\u0001\u0013\u0005\u0013i\b\u0013\n\u0013\f\u0013l\t\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0004\u0014q\b\u0014\u000b\u0014"+
		"\f\u0014r\u0001\u0014\u0001\u0014\u0001j\u0000\u0015\u0001\u0001\u0003"+
		"\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011"+
		"\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010"+
		"!\u0011#\u0012%\u0013\'\u0014)\u0015\u0001\u0000\u0004\u0003\u0000AZ_"+
		"_az\u0004\u000009AZ__az\u0001\u000009\u0003\u0000\t\n\r\r  y\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000"+
		"\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0001+\u0001"+
		"\u0000\u0000\u0000\u0003/\u0001\u0000\u0000\u0000\u00051\u0001\u0000\u0000"+
		"\u0000\u00073\u0001\u0000\u0000\u0000\t8\u0001\u0000\u0000\u0000\u000b"+
		":\u0001\u0000\u0000\u0000\r<\u0001\u0000\u0000\u0000\u000fA\u0001\u0000"+
		"\u0000\u0000\u0011H\u0001\u0000\u0000\u0000\u0013J\u0001\u0000\u0000\u0000"+
		"\u0015L\u0001\u0000\u0000\u0000\u0017N\u0001\u0000\u0000\u0000\u0019P"+
		"\u0001\u0000\u0000\u0000\u001bR\u0001\u0000\u0000\u0000\u001dT\u0001\u0000"+
		"\u0000\u0000\u001fV\u0001\u0000\u0000\u0000!X\u0001\u0000\u0000\u0000"+
		"#Z\u0001\u0000\u0000\u0000%b\u0001\u0000\u0000\u0000\'f\u0001\u0000\u0000"+
		"\u0000)p\u0001\u0000\u0000\u0000+,\u0005v\u0000\u0000,-\u0005a\u0000\u0000"+
		"-.\u0005r\u0000\u0000.\u0002\u0001\u0000\u0000\u0000/0\u0005=\u0000\u0000"+
		"0\u0004\u0001\u0000\u0000\u000012\u0005;\u0000\u00002\u0006\u0001\u0000"+
		"\u0000\u000034\u0005f\u0000\u000045\u0005u\u0000\u000056\u0005n\u0000"+
		"\u000067\u0005c\u0000\u00007\b\u0001\u0000\u0000\u000089\u0005(\u0000"+
		"\u00009\n\u0001\u0000\u0000\u0000:;\u0005)\u0000\u0000;\f\u0001\u0000"+
		"\u0000\u0000<=\u0005t\u0000\u0000=>\u0005y\u0000\u0000>?\u0005p\u0000"+
		"\u0000?@\u0005e\u0000\u0000@\u000e\u0001\u0000\u0000\u0000AB\u0005s\u0000"+
		"\u0000BC\u0005t\u0000\u0000CD\u0005r\u0000\u0000DE\u0005u\u0000\u0000"+
		"EF\u0005c\u0000\u0000FG\u0005t\u0000\u0000G\u0010\u0001\u0000\u0000\u0000"+
		"HI\u0005{\u0000\u0000I\u0012\u0001\u0000\u0000\u0000JK\u0005}\u0000\u0000"+
		"K\u0014\u0001\u0000\u0000\u0000LM\u0005,\u0000\u0000M\u0016\u0001\u0000"+
		"\u0000\u0000NO\u0005[\u0000\u0000O\u0018\u0001\u0000\u0000\u0000PQ\u0005"+
		"]\u0000\u0000Q\u001a\u0001\u0000\u0000\u0000RS\u0005+\u0000\u0000S\u001c"+
		"\u0001\u0000\u0000\u0000TU\u0005-\u0000\u0000U\u001e\u0001\u0000\u0000"+
		"\u0000VW\u0005*\u0000\u0000W \u0001\u0000\u0000\u0000XY\u0005/\u0000\u0000"+
		"Y\"\u0001\u0000\u0000\u0000Z^\u0007\u0000\u0000\u0000[]\u0007\u0001\u0000"+
		"\u0000\\[\u0001\u0000\u0000\u0000]`\u0001\u0000\u0000\u0000^\\\u0001\u0000"+
		"\u0000\u0000^_\u0001\u0000\u0000\u0000_$\u0001\u0000\u0000\u0000`^\u0001"+
		"\u0000\u0000\u0000ac\u0007\u0002\u0000\u0000ba\u0001\u0000\u0000\u0000"+
		"cd\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000de\u0001\u0000\u0000"+
		"\u0000e&\u0001\u0000\u0000\u0000fj\u0005\"\u0000\u0000gi\t\u0000\u0000"+
		"\u0000hg\u0001\u0000\u0000\u0000il\u0001\u0000\u0000\u0000jk\u0001\u0000"+
		"\u0000\u0000jh\u0001\u0000\u0000\u0000km\u0001\u0000\u0000\u0000lj\u0001"+
		"\u0000\u0000\u0000mn\u0005\"\u0000\u0000n(\u0001\u0000\u0000\u0000oq\u0007"+
		"\u0003\u0000\u0000po\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000"+
		"rp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000st\u0001\u0000\u0000"+
		"\u0000tu\u0006\u0014\u0000\u0000u*\u0001\u0000\u0000\u0000\u0005\u0000"+
		"^djr\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}