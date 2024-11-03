Para começar os testes da sua linguagem de programação construída em C++, você vai querer estabelecer uma base sólida de testes unitários que cubram desde funcionalidades básicas até aspectos mais complexos. Aqui está uma lista progressiva de testes que você pode implementar para garantir a robustez e a funcionalidade da sua linguagem:


# Deve ser capaz de criar variaveis e somar numero

```ruby
f64 n1 = 10.23

```

### 1. **Testes Básicos de Sintaxe e Semântica**
- **Testar o Analisador Léxico**: Verifique se o analisador léxico pode corretamente identificar tokens (palavras-chave, identificadores, literais, operadores, etc.).
- **Testar o Analisador Sintático**: Garanta que o parser pode construir corretamente árvores sintáticas para expressões válidas e rejeitar as inválidas.
- **Testar Análise Semântica**: Assegure que o analisador semântico pode corretamente vincular referências a declarações e verificar tipos.

### 2. **Testes de Execução de Código**
- **Execução de Expressões Simples**: Teste a avaliação de expressões matemáticas e lógicas básicas.
- **Declarações e Escopo de Variáveis**: Verifique se as variáveis são corretamente declaradas, inicializadas, e respeitam o escopo.
- **Funções e Procedimentos**: Teste a declaração e chamada de funções, passagem de parâmetros, e o retorno de valores.

### 3. **Testes de Estruturas de Controle**
- **Instruções Condicionais**: Teste `if`, `else`, e `switch` para garantir que as condições são corretamente avaliadas.
- **Laços de Repetição**: Verifique a funcionalidade de `for`, `while`, e `do-while` em diferentes cenários.

### 4. **Testes de Recursos Avançados**
- **Testar Sistemas de Tipos e Generics**: Garanta que a linguagem suporta definições de tipos complexos e generics corretamente.
- **Concorrência e Paralelismo**: Teste a criação e sincronização de threads ou outros modelos de concorrência que a linguagem suporta.
- **Coleta de Lixo e Gerenciamento de Memória**: Se aplicável, teste a eficácia e eficiência do sistema de gerenciamento de memória.

### 5. **Testes de Mnemônicos e Extensões**
- **Implementação de Mnemônicos**: Verifique se os mnemônicos modificam a linguagem conforme esperado, como adicionar novos comportamentos ou sintaxe.
- **Decoradores e Anotações**: Teste a funcionalidade dos decoradores para modificar o comportamento das funções ou classes.

### 6. **Testes de Integração e de Sistema**
- **Testar a Biblioteca Padrão**: Garanta que todas as funções e classes da biblioteca padrão funcionem conforme esperado em vários casos de uso.
- **Testar Aplicações Completas**: Escreva aplicações que utilizem múltiplos aspectos da linguagem para verificar a integração entre eles.

### 7. **Testes de Performance**
- **Benchmarking**: Compare a performance da sua linguagem com outras linguagens em tarefas típicas como manipulação de strings, cálculos matemáticos, e operações de I/O.
- **Testes de Estresse**: Avalie o desempenho e a estabilidade da linguagem sob carga pesada ou em condições extremas.

### Ferramentas e Frameworks de Teste
- **Google Test (gtest)**: Para testes unitários em C++.
- **Valgrind**: Para detecção de vazamentos de memória e problemas de gerenciamento de memória.
- **Sanitizers**: Use AddressSanitizer e ThreadSanitizer para encontrar problemas de uso de memória e concorrência.

### Conclusão
Ao criar essa base de testes, você poderá identificar e corrigir problemas desde o início do desenvolvimento da sua linguagem. Essa abordagem sistemática e progressiva ajudará a assegurar que a sua linguagem seja robusta, eficiente e confiável, facilitando a adoção e uso por outros desenvolvedores.