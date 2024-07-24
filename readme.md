# Especificação da Linguagem de Programação

## Tipos e Variáveis

### Declaração de Tipos
- `native type i32;` - Declaração nativa de um tipo inteiro para o compilador.
- `native type any;` - Tipo que pode ser reescrito com qualquer outro tipo.
- `native type unknown;` - Similar ao `any`, mas com intenções de uso mais restritas e gerenciamento de contratos.

### Declaração de Variáveis
- `var x1 i32 = 23` - Declaração explícita de uma variável com tipo.
- `var x2 = 23` - Declaração de variável com inferência de tipo.
- `const x3 = 32` - Declaração de uma constante.

## Funções

### Funções Simples
- `func example_function(x i32, y i32) i32` - Exemplo de uma função simples.

### Funções Recursivas
- `func recursive_example(n i32) i32` - Exemplo de uma função recursiva.

### Funções de Alta Ordem
- `func higher_order_example(f func(i32) i32, x i32) i32` - Exemplo de uma função de alta ordem.

### Função que retorna outra função
- `func return_function(x i32) func(i32) i32 {
    return (y i32) {
        return x + y
    }
}` - Exemplo de uma função que retorna outra função.

### Funções Anônimas (com seu próprio escopo)
- `var lambdaFunction = func (data string) { [...] }` - Exemplo de uma função anônima.

### Funções anônimas com escopo no local da declaração (sem escopo próprio)
- `var lambdaFunction = (data string) { [...] }` - Exemplo de uma função anônima.

### Funções Genéricas
- `func generic_example[T](data T) T` - Exemplo de uma função genérica usando Monomorphization.

### Modificadores e Metaprogramação
- `native modifier symbol(options map(string, any));` - Modificador que permite metaprogramação em tempo de compilação. recebendo como parâmetro 

### Exotypes
- `native func map(key Type, value Type) Type` - Definição de um exotype, isso acontece quando um dos parâmetro é um Type que possui características especiais.


func map(key Type, value Type) {
    /**
        O que eu quero dizer aqui é que 
     */
    return {
        get func(key Type) : Type; // quando uma função é declarada assim, ela apenas é uma declaração de interface;
        set func(key Type, value Type);
    }
}

var content map(string, i32); // aqui eu estou definindo que o tipo map é um exotype
var anotherContent map[string, i32]; // aqui também temos um genérico mas é um pouco diferença sobre como funciona por trás dos planos, aqui temos o monomorphization, mas acima não, porque o compilador não consegue inferir o tipo do map, então ele não consegue fazer o monomorphization. o primeiro utilizad um padrão Exotype, que é um tipo que pode ser reescrito com qualquer outro tipo.

Perceba que há uma semelhança entre declaração de tipos e declaração de objetos, o que pode confundir bastante;
var thisIsAnObject = {
    name: "John",
    age: 30,
}

Percenba que é bem parecido com o javascript porém a diferença é que neste caso um tipo obrigatóriamente deve ser declarado em algum lugar no sistema, algo assim
type PersonType = {
    name string,
    age i32,

    // métodos caso se queira
    func toString() {
        return this.name + " " + this.age
    }
}

agora podemos declarar um tipo de forma bem parecido e armazena o tipo em uma variavel
var thisIsAnType = {
    name string,
    age i32
}
A diferença sutil está apenas no ":"


var thisIsAnObject thiIsAnType; aqui temos um objeto cujo tipo é do tipo "thisIsAnType" criado. variaveis que armazenam tipos são chamadas de "types" e são a essencial de um exotype:

func createAnVariable(type Type) {
    return {
        name string
        age i32
        data type


        func getData() type {
            return type
        }
    }
}


Um conceito interessante sobre a linguagem é que ela deixa separado a ideia de estrutura de dados e métodos. No caos acima estamos crianso um método dentro da estrutura, mas para o interpretador ou parser o que isso significa é o seguinte:
- Esta função tem a capacidade de acessar quaisquer estruturas de dados que respeitem os atributos que a estrutura criada possui, por exemplo:

suponhja que eu tenha um objeto
var x = {
    name: "John",
    age: 30
    genrer: "male"
}

e suponhamos que eu tenha uma seguinte estrutura declarada:
var someStruct = {
    name string,
    age i32,

    public func doStuff() {
        return this.name + " " + this.age
    }

    protected func onlyCalledByExactlyThisStruct() {
        return this.name + " " + this.age
    }
}

No caso acima, o objeto respeita parcialmente o formato da estrutura declarada, o que permite chamar o método print()
x.doStuff()

Todo método criado dentro de uma declaração de estrutura é um objeto que tem acesso livre aos atributos da estrutura que o criou.
caso se queira que a função exiga exatamente a estrutura deve-se declarar como foi declarado no outro método, agora ele sempre vai dar prioridade para a estrutura mais completa
por exemplo se existir uma estrutura de dados declarada que tenha exatamente a estrutura do objeto ela tera um "match" perfeito então ela que vai ser associado ao lint



Um método pode ser chamado apenas com chaves graças à injeção de contexto, bem similar a injeção de dependência, mas ao invés de injetar dependências, injeta contexto.
exemplo de uso:

// method 'anMethod' recebe dois simbolos (similar ao ruby) e no final tem uma chave que já é um corpo de função do ultimop parâmetro, mas eis a declaração
anMethod :allowed, :use {
    name.print()
    age.print() // de onde vieram os dados?
}

// até lá em cima o parser ficará confuso e tratará a função como uma função louca (em inglês "wildcard function" ou em crazy function)
uma crazy function é uma função que chama atributos de um objeto que não foi declarado, por exemplo:
func IamCrazy() {
    @name.print() // o arroba indica que será declarado posteriormente
}



funções loucas podem ser chamadas porém elas irão retornará uma função cujo parâmetros serão as variaveis que faltam para que a função seja chamada, o compilador não vai deixar

var function = IamCrazy()! // ops, this is a crazy funcion, a exclamação vai ajudar para que programador tenham ciencia de que está chamando uma função louca, será obrigatório por segurança: experiencia do programador 
var value = function(name: {
    name: "John"
    age: 30
}) // pode ser esse objeto  ou qualquer outro que tenha os atrivutos necessários para chamar a função 'print'

podemos pensar em uma função louca como uma função que recebe um objeto e retorna uma função que recebe um objeto e retorna um objeto, e assim por diante, só que de uma forma mais simples e mais fácil de entender.
seria o equivalente a
func IamCrazy(name string, age i32) {
    return (name IPrintable) {
        name.print()
    }
}

 

eis a explicação:
func anMethod(secutiry :string, use :string, body func(string, string)) {
    type Context {
        name string
        age i32
    }

    var context Context = {
        name: "John",
        age: 30
    }

    Context.inject(body);



}

// terminar de ler as anotações do wikipedia sobre programação no obsiaidn para terminar isso aqui para saber como eu vou implementar.


// declara type <nome> {} é a mesma coisa que var <nome> = {} ou const <nome> = {} // se for constante podemos estaticamente delcarar o tipo.
type Thing {

}


// existem genéricos de dois tipos, os tipo template como no C++ que cria cópias, e os como o Java que fazem casting em tempo de compilação, o que é mais eficiente.


// pode-se fazer extensions
func content[T implements IPrintable] (value T) {}
func content[T extends IPrintable] (value T) {} // wilcard para permitir flexibilidade mesmo usando

A linguagem também permite o conceito de Box e unboxing, que é uma forma de encapsular um tipo de dados em uma caixa e desempacotar a caixa para acessar o conteúdo.
exemplo:
```java
List<Integer> numbers = new ArrayList<>();
numbers.add(5); // Auto-boxing de 'int' para 'Integer'
int num = numbers.get(0); // Auto-unboxing de 'Integer' para 'int'
```


um arquivo inteiro pode ser ums instancia de objeto se colocado a extensão correto
type module {
    name string
    age i32

    // o self é como é no ruby, é como se fosse o this
    self.new() {}

    reflection.loadAllFiles((script os.file) -> {
        // aqui dentro eu defino o que vai ser, se vou injetar o script dentro ou será como instancias
        // como se o tipo aqui fosse um esqueleeto
        // ainda preciso amadurecer a ideia do 'new'

        // o arquivo definido como tipo module, chamando new
        script.as(self).new()
    })

    return {}
}


o método é criado dentro do contexto de declaçaão de tipo e portando só pode ser chamado sob os termos do tipo:
os termos do tipo é que só pode ser chamado por um objeto que contenha os atributos.

porém podemos também criar contexto de declaração de motores exemplo:

context node {
    async func doSomething() {

    }
}


ou seja para rodar essa função preciso esta sob mesmo contexto de alguma forma

context node {
    await doSomething();
}


// neste exemplo contexto node permite integrar ao node.js o contexto tem capacidae de modificar comportamento da própria linguagem
injetar modificadores que só existem dentro do contexto. Por exemplo, podemos ter um contexto que contem um event loop. e neste contexto existe um modificador chamado 'async' que permite que uma função seja executada de forma assíncrona passado pro event loop

o contexto permite injetar frameworks de forma organica permitidno a separação de declaração e implementação


var ctx = module.new // isso pode ser feito em uma função, assim como no javascript. No caso o método new fará com que tudo criado dentro da função persista para ser usado 
ctx.name.print() // por exemplo

se o nome do arquivo for [algo].module.nstls #nstls é a extensão do arquivo


e se criarmos um arquivo com a extensão, ele poderá ser usado como se estivesse todo o código estivesse no contexto da função ou estrutura







### Interfaces e Contratos
- `native interface IPrintable;` - Interface para tipos que podem ser impressos.

## Operações e Expressões

### Operadores Básicos
- Operações de adição, subtração e outras operações aritméticas básicas são suportadas diretamente pelo compilador.

### Funções Anônimas e de Alta Ordem
- `data.map((data) { data.to(String) });` - Exemplo de uso de função anônima para mapear dados.
- `data.map func (data) { data.to String };` - Outra sintaxe para a função anônima mostrando a flexibilidade na chamada de funções.

data.map() {} // isso é chamar uma função map com parentese e um corpo
data.map () {} // isso é uma função map cujo primeiro parâmetro é uma função anônima com um corpo, cuidado com a diferença, observar o espaços e o uso de chaves


## Estruturas e Tipos Complexos

### Estruturas Simples
- `type PersonType = { name: string, age: i32 }` - Definição de uma estrutura simples para representar uma pessoa.

### Estruturas Aninhadas e Compostas
- Uso de estruturas dentro de outras estruturas para formar tipos de dados complexos.

## Impressão e Saída

- `native func print(data IPrintable) void;` - Função nativa para imprimir dados que implementam a interface `IPrintable`.
- Várias formas de chamar a função `print`, demonstrando flexibilidade na sintaxe:
  - `print x1`
  - `x2.print()`
  - `print(x2)`
  - `print x3.type()`
  - `print type(x3)`

## Metaprogramação e Modificação em Tempo de Compilação

- O uso de `symbol` e `exotype` para definir comportamentos e tipos que são determinados e otimizados em tempo de compilação.
- Discussão sobre como o tipo `any` e `unknown` difere em termos de implementação e uso, com `any` sendo mais flexível e `unknown` mais restrito e contratual.

## Reflexão e Contratos

- Discussão sobre como a linguagem pode suportar reflexão e contratos através do tipo `unknown` e funcionalidades de metaprogramação.

## Considerações de Design

- Discussão sobre as escolhas de design para a linguagem, como a flexibilidade de sintaxe e a forte capacidade de metaprogramação para permitir otimizações em tempo de compilação.

## Implementação e Desafios

- Considerações sobre como esses recursos avançados podem ser implementados na prática, incluindo desafios potenciais e soluções possíveis, como a integração de sistemas de tipos dinâmicos e estáticos.

## Conclusão

- Reflexão sobre como esses recursos podem beneficiar os desenvolvedores e sobre o potencial impacto dessa linguagem no desenvolvimento de software em geral.

