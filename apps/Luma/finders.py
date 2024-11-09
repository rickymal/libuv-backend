import re
import logging
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# Configurar o logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

class Prototype:
    """
    Classe que define constantes para controle de propagação em PrototypeContext.
    """
    ONLY_LOCAL = 1
    FORWARD = 2
    BACKWARD = 3
    GLOBAL = 4

class PrototypeContext:
    """
    Classe que representa um contexto com propagação de valores entre contextos pai e filho.
    """

    def __init__(self, name: str):
        """
        Inicializa um novo contexto.

        Args:
            name (str): Nome do contexto.
        """
        self.name: str = name
        self.data: Dict[str, Any] = dict()
        self.forward: Optional['PrototypeContext'] = None
        self.backward: Optional['PrototypeContext'] = None

    def get(self, key: str, default: Any = None, propagation: int = Prototype.ONLY_LOCAL) -> Any:
        """
        Obtém um valor do contexto com base na chave e no tipo de propagação.

        Args:
            key (str): Chave do valor a ser obtido.
            default (Any, opcional): Valor padrão caso a chave não seja encontrada.
            propagation (int, opcional): Tipo de propagação (ONLY_LOCAL, FORWARD, BACKWARD, GLOBAL).

        Returns:
            Any: Valor associado à chave ou o valor padrão.
        """
        value: Any = None
        if propagation == Prototype.ONLY_LOCAL:
            value = self.data.get(key, default)
        elif propagation == Prototype.FORWARD:
            value = self.data.get(key, None)
            if value is None and self.forward:
                return self.forward.get(key, default, propagation)
            value = value if value is not None else default
        elif propagation == Prototype.BACKWARD:
            value = self.data.get(key, None)
            if value is None and self.backward:
                return self.backward.get(key, default, propagation)
            value = value if value is not None else default
        elif propagation == Prototype.GLOBAL:
            # Busca tanto para trás quanto para frente
            value = self.data.get(key, None)
            if value is not None:
                return value
            if self.backward:
                value = self.backward.get(key, default, propagation)
                if value is not None:
                    return value
            if self.forward:
                value = self.forward.get(key, default, propagation)
                if value is not None:
                    return value
            value = default
        else:
            value = default

        logging.debug(f"Context get: key={key}, value={value}, context={self.name}")
        return value

    def set(self, key: str, value: Any) -> None:
        """
        Define um valor no contexto para uma determinada chave.

        Args:
            key (str): Chave onde o valor será armazenado.
            value (Any): Valor a ser armazenado.
        """
        logging.debug(f"Context set: key={key}, value={value}, context={self.name}")
        self.data[key] = value

    def append_child_context(self, name: str) -> 'PrototypeContext':
        """
        Cria e anexa um contexto filho a este contexto.

        Args:
            name (str): Nome do contexto filho.

        Returns:
            PrototypeContext: O contexto filho criado.
        """
        child_context = PrototypeContext(name)
        child_context.backward = self
        self.forward = child_context
        logging.debug(f"Context append_child: parent={self.name}, child={child_context.name}")
        return child_context

class Token:
    """
    Representa um token gerado durante a análise do texto.

    Atributos:
        start (int): Posição inicial do token.
        end (int): Posição final do token.
        name (str): Nome ou tipo do token.
        value (str): Valor do token.
        children (List[Token]): Lista de tokens filhos.
    """

    def __init__(self, start: int, end: int, name: str, value: str = '', children: Optional[List['Token']] = None):
        """
        Inicializa um novo token.

        Args:
            start (int): Posição inicial do token.
            end (int): Posição final do token.
            name (str): Nome ou tipo do token.
            value (str, opcional): Valor do token. Padrão é ''.
            children (List[Token], opcional): Tokens filhos. Padrão é None.
        """
        self.start: int = start
        self.end: int = end
        self.name: str = name
        self.value: str = value
        self.children: List['Token'] = children or []

    def to_yaml(self, indent: int = 0) -> str:
        """
        Converte o token e seus filhos em uma representação YAML.

        Args:
            indent (int, opcional): Nível de indentação. Padrão é 0.

        Returns:
            str: Representação YAML do token.
        """
        ind = '  ' * indent
        # Escapar caracteres especiais no valor
        value_escaped = self.value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        yaml_str = f"{ind}- name: {self.name}\n"
        yaml_str += f"{ind}  start: {self.start}\n"
        yaml_str += f"{ind}  end: {self.end}\n"
        yaml_str += f"{ind}  value: \"{value_escaped.strip()}\"\n"
        if self.children:
            yaml_str += f"{ind}  children:\n"
            for child in self.children:
                yaml_str += child.to_yaml(indent + 1)
        return yaml_str

    def to_mermaid(self, parent_id: Optional[int] = None, node_id: int = 0) -> Tuple[List[str], int]:
        """
        Converte o token e seus filhos em uma representação para diagramas Mermaid.

        Args:
            parent_id (Optional[int], opcional): ID do nó pai.
            node_id (int, opcional): ID do nó atual.

        Returns:
            Tuple[List[str], int]: Lista de linhas do diagrama e o próximo ID de nó.
        """
        lines: List[str] = []
        current_id = node_id
        # Escapar caracteres especiais no rótulo
        label = f"{self.name}: {self.value.strip()}"
        label = label.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        label = label.replace('[', '\\[').replace(']', '\\]').replace('<', '\\<').replace('>', '\\>')
        lines.append(f'id{current_id}["{label}"]')
        if parent_id is not None:
            lines.append(f'id{parent_id} --> id{current_id}')
        next_id = current_id + 1
        for child in self.children:
            child_lines, next_id = child.to_mermaid(parent_id=current_id, node_id=next_id)
            lines.extend(child_lines)
        return lines, next_id

    def __eq__(self, other: Any) -> bool:
        """
        Verifica se dois tokens são iguais.

        Args:
            other (Any): Outro objeto para comparação.

        Returns:
            bool: True se forem iguais, False caso contrário.
        """
        if not isinstance(other, Token):
            return False
        return (self.name == other.name and
                self.start == other.start and
                self.end == other.end and
                self.value == other.value and
                self.children == other.children)

    def __repr__(self) -> str:
        """
        Representação em string do token.

        Returns:
            str: Representação do token.
        """
        return (f"Token(name={self.name}, start={self.start}, end={self.end}, "
                f"value={self.value}, children={self.children})")

class Finder:
    """
    Classe base para todos os Finders (buscadores).
    """

    def __init__(self, on_find_token: Optional[List[Callable[['Token', 'PrototypeContext'], None]]] = None, pattern: str = '', name: str = ''):
        """
        Inicializa um Finder.

        Args:
            on_find_token (List[Callable], opcional): Lista de funções a serem chamadas quando um token for encontrado.
            pattern (str, opcional): Padrão a ser buscado.
            name (str, opcional): Nome do Finder.
        """
        self.on_find_token: List[Callable[['Token', 'PrototypeContext'], None]] = on_find_token or []
        self.pattern: str = pattern
        self.name: str = name

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Método base para escanear o texto. Deve ser implementado nas subclasses.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial. Padrão é 0.

        Returns:
            Tuple[Optional[Token], int]: Token encontrado e nova posição, ou (None, pos).
        """
        pass

class LiteralFinder(Finder):
    """
    Finder que busca por um padrão literal específico.
    """

    def __init__(self, on_find_token: Optional[List[Callable[['Token', 'PrototypeContext'], None]]] = None, pattern: str = '', name: str = ''):
        """
        Inicializa um LiteralFinder.

        Args:
            on_find_token (List[Callable], opcional): Funções de callback.
            pattern (str, opcional): Padrão literal a ser buscado.
            name (str, opcional): Nome do Finder.
        """
        super().__init__(on_find_token, pattern, name)

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto procurando pelo padrão literal.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Token encontrado e nova posição, ou (None, pos).
        """
        logging.debug(f"LiteralFinder scanning for '{self.pattern}' at position {pos}")
        if text.startswith(self.pattern, pos):
            start_pos = pos
            end_pos = pos + len(self.pattern)
            token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=self.pattern)
            for func in self.on_find_token:
                func(token, context)
            logging.debug(f"LiteralFinder found '{self.pattern}' from {start_pos} to {end_pos}")
            return token, end_pos
        else:
            logging.debug(f"LiteralFinder did not find '{self.pattern}' at position {pos}")
            return None, pos

class RegexFinder(Finder):
    """
    Finder que utiliza expressões regulares para buscar padrões no texto.
    """

    def __init__(self, on_find_token: Optional[List[Callable[['Token', 'PrototypeContext'], None]]] = None, pattern: str = '', name: str = ''):
        """
        Inicializa um RegexFinder.

        Args:
            on_find_token (List[Callable], opcional): Funções de callback.
            pattern (str, opcional): Expressão regular.
            name (str, opcional): Nome do Finder.
        """
        super().__init__(on_find_token, pattern, name)
        self.regex = re.compile(pattern, re.DOTALL)

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto usando a expressão regular.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Token encontrado e nova posição, ou (None, pos).
        """
        logging.debug(f"RegexFinder scanning with pattern '{self.pattern}' at position {pos}")
        m = self.regex.match(text, pos)
        if m:
            start_pos = pos
            end_pos = m.end()
            value = m.group()
            token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=value)
            for func in self.on_find_token:
                func(token, context)
            logging.debug(f"RegexFinder found '{value}' from {start_pos} to {end_pos}")
            return token, end_pos
        else:
            logging.debug(f"RegexFinder did not match at position {pos}")
            return None, pos

class ForwardFinder(Finder):
    """
    Finder que permite referência antecipada a outro Finder (forward declaration).
    """

    def __init__(self, name: str = ''):
        """
        Inicializa um ForwardFinder.

        Args:
            name (str, opcional): Nome do Finder.
        """
        super().__init__(name=name)
        self.target: Optional[Finder] = None

    def set_target(self, target: Finder) -> None:
        """
        Define o Finder alvo para o qual o ForwardFinder irá delegar.

        Args:
            target (Finder): Finder alvo.
        """
        self.target = target
        logging.debug(f"ForwardFinder '{self.name}' target set to '{target.name}'")

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto delegando ao Finder alvo.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Resultado do Finder alvo.
        """
        if self.target is None:
            raise ValueError(f"ForwardFinder target not set for {self.name}")
        logging.debug(f"ForwardFinder '{self.name}' delegates to '{self.target.name}' at position {pos}")
        return self.target.scan(text, context, pos)

class PatternParser:
    """
    Parser para analisar a string de padrão e construir a árvore de Finders.
    """

    TOKEN_REGEX = re.compile(r"\s*(?:(\()|(\))|(\|)|(&\w+)|(\*)|(\?)|(\+)|('([^']*)')|(\S+))")
    # Adicionamos ('([^']*)') para capturar literais entre aspas simples.

    def __init__(self, pattern: str, context: PrototypeContext):
        """
        Inicializa um PatternParser.

        Args:
            pattern (str): Padrão a ser analisado.
            context (PrototypeContext): Contexto atual.
        """
        self.pattern: str = pattern
        self.context: PrototypeContext = context
        self.tokens: List[str] = []
        self.pos: int = 0
        self.current_token: Optional[str] = None

    def parse(self) -> Finder:
        """
        Analisa o padrão e retorna o Finder correspondente.

        Returns:
            Finder: Finder resultante do padrão analisado.
        """
        logging.debug(f"PatternParser parsing pattern: {self.pattern}")
        self.tokenize()
        self.next_token()
        return self.expression()

    def tokenize(self) -> None:
        """
        Tokeniza a string de padrão.
        """
        pos = 0
        while pos < len(self.pattern):
            m = self.TOKEN_REGEX.match(self.pattern, pos)
            if not m:
                raise SyntaxError(f"Unexpected character at position {pos}")
            pos = m.end()
            token: Optional[str] = None
            for group_num in range(1, m.lastindex + 1):
                token = m.group(group_num)
                if token is not None:
                    token = token.strip()
                    if token:
                        self.tokens.append(token)
                        logging.debug(f"Tokenized: '{token}'")
                    break

    def next_token(self) -> None:
        """
        Avança para o próximo token.
        """
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            self.pos += 1
            logging.debug(f"Next token: '{self.current_token}'")
        else:
            self.current_token = None
            logging.debug("No more tokens")

    def expression(self) -> Finder:
        """
        Analisa uma expressão.

        Returns:
            Finder: Finder resultante da expressão.
        """
        term = self.term()
        if self.current_token == '|':
            finders = [term]
            while self.current_token == '|':
                self.next_token()
                finders.append(self.term())
            logging.debug(f"Created AlternationFinder with {len(finders)} options")
            return AlternationFinder(finders, name='alternation')
        else:
            return term

    def term(self) -> Finder:
        """
        Analisa um termo.

        Returns:
            Finder: Finder resultante do termo.
        """
        factors: List[Finder] = []
        while self.current_token and self.current_token not in {')', '|'}:
            factor = self.factor()
            factors.append(factor)
        if len(factors) == 1:
            return factors[0]
        else:
            logging.debug(f"Created SequenceFinder with {len(factors)} factors")
            return SequenceFinder(factors, name='sequence')

    def factor(self) -> Finder:
        """
        Analisa um fator.

        Returns:
            Finder: Finder resultante do fator.
        """
        base = self.base()
        while self.current_token in {'*', '+', '?'}:
            quantifier = self.current_token
            self.next_token()
            base = QuantifierFinder(base, quantifier, name='quantifier')
            logging.debug(f"Applied quantifier '{quantifier}'")
        return base

    def base(self) -> Finder:
        """
        Analisa a base de um fator.

        Returns:
            Finder: Finder resultante da base.
        """
        if self.current_token == '(':
            self.next_token()
            expr = self.expression()
            if self.current_token != ')':
                raise SyntaxError("Expected ')'")
            self.next_token()
            return expr
        elif self.current_token.startswith('&'):
            token_name = self.current_token[1:]
            self.next_token()
            parser = self.context.get(f"PS:{token_name}", None)
            if parser is None:
                raise ValueError(f"Parser {token_name} not found in context")
            logging.debug(f"Referenced parser: '{token_name}'")
            return parser
        else:
            # Trata literais
            literal = self.current_token
            self.next_token()
            # Remover aspas simples se existirem
            if literal.startswith("'") and literal.endswith("'"):
                literal = literal[1:-1]
            logging.debug(f"Created LiteralFinder for '{literal}'")
            return LiteralFinder(pattern=literal, name='literal')

class QuantifierFinder(Finder):
    """
    Finder que aplica quantificadores (*, +, ?) a outro Finder.
    """

    def __init__(self, finder: Finder, quantifier: str, name: str = ''):
        """
        Inicializa um QuantifierFinder.

        Args:
            finder (Finder): Finder ao qual o quantificador será aplicado.
            quantifier (str): Quantificador ('*', '+', '?').
            name (str, opcional): Nome do Finder.
        """
        super().__init__(name=name)
        self.finder: Finder = finder
        self.quantifier: str = quantifier  # '*', '+', '?'

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto aplicando o quantificador ao Finder interno.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Token encontrado e nova posição, ou (None, pos).
        """
        logging.debug(f"QuantifierFinder '{self.quantifier}' scanning at position {pos}")
        start_pos = pos
        children: List[Token] = []
        if self.quantifier == '*':
            while True:
                token, new_pos = self.finder.scan(text, context, pos)
                if token is not None and new_pos > pos:
                    children.append(token)
                    pos = new_pos
                else:
                    break
            # Sempre retornar um token, mesmo se nenhuma ocorrência for encontrada
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            logging.debug(f"QuantifierFinder '*' matched {len(children)} times from {start_pos} to {pos}")
            return token, pos
        elif self.quantifier == '+':
            token, pos = self.finder.scan(text, context, pos)
            if token is None:
                logging.debug(f"QuantifierFinder '+' failed to match at position {pos}")
                return None, start_pos
            children.append(token)
            while True:
                token, new_pos = self.finder.scan(text, context, pos)
                if token is not None and new_pos > pos:
                    children.append(token)
                    pos = new_pos
                else:
                    break
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            logging.debug(f"QuantifierFinder '+' matched {len(children)} times from {start_pos} to {pos}")
            return token, pos
        elif self.quantifier == '?':
            token, new_pos = self.finder.scan(text, context, pos)
            if token is not None and new_pos > pos:
                children.append(token)
                pos = new_pos
            value = ''.join(child.value for child in children)
            token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
            logging.debug(f"QuantifierFinder '?' matched {len(children)} times from {start_pos} to {pos}")
            return token, pos
        else:
            raise ValueError(f"Unknown quantifier: {self.quantifier}")

class AlternationFinder(Finder):
    """
    Finder que representa a alternância entre múltiplos Finders (operador '|').
    """

    def __init__(self, finders: List[Finder], name: str = ''):
        """
        Inicializa um AlternationFinder.

        Args:
            finders (List[Finder]): Lista de Finders para alternar.
            name (str, opcional): Nome do Finder.
        """
        super().__init__(name=name)
        self.finders: List[Finder] = finders

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto tentando cada Finder em ordem.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Primeiro token encontrado e nova posição, ou (None, pos).
        """
        logging.debug(f"AlternationFinder scanning at position {pos}")
        for finder in self.finders:
            token, new_pos = finder.scan(text, context, pos)
            if token is not None:
                logging.debug(f"AlternationFinder matched '{finder.name}' at position {pos}")
                return token, new_pos
        logging.debug("AlternationFinder did not match any option")
        return None, pos

class SequenceFinder(Finder):
    """
    Finder que representa uma sequência de Finders (concatenação).
    """

    def __init__(self, finders: List[Finder], name: str = ''):
        """
        Inicializa um SequenceFinder.

        Args:
            finders (List[Finder]): Lista de Finders a serem concatenados.
            name (str, opcional): Nome do Finder.
        """
        super().__init__(name=name)
        self.finders: List[Finder] = finders

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto procurando a sequência completa.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Token da sequência e nova posição, ou (None, pos).
        """
        logging.debug(f"SequenceFinder scanning at position {pos}")
        start_pos = pos
        children: List[Token] = []
        for finder in self.finders:
            # Ignora espaços em branco antes de cada token
            while pos < len(text) and text[pos].isspace():
                pos += 1
            token, pos = finder.scan(text, context, pos)
            if token is None:
                logging.debug(f"SequenceFinder failed at '{finder.name}' starting at position {pos}")
                return None, start_pos
            children.append(token)
        end_pos = pos
        value = ''.join(child.value for child in children)
        token = Token(start=start_pos + 1, end=end_pos, name=self.name, value=value, children=children)
        return token, pos

def extract(token: Token, context: PrototypeContext) -> None:
    """
    Extrai o token e o armazena no contexto.

    Args:
        token (Token): Token a ser armazenado.
        context (PrototypeContext): Contexto onde o token será armazenado.
    """
    context.set('token', token)

def extract_tree(context: PrototypeContext) -> Optional[Token]:
    """
    Recupera o token armazenado no contexto.

    Args:
        context (PrototypeContext): Contexto de onde o token será recuperado.

    Returns:
        Optional[Token]: Token armazenado ou None.
    """
    return context.get('token')

# Implementação recursiva para listas e objetos

class ListParser(Finder):
    """
    Parser para analisar listas no formato '[valor1, valor2, ...]'.
    """

    def __init__(self, name: str = 'list'):
        """
        Inicializa um ListParser.

        Args:
            name (str, opcional): Nome do Parser.
        """
        super().__init__(name=name)

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto procurando uma lista.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Token da lista e nova posição, ou (None, pos).
        """
        logging.debug(f"ListParser scanning at position {pos}")
        if pos >= len(text) or text[pos] != '[':
            return None, pos
        start_pos = pos
        pos += 1  # Pula '['
        children: List[Token] = []
        while pos < len(text):
            # Ignora espaços em branco
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Verifica se é o fechamento ']'
            if pos < len(text) and text[pos] == ']':
                pos += 1  # Pula ']'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ListParser found empty list at positions {start_pos}-{pos}")
                return token, pos
            # Tenta analisar um valor
            value_parser: Optional[Finder] = context.get('PS:VALUE')
            if value_parser is None:
                raise ValueError("Value parser 'PS:VALUE' not found in context")
            token, pos = value_parser.scan(text, context, pos)
            if token is None:
                logging.debug(f"ListParser failed to parse value at position {pos}")
                return None, start_pos
            children.append(token)
            # Ignora espaços em branco
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Verifica ',' ou ']'
            if pos < len(text) and text[pos] == ',':
                pos += 1  # Pula ','
            elif pos < len(text) and text[pos] == ']':
                pos += 1  # Pula ']'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ListParser parsed list from positions {start_pos}-{pos}")
                return token, pos
            else:
                logging.debug(f"ListParser expected ',' or ']' at position {pos}")
                return None, start_pos
        logging.debug("ListParser reached end of text without closing ']'")
        return None, start_pos

class ObjectParser(Finder):
    """
    Parser para analisar objetos no formato '{atributo1, atributo2, ...}'.
    """

    def __init__(self, name: str = 'object'):
        """
        Inicializa um ObjectParser.

        Args:
            name (str, opcional): Nome do Parser.
        """
        super().__init__(name=name)

    def scan(self, text: str, context: PrototypeContext, pos: int = 0) -> Tuple[Optional[Token], int]:
        """
        Escaneia o texto procurando um objeto.

        Args:
            text (str): Texto a ser escaneado.
            context (PrototypeContext): Contexto atual.
            pos (int, opcional): Posição inicial.

        Returns:
            Tuple[Optional[Token], int]: Token do objeto e nova posição, ou (None, pos).
        """
        logging.debug(f"ObjectParser scanning at position {pos}")
        if pos >= len(text) or text[pos] != '{':
            return None, pos
        start_pos = pos
        pos += 1  # Pula '{'
        children: List[Token] = []
        while pos < len(text):
            # Ignora espaços em branco
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Verifica se é o fechamento '}'
            if pos < len(text) and text[pos] == '}':
                pos += 1  # Pula '}'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ObjectParser found empty object at positions {start_pos}-{pos}")
                return token, pos
            # Tenta analisar um atributo
            attribute_parser: Optional[Finder] = context.get('PS:ATTRIBUTE')
            if attribute_parser is None:
                raise ValueError("Attribute parser 'PS:ATTRIBUTE' not found in context")
            token, pos = attribute_parser.scan(text, context, pos)
            if token is None:
                logging.debug(f"ObjectParser failed to parse attribute at position {pos}")
                return None, start_pos
            children.append(token)
            # Ignora espaços em branco
            while pos < len(text) and text[pos].isspace():
                pos += 1
            # Verifica ',' ou '}'
            if pos < len(text) and text[pos] == ',':
                pos += 1  # Pula ','
            elif pos < len(text) and text[pos] == '}':
                pos += 1  # Pula '}'
                value = text[start_pos:pos]
                token = Token(start=start_pos + 1, end=pos, name=self.name, value=value, children=children)
                logging.debug(f"ObjectParser parsed object from positions {start_pos}-{pos}")
                return token, pos
            else:
                logging.debug(f"ObjectParser expected ',' or '}}' at position {pos}")
                return None, start_pos
        logging.debug("ObjectParser reached end of text without closing '}'")
        return None, start_pos
