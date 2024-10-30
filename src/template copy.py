from lib import PatternMatcher, regex, regex_composer, skip_token, Query

def regex(ctx):
    # Implementação da transformação regex
    pass

def regex_composer(ctx):
    # Implementação do compositor de regex
    pass

# Padrões básicos
letter_pattern = PatternMatcher(name='letter_pattern', value='[a-zA-Z_À-ÿ]', transform=regex)
digit_pattern = PatternMatcher(name='digit_pattern', value='[0-9]', transform=regex)

letter_or_digit = PatternMatcher(
    name='letter_or_digit',
    value="pm:letter_pattern | pm:digit_pattern",
    transform=regex_composer
)
letter_or_digit.register(letter_pattern, digit_pattern, context='local')

pattern_tokens = [
    PatternMatcher(name='OPEN_ELEMENT', value='<', transform=None),
    PatternMatcher(name='CLOSE_ELEMENT', value='>', transform=None),
    PatternMatcher(name='DIGIT', value=digit_pattern.value, transform=regex),
    PatternMatcher(name='SKIP', value='[\\r\\n\\t ]+', transform=skip_token),
    PatternMatcher(name='LETTER', value=letter_pattern.value, transform=None),
    PatternMatcher(
        name='IDENTIFIER',
        value=f'{letter_pattern.value}{letter_or_digit.value}*',
        transform=regex
    ),
    PatternMatcher(
        name='Q_IDENTIFIER',
        value=f'{letter_pattern.value}{letter_or_digit.value}*(?:\\.{letter_pattern.value}{letter_or_digit.value}*)*',
        transform=regex
    ),
    PatternMatcher(name='EQUALS', value='=', transform=None),
    PatternMatcher(name='OPEN_BRACKET', value='\\[', transform=None),
    PatternMatcher(name='CLOSE_BRACKET', value='\\]', transform=None),
    # Outros tokens...
]

# Registro dos tokens no contexto apropriado
main = PatternMatcher(name='program', value="pm:statementXML | pm:statementNOSQL", transform=regex_composer)
main.register(*pattern_tokens, context='local-below')

# Definição e registro de statementXML
statementXML = PatternMatcher(
    name='statementXML',
    value="pm:OPEN_ELEMENT pm:attributes? pm:CLOSE_ELEMENT pm:app pm:CLOSE_ELEMENT",
    transform=regex_composer
)
main.register(statementXML, context='local')

# Definição e registro de statementNOSQL (se necessário)
statementNOSQL = PatternMatcher(name='statementNOSQL', value="...", transform=regex_composer)
main.register(statementNOSQL, context='local')

# Definição de 'app' (se necessário)
app = PatternMatcher(name='app', value="...", transform=regex_composer)
statementXML.register(app, context='local')

# Substituição do token 'SKIP' no contexto de statementXML, como é local significa que será aplicado só aqui.
statementXML.replace(
    Query(pattern_matcher='SKIP'),
    PatternMatcher(name='SKIP', value='[\\r\\n\\t]+', transform=skip_token),
    context='local'
)

# Definição e registro de 'attributes'
attributes = PatternMatcher(
    name='attributes',
    value="(pm:Q_IDENTIFIER pm:EQUALS pm:Q_IDENTIFIER) (pm:Q_IDENTIFIER pm:EQUALS pm:Q_IDENTIFIER)*",
    transform=regex_composer
)
statementXML.register(attributes, context='local')


code = """
<code>
    <wolfram.Math instance=[Ship, Algo] anotherParameter={name: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

main.parse(code)
