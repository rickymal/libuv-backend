
A linguagem permite a criação de tipos aninhados e estruturas compostas, facilitando a organização de dados complexos e relacionados.

type Address struct {
    street string
    city string
    zipCode i32
    anFunction func(string) string
};

type Company struct {
    name string
    address Address
    employees []PersonType
};

// Uso de um tipo aninhado
var myCompany = {
    name: "Tech Innovations"
    address: {
        street: "123 Tech Rd"
        city: "Innovate City"
        zipCode: 12345
    }
    employees: [
        {name: "Henrique", age: 30}
        {name: "Ana", age: 22}
    ]
};

A linguagem suporta a declaração de funções com parâmetros opcionais e argumentos nomeados, além de funções de alta ordem e genéricas.

func name(arg1 string, arg2 u32, arg3 string = "default") string {
    ...
}

var result = name('hello', 10, "world");


// Função que retorna outra função
func name(arg1 func(string) string) func(i32) i32 {

    return (x i32) {
        return 10;
    }

    // ou retorno explícito 
    /**
    return (x i32) i32 {
        return 10;
    }
     */
}

var ctx = name((names string) {
    ...
});

ctx();

// A linguagem suporta interfaces avançadas que facilitam o polimorfismo e a reutilização de código.

type IPrintable interface {
    name string // aceita atributos também
    print() void
};

// uso impĺícito de interface
type Document {
    content string

    func print() {
        console.log("Document: ${this.content}");
    }
}

// uso explícito de interface
type Image implements Printable {
    filepath string,

    func print() {
        console.log("Printing image from: " + this.filepath);
    }
}

// Função genérica para imprimir qualquer objeto Printable
func printItem(item Printable) {
    item.print()
}

// declaração do tipo da estrutura pode ser explícita
var doc = Document { content: "Hello, world!" };
var img = Image { filepath: "/path/to/image.jpg" };

// ou implícita, o compilador irá inferir baseado no que foi declarado
var doc = { content: "Hello, world!" };
var img = { filepath: "/path/to/image.jpg" };

printItem(doc)
printItem(img)

// A linguagem oferece flexibilidade para tipos genéricos e dinâmicos.

func transform[T](input T, functionName func (T) T) T {
    return func(input);
}

// declaração de função anônima explícito
var increment = (x i32) i32 { return x + 1; };
var shout = (msg string) string { return msg.toUpper() + "!"; };

// declaração de função anônima implícito, o retorno da função dirá como será feito.
var increment = (x i32) { return x + 1; }; 
var shout = (msg string) { return msg.toUpper() + "!"; };

var newNumber = transform(10, increment); // Retorna 11
var loudMessage = transform("hello", shout); // Retorna "HELLO!"

// o 'any' é uma interface{} equivalente em golang praticamente
// Uso de genéricos com tipos dinâmicos
var mixedBag any = [1, "string", true];
mixedBag.forEach((item) {
    if (item.is(i32)) {
        console.log("Integer: ${item.toString()}");
    } else if (item.is(string)) {
        console.log("String: ${item.toUpperCase()}");
    }
});

// A linguagem permite a modificação dinâmica de estruturas durante o runtime.

// declara um modificador que será implementado nativamente (internamente pela linguagem)
native modifier mutable;

mutable type FlexibleType = {
    key string,
};

var flex = FlexibleType { key: "initial value" };

// Adiciona dinamicamente um novo campo
flex.newField = 100; //
flex.add_field("newField", i32);
flex.newField = 100;

console.log(flex.newField);

// A linguagem suporta decoradores e modificadores aplicados a funções e tipos.


// exemplo de função genérica que recebe uma função e retorna uma função
func annotate[T](functionName func(T) T) func(T) T {}

// Decorador em tempo de execução
@annotate()
func foo() {}

// igual aiop native modifie
// Modificadores: Decorador em tempo de compilação
@[annotate]
func foo() {}

// Decoradores em tempo de compilação podem ser passados assim também
annotate func foo() {}



// A linguagem permite a criação de contextos, semelhante aos hooks de contexto do React.

native func (var IPrintable) print();

type use struct {
    native modifier abstract[T](func (T) T) func (T) T;
}

// Decorador que ajuda o compilador a identificar variáveis em contexto
@[use.abstract]
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

// ou 
<context n8n>
    foo()
<context/>

// 9.1 Exemplo básico de composição por aninhamento


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

// 9.2 Composição direta e inversa


type AAA {
    name string
    data [][]f32? // a interrogação indica que a matriz pode ser nula

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

ctx.doSomething(); // ao chamar o método, o compilador irá verificar o escopo do tipo BBB e verá que a função exige o uso de uma varivel name presente no tipo pai. Nesse caso, a função irá disparar um erro de compilação. porém o modificador de acesso high permite com que a função continue a ser compilada. pois adiciona a palavra reservada outer e inner, que permite uma compilação lazy vamos dizer assim: A função com o modificador 'high' ao ser chamada na verdade retorna outra função cujos parâmetros são os atributos pendentes para ser executado ou podendo passar o objeto inteiro que contém os atributos.

Ou seja se no objeto passado houve tudo que precisa, simplesmente executa se não retorna

no caso supondo que estivesse escrito assim:

native modifier high; // adicionar palavras inner e outer para acessar o escopo interno e externo
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

var value func[T] (**kwargs) = ctx.doSomething(); 

// o atributo que faltava para que a execução ocorrece, podendo também passar um tipo inteiro contando que este contenha o atributo requerido.
value({name: "Henrique"})


// implemntações futuras
os modificadores adicionar palavras chave especiais podendo este serem aplicados em declaração e implementação das funções ou do uso das mesmas.  

// tipo abstrato é um tipo que não pode ser instanciado, apenas deve fazer parte de outro tipo como no aninhamento, ou apenas para uso em declaração de funções. os abstract são bem parecido com traits também.
abstract type db {
    func doSomethign() {
        ...
    }
}

type AAA struct {
    age i32
    name string
    db IDatabase
    ap IAnotherProvider?
}

var variable =  {
    age: 10
    name: "Henrique"
    db: db
    ap: null
};

// Sintaxe alternativa com anotação XML
var variable = (
    <AAA>
        <a>
        <b>
    </AAA>
);


// também podemos ter isso

native modifier strategy(string);

type AAA struct {
    age i32
    name string

    @[strategy('an option to instanciate this struct')]
    type struct {
        anField i32

        func doSomething() {
            io.print("do something with strategy I");
        }
    }

    @[strategy('another option to instanciate this struct')]
    type struct {
        anotherField i32

        func doSomething() {
            io.print("do something with strategy II");
        }
    }
}



var ctx AAA = {
    age: 10,
    name: "Henrique",
    anField: 10,
}

ctx.doSomething();  // imprimi "do something with strategy I"

var cty AAA = {
    age: 10,
    name: "Henrique",
    anotherField: 10,
}

cty.doSomething(); // imprimi "do something with strategy II"