import re
from typing import List, Dict, Union, Tuple

# Classe para ler dados e permitir slicing de strings ou streams
class StringStreamer:
    def __init__(self, data: Union[str, 'Stream']):
        if isinstance(data, str):
            self.data = data
        elif hasattr(data, 'read'):
            self.data = data.read()
        else:
            raise ValueError("O parâmetro deve ser uma string ou um stream com o método 'read'.")

    def get_slice(self, start: int, end: int) -> str:
        return self.data[start:end]


from typing import List, Dict, Union, Tuple, Callable

# Classe base para as funcionalidades comuns de busca
class BaseStringFinder:
    def __init__(self, data: Union[str, 'Stream'], on_find_token: Callable[[str], Tuple[List[str], Dict[str, Union[int, str]]]] = None):
        self.data = data if isinstance(data, str) else data.read() if hasattr(data, 'read') else None
        if self.data is None:
            raise ValueError("O parâmetro deve ser uma string ou um stream com o método 'read'.")
        
        # Callback para adicionar metadados personalizados
        self.on_find_token = on_find_token if on_find_token else lambda token: ([], {})

    def get_slice(self, start: int, end: int) -> str:
        return self.data[start:end]

    def _get_line_column(self, position: int) -> Tuple[int, int]:
        """Calcula a linha e coluna de um índice baseado no conteúdo."""
        line = 1
        last_newline_pos = -1
        for i, char in enumerate(self.data[:position]):
            if char == '\n':
                line += 1
                last_newline_pos = i
        column = position - last_newline_pos
        return line, column

    def _apply_callback(self, token: str) -> Dict[str, Union[int, str]]:
        """Aplica o callback e adiciona os metadados personalizados ao token."""
        args, kwargs = self.on_find_token(token)
        # Converte args em chaves com valores True
        metadata = {arg: None for arg in args}
        metadata.update(kwargs)
        return metadata



# Subclasse para busca com expressões regulares
class RegexFinder(BaseStringFinder):
    def __init__(self, data: str, on_find_token: Callable[[str], Tuple[List[str], Dict[str, int | str]]] = None, pattern = None):
        super().__init__(data, on_find_token)
        self.pattern = pattern


    def find_positions(self, pattern: str) -> List[Dict[str, Union[int, str]]]:
        """Encontra todas as ocorrências de um padrão regex na string armazenada."""
        pattern = self.pattern
        results = []
        matches = re.finditer(pattern, self.data)
        
        for match in matches:
            start, end = match.span()
            found_text = match.group()
            results.append({"start": start, "end": end, "value": found_text})
        
        return results

    def find_positions_with_line_column(self,) -> List[Dict[str, Union[int, str]]]:
        """Encontra todas as ocorrências de um padrão regex com informações de linha e coluna e metadados adicionais."""
        pattern = self.pattern
        results = []
        matches = re.finditer(pattern, self.data)
        
        for match in matches:
            start, end = match.span()
            start_line, start_column = self._get_line_column(start)
            end_line, end_column = self._get_line_column(end - 1)
            found_text = match.group()

            # Adiciona metadados personalizados
            metadata = self._apply_callback(found_text)
            token_info = {
                "start_line": start_line,
                "start_column": start_column,
                "end_line": end_line,
                "end_column": end_column,
                "value": found_text,
                **metadata  # Inclui os metadados personalizados no dicionário
            }
            results.append(token_info)
        
        return results

# Subclasse para busca de correspondências exatas de substring
class ExactMatchFinder(BaseStringFinder):
    def find_positions(self, substring: str) -> List[Dict[str, Union[int, str]]]:
        """Encontra todas as ocorrências de uma substring na string armazenada."""
        results = []
        start = 0
        
        while start < len(self.data):
            start = self.data.find(substring, start)
            
            if start == -1:
                break
            
            end = start + len(substring)
            
            results.append({"start": start, "end": end, "value": substring,})
            start += 1
        
        return results

    def find_positions_with_line_column(self, substring: str) -> List[Dict[str, Union[int, str]]]:
        """Encontra todas as ocorrências de uma substring com informações de linha e coluna."""
        results = []
        start = 0
        
        while start < len(self.data):
            start = self.data.find(substring, start)
            if start == -1:
                break
            
            end = start + len(substring)
            start_line, start_column = self._get_line_column(start)
            end_line, end_column = self._get_line_column(end - 1)
            results.append({
                "start_line": start_line,
                "start_column": start_column,
                "end_line": end_line,
                "end_column": end_column,
                "value": substring
            })
            start += 1
        
        return results


from typing import List, Dict, Union, Tuple

class SplitFinder(BaseStringFinder):
    def find_positions_with_line_column(self) -> List[Dict[str, Union[int, str]]]:
        """Divide o texto por espaços e encontra as informações de linha e coluna para cada segmento."""
        results = []
        start_position = 0
        for part in self.data.split(" "):
            if part:  # Ignora partes vazias, caso hajam múltiplos espaços
                start = start_position
                end = start + len(part)
                start_line, start_column = self._get_line_column(start)
                end_line, end_column = self._get_line_column(end - 1)
                


                results.append({
                    "start_line": start_line,
                    "start_column": start_column,
                    "end_line": end_line,
                    "end_column": end_column,
                    "value": part,
                    **self._apply_callback(part)
                })
                
            start_position += len(part) + 1  # Move para a próxima posição considerando o espaço

        return results

# Exemplo de uso com RegexFinder para encontrar caracteres especiais
text_complete = "A expressão usa &IDENTIFIER*, alternadores |, quantificadores * e ?."

# Callback para adicionar metadados
def add_meta(token: str):
    args = []
    kwargs = {}

    if "&" in token:
        args.append("is_identifier")
    
    if token.endswith("*"):
        args.append("is_infinity")

    if "|" in token:
        kwargs["is_alternator"] = True

    if "+" in token:
        args.append("has_plus")

    return args, kwargs

# Instância de RegexFinder com o callback on_find_token
regex_finder = RegexFinder(text_complete, on_find_token=add_meta, pattern = r"&\S+|[|*?()]")

# Padrão para capturar identificadores e caracteres especiais

resultados = regex_finder.find_positions_with_line_column()

# Exibindo os resultados com metadados personalizados
print("Tokens encontrados com metadados adicionais:")
for resultado in resultados:
    print(resultado)


# Instância de RegexFinder com o callback on_find_token
regex_finder = SplitFinder("&START &WHITESPACE+ (&MIDDLE1|&MIDDLE2) &WHITESPACE+ &END", on_find_token=add_meta)

# Padrão para capturar identificadores e caracteres especiais
resultados = regex_finder.find_positions_with_line_column()

# Exibindo os resultados com metadados personalizados
print("Tokens encontrados com metadados adicionais:")
for resultado in resultados:
    print(resultado)
