https://github.com/antlr/antlr4/blob/master/doc/getting-started.md


A linguagem de forma organiza programando de forma imperativa deve ser capaz de criar pipelines eficientes com modificadores corretos:

por exemplo carregando texto via stream, processar em batchs de bytes e outro pipe para mandar para um embeddings

a linguagem dever ter um trigger de lazy function ou de estrutura por exemplo, quando um contexto criar todas as variáveis necessárias para executar algo, ele dispara um construtor por exemplo, evitando os famosos 'init' para inicializar algo


Investigar a relaçaõ de ate que nivel de abstração é necessaário chegar, quanto mais abstração masi fácil porém menos liberdade, enmtão tenho que saber calcular isso

passagem de parametro via contexto (ajuda dois frameworks a trabalhagem junto sem que o programador final precisse saber)

esse link:https://langchain-ai.github.io/langgraph/#example
descreve muito bem minha visão para a linguagem na construção de contexto, langgraph

### Introdução à Linguagem

A linguagem proposta oferece uma combinação de tipagem dinâmica, genéricos, composição, contextos de execução e modificação de estruturas em tempo de execução. Ela visa facilitar o desenvolvimento de software flexível, reutilizável e eficiente.

### 1. Tipos Aninhados e Estruturas Compostas

A linguagem permite a criação de tipos aninhados e estruturas compostas, facilitando a organização de dados complexos e relacionados.

```zig
type Address struct {
    street string
    city string
    zipCode i32
};

type Company struct {
    name string
    address Address
    employees []PersonType
};

// Uso de um tipo aninhado
var myCompany = {
    name: "Tech Innovations",
    address: {
        street: "123 Tech Rd",
        city: "Innovate City",
        zipCode: 12345
    },
    employees: [
        {name: "Henrique", age: 30},
        {name: "Ana", age: 22}
    ]
};
```

### 2. Declaração de Funções

A linguagem suporta a declaração de funções com parâmetros opcionais e argumentos nomeados, além de funções de alta ordem e genéricas.

```zig
func name(arg1 string, arg2 u32, arg3 string = "default") string {
    ...
}

var result = name('hello', 10, "world");

// Função que retorna outra função
func name(arg1 func(string) string) func(i32) i32 {

    return (x) {
        return 10;
    }
}

var ctx = name(() {
    ...
});

ctx();
```

### 3. Traits Avançadas e Polimorfismo

A linguagem suporta Traits avançadas que facilitam o polimorfismo e a reutilização de código.

```zig
type IPrintable interface {
    name string,
    print() void
};

// Uso implícito de interface
type Document {
    content string,

    func print() {
        console.log("Document: ${this.content}");
    }
}

// Uso explícito de interface
type Image implements Printable {
    filepath string,

    func print() {
        console.log("Printing image from: " + this.filepath);
    }
}

// Função genérica para imprimir qualquer objeto Printable
func printItem(item Printable) {
    item.print();
}

// Declaração do tipo da estrutura pode ser explícita
var doc = Document { content: "Hello, world!" };
var img = Image { filepath: "/path/to/image.jpg" };

// Ou implícita, o compilador irá inferir baseado no que foi declarado
var doc = { content: "Hello, world!" };
var img = { filepath: "/path/to/image.jpg" };

printItem(doc);
printItem(img);
```

### 4. Tipagem Dinâmica e Uso Flexível de Genéricos

A linguagem oferece flexibilidade para tipos genéricos e dinâmicos.

```zig
func transform[T](input T, func (T) T) T {
    return func(input);
}

var increment = (x i32) i32 { return x + 1; };
var shout = (msg string) string { return msg.toUpper() + "!"; };

var newNumber = transform(10, increment); // Retorna 11
var loudMessage = transform("hello", shout); // Retorna "HELLO!"

// Uso de genéricos com tipos dinâmicos
var mixedBag: any[] = [1, "string", true];
mixedBag.forEach((item) {
    if (item.is(i32)) {
        console.log("Integer: ${item.toString()}");
    } else if (item.is(string)) {
        console.log("String: ${item.toUpperCase()}");
    }
});
```

### 5. Modificação de Estruturas em Tempo de Execução

A linguagem permite a modificação dinâmica de estruturas durante o runtime.

```zig
native modifier mutable;

mutable type FlexibleType = {
    key string,
};

var flex = FlexibleType { key: "initial value" };

// Adiciona dinamicamente um novo campo
flex.add_field("newField", i32);
flex.newField = 100;

console.log(flex.newField);
```

### 6. Decoradores e Modificadores

A linguagem suporta decoradores e modificadores aplicados a funções e tipos.

```zig
func annotate[T](func func(T) T) func(T) T {}

// Decorador em tempo de execução
@annotate()
func foo() {}

// Modificadores: Decorador em tempo de compilação
@[annotate]
func foo() {}

// Decoradores em tempo de compilação podem ser passados assim também
annotate func foo() {}
```

### 7. Construção de Contexto

A linguagem permite a criação de contextos, semelhante aos hooks de contexto do React.

```zig
native func (var IPrintable) print();

// Decorador que ajuda o compilador a identificar variáveis em contexto
@[use.context]
func baz() {
    n8n.name.print(); // A variável name não existe em lugar algum! O compilador verifica o contexto
}

context n8n {
    var name = "Henrique"
} {
}

func foo() {
    name.print(); // Vai funcionar pois está dentro do contexto
}

context {
    var name = "Henrique";
} {
    foo();
}
```

### 8. Aninhamento e Composição

#### 8.1 Exemplo básico de composição por aninhamento

```zig
type AAA struct {
    age i32,
    name string,

    func foo() {
        ...
    },

    type BBB struct {
        height f32,
        weight f32,

        func bar() {
            ...
        },

        type CCC struct {
            birthday string,

            func baz() {
                ...
            }
        }
    }
}
```

#### 8.2 Composição direta e inversa

```zig
type AAA {
    name string,
    data [][]f32?,

    func doAnotherThing() {
        inner BBB.age.print(); // Acesso explícito ao escopo interno
    },

    type BBB {
        age i32,
        func doSomething() {
            outer name.print(); // Acesso ao escopo do tipo que o contém
        }
    }
}

var ctx = {
    name: "Henrique",
    data: null,
    age: 10
};

// Explicitamente declarando o tipo BBB
var ctx BBB = {
    name: "Henrique",
    data: null,
};

ctx.doSomething(); // Ao chamar o método, o compilador irá verificar o escopo do tipo BBB e verá que a função exige o uso de uma variável name presente no tipo pai. Nesse caso, a função irá disparar um erro de compilação, porém a palavra reservada outer permite que a função continue a ser compilada. 
```

#### 8.3 Composição com modificadores de alta ordem

```zig
native modifier high;

type AAA {
    name string,
    data [][]f32?,

    high func doAnotherThing() {
        inner BBB.age.print(); // Acesso explícito ao escopo interno
    },

    type BBB {
        age i32,
        high func doSomething() {
            outer name.print(); // Acesso ao escopo do tipo que o contém
        }
    }
}

var ctx = {
    name: "Henrique",
    data: null,
    age: 10
};

// Explicitamente declarando o tipo BBB
var ctx BBB = {
    name: "Henrique",
    data: null,
};

var value = ctx.doSomething();

// O atributo que faltava para que a execução ocorresse, podendo também passar um tipo inteiro contanto que este contenha o atributo requerido.
value({name: "Henrique"});
```

### 9. Injeção de Dependências

A linguagem permite a injeção de dependências utilizando construtores.

```zig
type AAA struct {
    age i32,
    name string,

    // É possível fazer composição sem passar corpo (automaticamente ele cria os atributos com o mesmo nome)
    constructor(db IDatabase, ap IAnotherProvider);
}

// Criação de objeto com injeção de dependências
var variable = AAA(a, b) {
    age: 10,
    name: "Henrique"
};

// Sintaxe alternativa com anotação XML
var variable = (
    <AAA>
        <a>
        <b>
    </AAA>
);
```

Essa estrutura organizada e enriquecida oferece uma visão clara e sequencial das funcionalidades da linguagem, destacando a flexibilidade e o poder dos conceitos de tipos anônimos, composição, contextos e modificação de estruturas em tempo de execução.
