Vamos criar exemplos funcionais para as demais estruturas de controle de fluxo e outras funcionalidades básicas definidas na sua linguagem. Aqui estão os exemplos:

### 1. **If-Else Statement**

```luna
if 3 > 2 {
    print("Maior")
} else {
    print("Menor ou igual")
}
```

### 2. **While Statement**

```luna
var count = 0;

while (count < 5) {
    print("Contagem: ", count)
    count = count + 1
}
```

### 3. **For Statement**

```luna
for (var i = 0; i < 10; i = i + 1) {
    print("Valor de i: ", i)
}
```

### 4. **Function Declaration and Return**

```luna
func add(a i32, b i32) i32 {
    return a + b;
}

var result = add(5, 3);
print("Resultado: ", result)
```

### 5. **Anonymous Function Declaration**

```luna
var add = func(a i32, b i32) i32 {
    return a + b;
}

var result = add(4, 2);
print("Resultado: ", result)
```

### 6. **Return Statement**

```luna
func greet(name string) {
    if name != "" {
        return "Olá, " + name;
    }
    return "Olá, visitante";
}

print(greet("João"))
print(greet(""))
```

### 7. **Break Statement**

```luna
for (var i = 0; i < 10; i = i + 1) {
    if i == 5 {
        break;
    }
    print("i: ", i)
}
```

### 8. **Continue Statement**

```luna
for (var i = 0; i < 10; i = i + 1) {
    if i % 2 == 0 {
        continue;
    }
    print("Ímpar: ", i)
}
```

### 9. **Word With Parameter**

```luna
print("Olá, mundo!") // Exemplo de chamada de função com uma string como parâmetro

log(404) // Exemplo de chamada de função com um número inteiro como parâmetro
```

### 10. **Memory Allocation**

```luna
const maxCount = 100;
var currentCount = 0;
```

Esses exemplos cobrem uma gama básica de funcionalidades que você definiu para a linguagem. Eles demonstram o uso de declarações condicionais, loops, funções (tanto nomeadas quanto anônimas), e gerenciamento de variáveis. Esses exemplos também incluem o uso de operadores, declarações de controle de fluxo como `break` e `continue`, e a utilização de parâmetros em funções. 

Esses exemplos são uma boa base para testar a funcionalidade e a sintaxe da sua linguagem, garantindo que a gramática e o analisador sintático estejam funcionando conforme esperado. Se precisar de mais detalhes ou exemplos adicionais, por favor, avise!