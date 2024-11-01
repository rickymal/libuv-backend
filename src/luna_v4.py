import re
from typing import List, Tuple, Union

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

    def find_regex_positions(self, pattern: str) -> List[Tuple[int, int, str]]:
        """Encontra todas as ocorrências de um padrão regex na string armazenada."""
        results = []
        matches = re.finditer(pattern, self.data)
        
        for match in matches:
            start, end = match.span()
            found_text = match.group()
            results.append((start, end, found_text))
        
        return results

    def find_substring_positions(self, substring: str) -> List[Tuple[int, int, str]]:
        """Encontra todas as ocorrências de uma substring na string armazenada."""
        results = []
        start = 0
        
        while start < len(self.data):
            start = self.data.find(substring, start)
            
            if start == -1:
                break
            
            end = start + len(substring)
            results.append((start, end, substring))
            start += 1
        
        return results


texto = "A temperatura está em 20 graus hoje e ontem estava em 18 graus."
ss = StringStreamer(texto)

# Busca por padrão regex
padrao = r"\b\d+\b"
resultados_regex = ss.find_regex_positions(padrao)
for inicio, fim, valor in resultados_regex:
    print(f"[Regex] Posição inicial: {inicio}, Posição final: {fim}, Valor encontrado: {valor}")

# Busca por substring
substring = "graus"
resultados_substring = ss.find_substring_positions(substring)
for inicio, fim, valor in resultados_substring:
    print(f"[Substring] Posição inicial: {inicio}, Posição final: {fim}, Valor encontrado: {valor}")
