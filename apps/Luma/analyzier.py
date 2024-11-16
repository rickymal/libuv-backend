import re
from typing import Dict, Any, Tuple
from enum import Enum
import enums
from enums import PropagationType


def analyze_pattern(antlr_code: str, matcher) -> tuple[dict[str, bool | PropagationType], str]:
    # Regex para dividir padrão e operadores, incluindo operadores compostos como *?
    #antlr_code = &SLASH?
    #matcher = r"(.*|&?\w+)(\*\?|\*|\?|\?\*)?$"
    match = re.match(matcher, antlr_code)

    if not match:
        raise ValueError("Formato inválido de padrão!")

    # Extraindo partes
    # operator = None
    pattern, operator = match.groups()
    spl_pattern = []

    # Determinando se é um grupo
    is_group = pattern.startswith("(") and pattern.endswith(")")
    is_or = False
    is_identifier = pattern.startswith("&")
    if is_group:
        pattern = pattern[1:-1]  # Remove os parênteses
        g_pattern = pattern.split("|")
        is_or = len(g_pattern) > 1
        if is_or:
            spl_pattern = list(enumerate(pattern.split("|")))
        else:
            spl_pattern = list([0, idx] for idx in pattern.split(" "))
    elif is_identifier:
        pattern = pattern[1:]  # Remove o `&`
        spl_pattern = [[0, pattern]]




    # Determinando a propagação
    if operator == "*":
        propagation = enums.PropagationType.ONE_TO_MANY
    elif operator == "?":
        propagation = enums.PropagationType.ZERO_TO_ONE
    elif operator == "*?":
        propagation = enums.PropagationType.ZERO_TO_MANY
    else:
        propagation = enums.PropagationType.ONLY_ONE

    # Retorna os dados analisados
    return {
        'is_identifier': is_identifier,
        'is_group': is_group,
        'propagation': propagation,
        'is_or' : is_or,
    }, spl_pattern

if __name__ == "__main__":
    test_cases = [
        "(expr)*",
        "(expr)*?",
        "&identifier?",
        "identifier",
        "invalid_pattern",
    ]
    for test in test_cases:
        try:
            result, pattern = analyze_pattern(test)
            print(f"Input: {test}")
            print(f"Pattern: {pattern}")
            print(f"Analysis: {result}\n")
        except ValueError as e:
            print(f"Input: {test} - Error: {e}\n")