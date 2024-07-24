// Generated from /home/rickymal/Área de trabalho/libuv-backend/malech.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class malechLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, COMMENT=11, COMMENT_SKIP=12, WS=13, ID=14, NUMBER=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "COMMENT", "COMMENT_SKIP", "WS", "ID", "NUMBER"
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


	public malechLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "malech.g4"; }

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
		"\u0004\u0000\u000fx\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0005\nI\b\n\n\n\f\nL\t\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\nT\b\n\n\n\f\nW\t\n\u0001\n\u0001\n\u0005"+
		"\n[\b\n\n\n\f\n^\t\n\u0003\n`\b\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0004\fg\b\f\u000b\f\f\fh\u0001\f\u0001\f\u0001\r"+
		"\u0001\r\u0005\ro\b\r\n\r\f\rr\t\r\u0001\u000e\u0004\u000eu\b\u000e\u000b"+
		"\u000e\f\u000ev\u0001J\u0000\u000f\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u0001\u0000\u0005\u0002"+
		"\u0000\n\n\r\r\u0003\u0000\t\n\r\r  \u0003\u0000AZ__az\u0004\u000009A"+
		"Z__az\u0001\u000009\u007f\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0001\u001f\u0001\u0000"+
		"\u0000\u0000\u0003$\u0001\u0000\u0000\u0000\u0005&\u0001\u0000\u0000\u0000"+
		"\u0007(\u0001\u0000\u0000\u0000\t*\u0001\u0000\u0000\u0000\u000b4\u0001"+
		"\u0000\u0000\u0000\r8\u0001\u0000\u0000\u0000\u000f:\u0001\u0000\u0000"+
		"\u0000\u0011@\u0001\u0000\u0000\u0000\u0013B\u0001\u0000\u0000\u0000\u0015"+
		"_\u0001\u0000\u0000\u0000\u0017a\u0001\u0000\u0000\u0000\u0019f\u0001"+
		"\u0000\u0000\u0000\u001bl\u0001\u0000\u0000\u0000\u001dt\u0001\u0000\u0000"+
		"\u0000\u001f \u0005f\u0000\u0000 !\u0005u\u0000\u0000!\"\u0005n\u0000"+
		"\u0000\"#\u0005c\u0000\u0000#\u0002\u0001\u0000\u0000\u0000$%\u0005(\u0000"+
		"\u0000%\u0004\u0001\u0000\u0000\u0000&\'\u0005)\u0000\u0000\'\u0006\u0001"+
		"\u0000\u0000\u0000()\u0005;\u0000\u0000)\b\u0001\u0000\u0000\u0000*+\u0005"+
		"i\u0000\u0000+,\u0005n\u0000\u0000,-\u0005t\u0000\u0000-.\u0005e\u0000"+
		"\u0000./\u0005r\u0000\u0000/0\u0005f\u0000\u000001\u0005a\u0000\u0000"+
		"12\u0005c\u0000\u000023\u0005e\u0000\u00003\n\u0001\u0000\u0000\u0000"+
		"45\u0005v\u0000\u000056\u0005a\u0000\u000067\u0005r\u0000\u00007\f\u0001"+
		"\u0000\u0000\u000089\u0005=\u0000\u00009\u000e\u0001\u0000\u0000\u0000"+
		":;\u0005c\u0000\u0000;<\u0005o\u0000\u0000<=\u0005n\u0000\u0000=>\u0005"+
		"s\u0000\u0000>?\u0005t\u0000\u0000?\u0010\u0001\u0000\u0000\u0000@A\u0005"+
		".\u0000\u0000A\u0012\u0001\u0000\u0000\u0000BC\u0005,\u0000\u0000C\u0014"+
		"\u0001\u0000\u0000\u0000DE\u0005/\u0000\u0000EF\u0005*\u0000\u0000FJ\u0001"+
		"\u0000\u0000\u0000GI\t\u0000\u0000\u0000HG\u0001\u0000\u0000\u0000IL\u0001"+
		"\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000"+
		"KM\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000MN\u0005*\u0000\u0000"+
		"N`\u0005/\u0000\u0000OP\u0005/\u0000\u0000PQ\u0005/\u0000\u0000QU\u0001"+
		"\u0000\u0000\u0000RT\b\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000TW\u0001"+
		"\u0000\u0000\u0000US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000"+
		"V`\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000X\\\u0005#\u0000\u0000"+
		"Y[\b\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000\u0000"+
		"\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]`\u0001\u0000\u0000"+
		"\u0000^\\\u0001\u0000\u0000\u0000_D\u0001\u0000\u0000\u0000_O\u0001\u0000"+
		"\u0000\u0000_X\u0001\u0000\u0000\u0000`\u0016\u0001\u0000\u0000\u0000"+
		"ab\u0003\u0015\n\u0000bc\u0001\u0000\u0000\u0000cd\u0006\u000b\u0000\u0000"+
		"d\u0018\u0001\u0000\u0000\u0000eg\u0007\u0001\u0000\u0000fe\u0001\u0000"+
		"\u0000\u0000gh\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001"+
		"\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000jk\u0006\f\u0000\u0000k\u001a"+
		"\u0001\u0000\u0000\u0000lp\u0007\u0002\u0000\u0000mo\u0007\u0003\u0000"+
		"\u0000nm\u0001\u0000\u0000\u0000or\u0001\u0000\u0000\u0000pn\u0001\u0000"+
		"\u0000\u0000pq\u0001\u0000\u0000\u0000q\u001c\u0001\u0000\u0000\u0000"+
		"rp\u0001\u0000\u0000\u0000su\u0007\u0004\u0000\u0000ts\u0001\u0000\u0000"+
		"\u0000uv\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000vw\u0001\u0000"+
		"\u0000\u0000w\u001e\u0001\u0000\u0000\u0000\b\u0000JU\\_hpv\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}