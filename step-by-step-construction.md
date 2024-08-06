- [ ] Criar o parser para as estruturas
- [ ] Começar a trabalhar com llvm, criando o interpretador e o parser
- [ ] Construir o parser para a linguagem, agora teremos interpretação de código e o parser de fato para cada exemplo criado
- [ ] preparar o kernel e fazer plugin para a linguagem no vscode
- [ ] Lançar e criar projetos de eng. naval nele de cálculo estrutural e criar um sistema de ERP, não seu ainda, talvez um crud

Criar uma linguagem de programação é uma tarefa fascinante e complexa. Para o MVP (Minimum Viable Product) de uma linguagem de programação, além de funções e estrutura de dados, há alguns outros componentes essenciais que você pode considerar. Vamos discutir as próximas etapas com foco nas funcionalidades básicas:

### 1. **Funções**

#### Definição de Funções
Você precisará definir como as funções são declaradas e chamadas. Isso inclui:

- **Declaração de Função:** Definir uma gramática para a declaração de funções, incluindo o nome da função, parâmetros, tipo de retorno (se houver) e corpo da função.
- **Chamada de Função:** Definir como as funções são chamadas, incluindo a passagem de argumentos.

Exemplo básico de gramática para funções:

```antlr
functionDeclaration: 'fn' WORD '(' parameters? ')' '{' statement* '}';
parameters: parameter (',' parameter)*;
parameter: type WORD;
type: 'int' | 'string' | 'void' | 'float' | /* outros tipos */;
functionCall: WORD '(' arguments? ')';
arguments: expression (',' expression)*;
```

### 2. **Estrutura de Dados**

#### Tipos Primitivos e Compostos
Definir tipos de dados básicos e compostos, como:

- **Tipos Primitivos:** Inteiros, floats, strings, booleans.
- **Tipos Compostos:** Arrays, listas, tuplas, estruturas (structs).

Exemplo básico de gramática para tipos de dados:

```antlr
type: 'int' | 'float' | 'string' | 'bool' | 'array' '<' type '>' | 'struct' '{' structFields '}';
structFields: type WORD (',' type WORD)*;
```

#### Declaração e Uso de Variáveis
Incluir regras para a declaração e inicialização de variáveis, além de como elas podem ser usadas em expressões.

### 3. **Controle de Fluxo**

#### Estruturas de Controle de Fluxo
Incluir estruturas básicas de controle de fluxo, como:

- **Condicionais:** `if`, `else`.
- **Loops:** `for`, `while`.

Exemplo de gramática:

```antlr
ifStatement: 'if' '(' expression ')' '{' statement* '}' ('else' '{' statement* '}')?;
loopStatement: 'for' '(' variableDeclaration? ';' expression? ';' expression? ')' '{' statement* '}'
             | 'while' '(' expression ')' '{' statement* '}';
```

### 4. **LLVM Integration**

#### Representação IR (Intermediate Representation)
Para usar o LLVM, você precisará traduzir sua linguagem para a representação intermediária (IR) do LLVM. Isso envolve:

- **Geração de Código:** Implementar um backend que converte a AST (Árvore Sintática Abstrata) para LLVM IR.
- **Tipos e Funções LLVM:** Definir como os tipos e funções da sua linguagem mapeiam para os tipos e funções do LLVM.

### 5. **Outros Componentes Importantes**

#### 1. **Erro e Tratamento de Exceções**
   - Definir como os erros são tratados, tanto em tempo de compilação quanto em tempo de execução.

#### 2. **Entrada e Saída**
   - Definir operações básicas de entrada e saída, como leitura de entradas do usuário e impressão de saídas.

#### 3. **Comentários**
   - Implementar uma sintaxe para comentários, tanto de linha única quanto de múltiplas linhas.

### 6. **Próximos Passos**

1. **Implementar o Parser e AST:** 
   - Continue desenvolvendo seu parser usando ANTLR e construa a árvore sintática abstrata para representar programas.

2. **Implementar o Analisador Semântico:**
   - Verifique tipos, variáveis não declaradas e outras verificações semânticas.

3. **Implementar o Gerador de Código LLVM:**
   - Crie uma interface para traduzir sua AST para o código IR do LLVM.

4. **Testes e Validação:**
   - Escreva casos de teste para garantir que todas as funcionalidades básicas estejam funcionando corretamente.

5. **Documentação:**
   - Documente a gramática e a semântica da linguagem, facilitando o entendimento e o uso.

6. **Exploração de Recursos Avançados:**
   - Após criar o MVP, explore recursos avançados como inferência de tipos, garbage collection, metaprogramação, etc.

### Conclusão

Começar com funções, estruturas de dados e controle de fluxo é essencial para qualquer linguagem de programação. A integração com o LLVM é uma excelente maneira de compilar sua linguagem para código de máquina eficiente. Ao seguir esses passos, você criará uma base sólida para expandir sua linguagem no futuro. Boa sorte com seu projeto!