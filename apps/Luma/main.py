from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple, Union


import yaml

import dataclasses
from typing import Any, Dict

from IPython.terminal.shortcuts.auto_suggest import accept_and_move_cursor_left

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


def regex_finder(self: TokenTK, text: str) -> List[Tuple[int, int, str]]:
    matches = []
    for match in re.finditer(self.pattern, text):
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
        self.tokens: Dict[str, TokenTK] = {}

    def set_token(self, name: str, token_info: Dict[str, Any]):
        token = TokenTK(
            name=name,
            pattern=token_info.get('pattern', ''),
            is_primitive=token_info.get('is_primitive', False),
            is_owner=token_info.get('is_owner', False),
            personality=token_info.get('personality', None),
            contexts=list(token_info.get('contexts', ())),
            scan=None
        )

        from types import MethodType
        token.scan = MethodType(token_info.get("scan"), token)
        self.tokens[name] = token

    def get_token(self, name: str) -> Optional[TokenTK]:
        return self.tokens.get(name) or (self.parent.get_token(name) if self.parent else None)

    def set_variable(self, key: str, value: Any):
        self.variables[key] = value

    def get_variable(self, key: str) -> Any:
        return self.variables.get(key) or (self.parent.get_variable(key) if self.parent else None)




def process_code_recursively(code, token, start=0, batch_loading=1):
    """
    Processa o código recursivamente a partir do token atual.

    Args:
        code (str): O código a ser processado.
        token: O token atual que será processado.
        start (int): Posição inicial do intervalo de texto.
        batch_loading (int): Tamanho do intervalo a ser extraído.
    """
    # Extrair o intervalo de texto
    end = start + batch_loading
    i_code = code[start:end]

    # Se o texto está vazio, encerrar
    if not i_code:
        print("Texto vazio. Retornando.")
        return

    # Escanear e obter resultado
    result = token.scan(i_code)
    print(f"Token: {token}, Texto: '{i_code}', Resultado: {result}")

    # Associar o resultado ao token
    if result:
        token.value = result  # Associa o resultado ao token

        # Obter os próximos tokens possíveis
        next_tokens = token.ntokens
        print(f"Próximos tokens possíveis: {next_tokens}")

        # Se não houver mais tokens possíveis, encerrar
        if not next_tokens:
            print("Fim da árvore de tokens.")
            return

        # Para cada próximo token possível, explorar recursivamente
        for next_token in next_tokens:
            print(f"Explorando próximo token: {next_token}")
            process_code_recursively(code, next_token, start=end, batch_loading=batch_loading)
    else:
        # Expandir a janela de texto e tentar novamente
        print(f"Nenhum resultado para o token: {token}. Expansão da janela.")
        process_code_recursively(code, token, start, batch_loading + 1)

# Exemplo de Uso
if __name__ == "__main__":

    ctx = build_grammar(None)
    # tk_l = build_superficialize(ctx, "&TEST2")tk =
    tk_left: list[TokenTK] = compile_token(extract_token_from_context("&TEST4", ctx))

    # Processando o código
    code = "</></></>"
    process_code_recursively(code, tk_left[0], batch_loading=1)