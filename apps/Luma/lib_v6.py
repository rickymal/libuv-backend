


class Literal:
    def __init__(self, name: str, value: str) -> None:
        self.name = name 
        self.value = value

    def __repr__(self) -> str:
        return f"Literal({self.name},{self.value})"

class Pattern:
    def __init__(self, name: str, value: str) -> None:
        self.name = name :quit
        self.value = value 


class AndSelector:
    def __init__(self, *objects):
        self.objects = objects

    def compile(self, left_ch, right_ch):
        pass


class Rule:
    def literal(self, name: str, value: str):
        return Literal(name, value)

    def pattern(self, name: str, value: str):
        return Pattern(name, value)

    def and_(self, *objects):
        return AndSelector(*objects)

class Grammar:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"Grammar({self.name})"
    

    def extra(self, skips: list[str]):
        pass 

    
    def rule(self, name: str):
        return Rule()
    pass


