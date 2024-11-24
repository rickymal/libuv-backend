

def regex_finder(text: str, pattern: str) -> list[tuple[int, int, str]]:
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.end(), match.group()))
    return matches

open_bracket = lambda text: regex_finder(text, pattern="<")
slash = lambda text: regex_finder(text, pattern="/")
question = lambda text: regex_finder(text, pattern="?")
close_bracket = lambda text: regex_finder(text, pattern=">")
open_quote = lambda text: regex_finder(text, pattern="[")
close_quote = lambda text: regex_finder(text, pattern="]")
comma = lambda text: regex_finder(text, pattern=",")
open_key = lambda text: regex_finder(text, pattern="{")
close_key = lambda text: regex_finder(text, pattern="}")
two_dots = lambda text: regex_finder(text, pattern=":")
equal = lambda text: regex_finder(text, pattern="=")

identifier = lambda text: regex_finder(text, pattern="^[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*$")





from dataclasses import dataclass
@dataclass
class Token:
    name: str
    scan: callable
    zero: bool
    many: bool


class Chain:
    pass 

class Selector:

    def zip_with_offset(self, lst: list, offset: int):
        """
        Retorna um iterador zipado com deslocamento na lista.

        :param lst: Lista de elementos.
        :param offset: Número inteiro que define o deslocamento.
        :return: Iterador com valores zipados.
        """
        lst = tuple(lst)
        if offset <= 0 or offset > len(lst):
            raise ValueError("O deslocamento deve ser maior que 0 e menor ou igual ao tamanho da lista.")

        iterators = [lst[i:] for i in range(offset)]
        return zip(*iterators)
    pass

import pdb


@dataclass
class Chain:
    pos: int
    val: Selector | Token
    next: list[Chain]


input_ch = Chain()
outpu_ch = Chain()


class And(Selector):
    def __init__(self, *opt : Selector | Token,zero:bool = False, many: bool = False) -> None:
        self.opt = opt
        self.zero = zero
        self.many = many


    def compile(self, left_ch: Chain, right_ch: Chain):
        d_chns = [Chain(pos=idx + 1, val = val, next=[]) for idx, val in enumerate(self.opt)]
        r_chns = d_chns[::-1]
        
        for ch1, ch2 in self.zip_with_offset(d_chns, 2):
            ch1.next.append(ch2)

            if ch1.many:
                ch1.next.append(ch1)

        for ch1, ch2 in self.zip_with_offset(r_chns, 2):
            if ch1.zero:
                ch2.next.append(*ch1.next)

        if left_ch is not None:
            left_ch.next.append(d_chns[0])

        if right_ch is not None:
            d_chns[-1].next.append(right_ch)

        return left_ch


class Or(Selector):
    def __init__(self, *opt : Selector | Token,zero:bool = False, many: bool = False) -> None:
        self.opt = opt
        self.zero = zero
        self.many = many

    def compile(self, left_ch: Chain, right_ch: Chain):
        d_chns = [Chain(pos = 1, val = val, next = []) for val in self.opt]

        for ch in d_chns:
            left_ch.next.append(ch)
            ch.next.append(right_ch)

        return left_ch


class ZeroToMany(Selector):
    def __init__(self, *opt : Selector | Token,zero:bool = False, many: bool = False) -> None:
        self.opt = opt
        self.zero = zero
        self.many = many

    def compile(self, left_ch: Chain, right_ch: Chain):
        pdb.set_trace()
        pass

open_bracket_token = Token(name = "open_bracket", scan=open_bracket, zero = False, many = False)

root = None


identifier = Token(name = "identifier", scan=identifier, zero=False, many=False)

array_parser = And(
    open_quote,
    identifier,
    ZeroToMany(
        comma,
        identifier,
    ),
    close_quote,
    skip_chars = [" "] # Indica que espaço não será considerado para analise neste contexto e abaio
)


object_parser = And(
    open_key,
    identifier,
    two_dots,
    identifier,
    ZeroToMany(
        identifier,
        two_dots,
        identifier
    ),
    close_key
)

attributes = And(
    identifier,
    equal,
    Or(
        object_parser,
        array_parser,
        root,
        zero=True,
        many=True,
    ),
)


code = "<wolfram.Math instance=[Ship, Algo] anotherParameter={name: Henrique} thirdParameter=<anotherXmlThing></anotherXmlThing>>"





interval = 1
start = 0
for end in range(interval, len(code), interval):
    p_code = code[start:end]

    
    pass
