# main.py

from lib import PatternMatcher, regex, regex_composer, skip_token, Query

# Definição dos padrões básicos
letter_pattern = PatternMatcher(name='letter_pattern', value='[a-zA-Z_À-ÿ]', transform=regex)
digit_pattern = PatternMatcher(name='digit_pattern', value='[0-9]', transform=regex)

# Compondo um padrão que inclui letras ou dígitos
letter_or_digit = PatternMatcher(
    name='letter_or_digit',
    value="pm:letter_pattern|pm:digit_pattern",
    transform=regex_composer
)
letter_or_digit.register(letter_pattern, digit_pattern, context='local')

# Definição dos tokens
pattern_tokens = [
    PatternMatcher(name='OPEN_ELEMENT', value='<', transform=regex),
    PatternMatcher(name='CLOSE_ELEMENT', value='>', transform=regex),
    PatternMatcher(name='DIGIT', value=digit_pattern.value, transform=regex),
    PatternMatcher(name='SKIP', value='[\\r\\n\\t ]+', transform=skip_token),
    PatternMatcher(name='LETTER', value=letter_pattern.value, transform=regex),
    PatternMatcher(
        name='IDENTIFIER',
        value=f'{letter_pattern.value}({letter_or_digit.value})*',
        transform=regex
    ),
    PatternMatcher(
        name='Q_IDENTIFIER',
        value=f'{letter_pattern.value}({letter_or_digit.value})*(?:\\.{letter_pattern.value}({letter_or_digit.value})*)*',
        transform=regex
    ),
    PatternMatcher(name='EQUALS', value='=', transform=regex),
    PatternMatcher(name='OPEN_BRACKET', value='\\[', transform=regex),
    PatternMatcher(name='CLOSE_BRACKET', value='\\]', transform=regex),
    # Outros tokens...
]

# Criação do PatternMatcher principal
main = PatternMatcher(name='program', value="pm:statementXML|pm:statementNOSQL", transform=regex_composer)
main.register(*pattern_tokens, context='local-below')

# Definição e registro de statementXML
statementXML = PatternMatcher(
    name='statementXML',
    value="pm:OPEN_ELEMENT(pm:attributes)?pm:CLOSE_ELEMENT(pm:app)?pm:OPEN_ELEMENT/pm:CLOSE_ELEMENT",
    transform=regex_composer
)
main.register(statementXML, context='local')

# Definição e registro de statementNOSQL (exemplo simplificado)
statementNOSQL = PatternMatcher(
    name='statementNOSQL',
    value="pm:IDENTIFIER pm:EQUALS pm:IDENTIFIER",
    transform=regex_composer
)
main.register(statementNOSQL, context='local')

# Definição de 'app' (exemplo simplificado)
app = PatternMatcher(name='app', value="pm:IDENTIFIER", transform=regex_composer)
statementXML.register(app, context='local')

# Substituição do token 'SKIP' no contexto de statementXML
statementXML.replace(
    Query(pattern_matcher='SKIP'),
    PatternMatcher(name='SKIP', value='[\\r\\n\\t]+', transform=skip_token),
    context='local'
)

# Definição e registro de 'attributes'
attributes = PatternMatcher(
    name='attributes',
    value="(pm:Q_IDENTIFIER pm:EQUALS pm:Q_IDENTIFIER)(pm:Q_IDENTIFIER pm:EQUALS pm:Q_IDENTIFIER)*",
    transform=regex_composer
)
statementXML.register(attributes, context='local')

# Compilação dos padrões
main.compile()

# Exemplo de código para análise
code = "<wolfram.Math instance=Ship>\n    appContent\n</wolfram.Math>"

# Parsing do código
tokens = main.parse(code)

# Exibindo os tokens reconhecidos
for token in tokens:
    print(f"{token.name}: '{token.value}'")
