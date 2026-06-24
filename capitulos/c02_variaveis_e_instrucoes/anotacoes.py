"""
Capítulo 2: Variáveis e instruções

Tópicos estudados:
- Variáveis
- Diagramas de estado
- Nomes de variáveis
- Instrução import
- Expressões e instruções
- Função print
- Argumentos
- Comentários
- Depuração
- Glossário
- Exercícios
"""


def variaveis():
    """
    Demonstrar o conceito de atribuição e uso de variáveis na memória.
    """
    print("--- Demonstração de Variáveis ---\n")
    # Uma "variável" é um nome que se refere a um valor.
    n = 17
    pi = 3.141592653589793
    message = 'And now for something completely different'
    # Podemos utilizar uma variável como parte de uma expressão
    # com operadores aritméticos:
    print(n + 25)
    print(2 * pi)
    # Também é possível empregar uma variável ao chamar uma
    # função:
    print(round(pi))
    print(len(message))


def diagramas_de_estado():
    """
    Exemplificar a representação visual de variáveis e seus valores na memória.
    """
    print("--- Demonstração de Diagramas de Estado ---\n")
    # Uma forma comum de representar variáveis por escrito é
    # colocar o nome com uma seta apontada para o seu valor:
    print('n ----> 17')
    print('pi ----> 3.141592653589793')
    print('message ----> \'And now for something completely different\'')
    # Esse tipo de figura é denominado "diagrama de estado" porque
    # ilustra a condição atual de cada uma das variáveis (pense
    # nisso como o estado da variável).
    # Utilizaremos diagramas de estado ao longo deste livro para
    # representar um modelo de como o Python armazena variáveis
    # e seus respectivos valores.


def nomes_de_variaveis():
    """
    Explicar as regras de nomenclatura de variáveis e identificar palavras
    reservadas.
    """
    print("--- Demonstração de Nomes de Variáveis ---\n")
    # Nomes de variáveis não têm limite de tamanho.
    # Podem conter tanto letras quanto números, mas não podem
    # começar com um número.
    # É possível utilizar letras maiúsculas, mas a recomendação
    # é utilizar apenas letras minúsculas.
    # O único sinal de pontuação permitido em nomes de variáveis
    # é o "underscore(_)".
    # -------------------------------------------------------------
    # Se atribuirmos um nome inválido a uma variável, receberemos
    # um erro de sintaxe. Por exemplo, o nome "million!" é inválido
    # porque contém pontuação.
    # Para testar o erro, descomente a linha abaixo:
    # million! = 1000000
    # -------------------------------------------------------------
    # "76trombones = 'big parade'" é inválido porque começa com um
    # número
    # Para testar o erro, descomente a linha abaixo:
    # 76trombones = 'big parade'
    # -------------------------------------------------------------
    # "class" também é inválido, mas pode não ser óbvio o porquê
    # Para testar o erro, descomente a linha abaixo:
    # class = 'Self-Defense Against Fresh Fruit'
    # Acontece que class é uma "palavra reservada", ou seja, é
    # uma palavra especial utilizada para especificar a estrutura
    # de um programa. Palavras reservadas não podem ser utilizadas
    # como nomes de variáveis.
    # -------------------------------------------------------------
    # Aqui está uma lista completa das palavras reservadas do
    # Python (não é necessário memorizar essa lista):
    palavras_reservadas = [
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "case", "class", "continue", "def", "del", "elif", "else",
        "except", "finally", "for", "from", "global", "if", "import", "in",
        "is", "lambda", "match", "nonlocal", "not", "or", "pass", "raise",
        "return", "try", "while", "with", "yield"
    ]
    print(", ".join(palavras_reservadas))


def instrucao_import():
    """
        Demonstrar o uso da instrução import para acessar módulos,
        suas variáveis e funções.
    """
    print("--- Demonstração da Instrução Import ---\n")
    # Para utilizar alguns recursos do Python, é necessário
    # "importá-los". Por exemplo, a instrução a seguir importa
    # o módulo "math":
    import math
    # Um módulo é uma coleção de variáveis e funções.
    # O módulo math oferece uma variável chamada "pi", que
    # armazena o valor da constante matemática conhecida
    # como π. É possível mostrar seu valor dessa forma:
    print(math.pi)
    # Para utilizar uma variável em um módulo, é necessário
    # empregar o "operador de ponto(.)" entre o nome do módulo
    # e o nome da variável.
    # O módulo math também contém funções. Por exemplo, "sqrt"
    # calcula raízes quadradas:
    print(math.sqrt(25))
    # E "pow" eleva um número à potência de um segundo número:
    print(math.pow(5, 2))
    # Até agora, vimos duas maneiras de elevar um número a uma
    # potência: podemos utilizar a função "math.pow" ou o
    # operador de exponenciação, "**". Ambos são adequados,
    # mas o operador é utilizado com mais frequência do que a
    # função.


def expressoes_e_instrucoes():
    """
        Diferenciar expressões e instruções através de exemplos de avaliação
        e execução.
    """
    print("--- Demonstração de Expressões e Instruções ---\n")
    import math
    # Uma expressão pode consistir em um único valor, como um
    # número inteiro, um número de ponto flutuante ou uma string.
    # Também pode ser composta de uma coleção de valores e
    # operadores.
    # Além disso, expressões podem incluir nomes de variáveis e
    # chamadas de função. Vejamos a seguir um exemplo de expressão
    # que reúne vários desses elementos:
    n = 17
    print(19 + n + round(math.pi) * 2)
    # Também vimos alguns tipos de instruções. Uma "instrução" é
    # uma unidade de código que tem um efeito, mas nenhum valor.
    # Por exemplo, uma instrução de atribuição cria uma variável
    # e atribui um valor a ela, mas a instrução em si não tem valor:
    # x = 42
    # Da mesma forma, uma instrução de importação também tem um efeito:
    # -- ela importa um módulo para que possamos utilizar os valores e
    # funções que ele contém --, mas a instrução em si não produz um valor.
    # Calcular o valor de uma expressão é o que chamamos de "avaliação".
    # Executar uma instrução é chamado de "execução".


def funcao_print():
    """
        Demonstrar o uso da função print para exibir valores, expressões
        e múltiplos argumentos.
    """
    print("--- Demonstração da Função Print ---\n")
    import math
    # A função "print" exibe valores e/ou expressões no console:
    n = 17
    print(n + 1)
    # Ela também funciona com números de ponto flutuante e strings:
    print("The value of pi is approximately")
    print(math.pi)
    # Também é possível utilizar uma sequência de expressões
    # separadas por vírgula:
    print("The value of pi is approximately", math.pi)
    # Vale destacar que a função "print" insere um espaço entre os valores
    # exibidos.


def argumentos():
    """
    Explicar o conceito de argumentos em funções, cobrindo parâmetros
    opcionais, múltiplos e erros de tipo.
    """
    print("--- Demonstração de Argumentos ---\n")
    import math
    # Quando chamamos uma função, a expressão entre parênteses é chamada de
    # "argumento".
    # Algumas das funções que vimos até agora aceitam apenas um argumento,
    # como a função "int":
    print(int("101"))
    # Outras funções aceitam dois argumentos, como é o caso de "math.pow":
    print(math.pow(5, 2))
    # Há também funções que podem receber argumentos adicionais, que são
    # opcionais. Por exemplo, a função "int" pode aceitar um segundo
    # argumento que especifica a base do número:
    print(int("101", 2))  # A sequência de dígitos "101" na base "2"
    # representa o número "5" na base "10".
    # A função "round" também permite um segundo argumento opcional, que
    # determina o número de casas decimais para o arredondamento:
    print(round(math.pi, 3))
    # Algumas funções conseguem aceitar qualquer quantidade de argumentos,
    # como a função "print":
    print("Any", "number", "of", "arguments")
    # Se chamarmos uma função e fornecermos argumentos em excesso, um
    # "TypeError" será gerado.
    # Para testar o erro, descomente a linha abaixo:
    # print(float("123.0", 2))  # TypeError: float expected at most 1
    # argument, got 2
    # Se fornecermos argumentos de menos, o resultado será o mesmo: um
    # "TypeError".
    # Para testar o erro, descomente a linha abaixo:
    # print(math.pow(2))  # TypeError: pow expected 2 arguments, got 1
    # Além disso, se passarmos um argumento de um tipo que a função não
    # consegue manipular, também ocorrerá um "TypeError":
    # Para testar o erro, descomente a linha abaixo:
    # print(math.sqrt("123"))  # TypeError: must be real number, not str


def comentarios():
    """
        Explicar o papel dos comentários no código e a importância de
        documentar o motivo por trás das decisões de implementação.
    """
    print("--- Uso de Comentários ---\n")
    # Comentários
    print(
        "À medida que os programas se tornam maiores e mais complexos, "
        "tornam-se mais difíceis de compreender. As linguagens formais são "
        "densas, e muitas vezes é complicado olhar para um trecho de código "
        "e compreender o que ele faz ou o motivo pelo qual faz isso.\n"
    )
    print(
        "Por essa razão, é recomendável adicionar notas aos seus programas "
        "para explicar, em linguagem natural, o que o código está realizando. "
        "Essas notas são chamadas de \"comentários\" e começam com símbolo de "
        "cerquilha (#).\n"
    )
    # quantidade de segundos em 42:42
    seconds = 42 * 60 + 42  # noqa: F841
    # Também é possível colocar comentários ao final das linhas de código:
    miles = 10 / 1.61  # 10 quilômetros em milhas # noqa: F841
    print(
        "Tudo que está após o # até o final da linha é ignorado e não afeta "
        "a execução do programa. Os comentários são mais úteis quando "
        "documentam algo no código que não é imediatamente óbvio. Podemos "
        "assumir que o leitor compreende o que o código faz; portanto, é "
        "mais útil explicar \"por que\" ele faz o que faz.\n"
    )
    # Esse comentário abaixo, por exemplo, é redundante e pouco útil:
    v = 8  # atribui 8 ao v # noqa: F841
    # Por outro lado, este comentário abaixo oferece informações valiosas
    # que não estão no código:
    v = 8  # velocidade em milhas por hora # noqa: F841
    print(
        "Nomes de variáveis bem escolhidos podem diminuir a necessidade de "
        "comentários, mas nomes muito longos podem tornar expressões "
        "complexas mais difíceis de ler. Portanto, é importante que haja um "
        "equilíbrio."
    )


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # variaveis()
    # diagramas_de_estado()
    # nomes_de_variaveis()
    # instrucao_import()
    # expressoes_e_instrucoes()
    # funcao_print()
    # argumentos()
    # comentarios()
    pass
