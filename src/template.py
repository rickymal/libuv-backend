from lib import PatternMatcher, regex, regex_composer, skip_token, Query

def regex(ctx):
    # Implementação da transformação regex
    pass

def regex_composer(ctx):
    # Implementação do compositor de regex
    pass

# Padrões básicos
main = PatternMatcher(name = 'program', value = "pm:statementXML|pm:statementPackage", transform=regex_composer)

identifier = PatternMatcher(name='identifier', value = '', transform='regex')


main.register(
    PatternMatcher(name = 'statementXML', value = 'pm:open_tag pm:q_identifier pm:close_tag', transform=regex_composer)
    context='local'
)


code = """
<code>
    <wolfram.Math instance=[Ship, Algo] anotherParameter={name: "Henrique"} thirdParameter=<anotherXmlThing></anotherXmlThing>>
    </wolfram.Math>
</code>
"""

main.parse(code)
