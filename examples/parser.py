import re
import xml.etree.ElementTree as ET
from typing import List, Dict

def infer_patterns(examples: List[str], token_names: List[str]) -> Dict[str, str]:
    # Função simples para inferir padrões de token baseados em exemplos
    patterns = {}
    for token in token_names:
        token_values = []
        for example in examples:
            match = re.search(r'\b' + token + r'\b', example)
            if match:
                token_values.append(match.group())
        
        # Um placeholder simples para cada tipo de token encontrado
        if token_values:
            # Criação de um padrão baseado no conteúdo dos valores dos tokens
            token_pattern = r"(.*?)"  # Captura tudo de forma simples
            patterns[token] = token_pattern
    return patterns

def create_regex_from_patterns(token_patterns: Dict[str, str], token_names: List[str]) -> str:
    # Cria uma regex com base nos padrões de tokens inferidos
    regex_pattern = ""
    for token in token_names:
        token_placeholder = f"[{token}]"
        token_pattern = token_patterns.get(token, r".*?")
        regex_pattern += token_pattern
    return regex_pattern

def main():
    # Carregar e analisar o XML
    tree = ET.parse('statements.xml')
    root = tree.getroot()

    # Iterar sobre todos os elementos <statement>
    for statement in root.findall('statement'):
        # Extrair o nome do statement
        name = statement.find('name').text

        # Extrair o padrão do statement
        token_pattern = statement.find('token').text
        token_names = re.findall(r'\[([^\]]+)\]', token_pattern)

        print(f"Statement Name: {name}\n")

        examples_data = []

        # Extrair e processar os exemplos
        examples = statement.find('examples')
        for example in examples.findall('example'):
            example_text = example.text.strip()
            examples_data.append(example_text)

        # Inferir padrões dos tokens
        token_patterns = infer_patterns(examples_data, token_names)
        generated_regex = create_regex_from_patterns(token_patterns, token_names)

        print(f"Inferred Regex Pattern: {generated_regex}\n")
        print(f"Tokens and Patterns:")
        for token, pattern in token_patterns.items():
            print(f"{token}: {pattern}")

        print("\n")

if __name__ == "__main__":
    main()
