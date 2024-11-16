from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple, Union


import yaml

import dataclasses
from typing import Any, Dict

from analyzier import analyze_pattern
from enums import Personality, PropagationType
from etc import *
import re

# Definição do Token
from dataclasses import field, dataclass
from typing import Callable, Dict, Any, List, Tuple, Optional, Union

from enums import Personality
from token_tk_base import TokenTK


def get_value(value: str, contexts: List['ParserContext']) -> Tuple[TokenTK, Optional['ParserContext']]:
    for ctx in contexts:
        value = value.replace('?',"")
        token = ctx.get_token(value)
        if token:
            return token, ctx
    raise ValueError(f"Token '{value}' não encontrado em nenhum contexto.")


def regex_finder(token_info: Dict[str, Any], text: str) -> List[Tuple[int, int, str]]:
    pattern = token_info['pattern']
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.end(), match.group()))
    return matches


def pattern_finder(pattern: str, text: str) -> List[Tuple[int, int, str]]:
    tokens = pattern.strip().split()
    return [(0, len(text), text)] if ' '.join(tokens) == text else []


def eof_finder(token_info: Dict[str, Any], text: str) -> List[Tuple[int, int, str]]:
    return [(0, 0, 'EOF')] if text == '' else []


def convert_to_dict(obj: Any) -> Any:
    """
    Converte um objeto dataclass para um dicionário de forma recursiva.
    Se o objeto não for uma dataclass, retorna o objeto como está.

    Args:
        obj (Any): O objeto a ser convertido.

    Returns:
        Any: O dicionário resultante ou o objeto original se não for uma dataclass.
    """
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    elif isinstance(obj, list):
        return [convert_to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_to_dict(value) for key, value in obj.items()}
    else:
        return obj


def export_dict_to_yaml_file(data: Dict[str, Any], file_path: str) -> None:
    """
    Exporta um dicionário para um arquivo YAML.

    Args:
        data (Dict[str, Any]): O dicionário a ser exportado.
        file_path (str): O caminho do arquivo onde o YAML será salvo.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)
        print(f"Dados exportados com sucesso para {file_path}")
    except Exception as e:
        print(f"Erro ao exportar para YAML: {e}")




# Definição do Contexto de Parsing
class ParserContext:
    def __init__(self, name: str = 'root', parent: Optional['ParserContext'] = None):
        self.name = name
        self.parent = parent
        self.variables: Dict[str, Any] = {}
        self.tokens: Dict[str, Token] = {}

    def set_token(self, name: str, token_info: Dict[str, Any]):
        token = TokenTK(
            name=name,
            pattern=token_info.get('pattern', ''),
            is_primitive=token_info.get('is_primitive', False),
            is_owner=token_info.get('is_owner', False),
            personality=token_info.get('personality', None),
            contexts=list(token_info.get('contexts', ())),
        )
        self.tokens[name] = token

    def get_token(self, name: str) -> Optional[TokenTK]:
        return self.tokens.get(name) or (self.parent.get_token(name) if self.parent else None)

    def set_variable(self, key: str, value: Any):
        self.variables[key] = value

    def get_variable(self, key: str) -> Any:
        return self.variables.get(key) or (self.parent.get_variable(key) if self.parent else None)



# Exemplo de Uso
if __name__ == "__main__":

    ctx = build_grammar(None)
    # tk_l = build_superficialize(ctx, "&TEST2")tk =
    tk_left: list[TokenTK] = compile_token(extract_token_from_context("&TEST3", ctx))

