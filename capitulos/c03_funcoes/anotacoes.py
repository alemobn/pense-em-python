"""
Capítulo 3: Funções

Tópicos estudados:
- Definindo novas funções
- Parâmetros
- Chamando funções
- Repetição
- Variáveis e parâmetros são locais
- Diagrama de pilha
- Tracebacks
- Por que utilizar funções?
- Depuração
- Glossário
- Exercícios
"""


def definindo_novas_funcoes():
    """
    Explica a criação de uma função básica, a diferença entre o objeto da
    função na memória e a sua execução real através do operador de chamada.
    """
    print("--- Definindo novas funções ---\n")

    def print_lyrics():  # <- cabeçalho da função
        # Tudo que está abaixo do cabeçalho e indentado -> corpo da função
        print("I'm a lumberjack, and I'm okay.")
        print("I sleep all night and I work all day.")

    print(
        "'def' é uma palavra reservada que indica uma definição de função. "
        "O nome da função é 'print_lyrics'. Qualquer nome de variável "
        "válido também pode ser utilizado como nome de função."
        "\n\n"
        "Os parênteses vazios após o nome da função indicam que ela não "
        "recebe argumentos."
        "\n\n"
        "Definir uma função cria um 'objeto de função', que é alocado na "
        "memória RAM e pode ser referenciado como qualquer outra variável. "
        "Podemos exibir o ponteiro desse objeto da seguinte maneira:"
        "\n"
    )
    print(print_lyrics)  # Exibindo o objeto da função
    print()
    print_lyrics()  # Chamando a função (execução)


def parametros():
    """
    Explica o conceito de parâmetros e argumentos, demonstrando como os valores
    são atribuídos e copiados na memória durante a chamada de uma função.
    """
    print("--- Parâmetros e Argumentos ---\n")
    print(
        "Algumas das funções que vimos até agora exigem argumentos; "
        "por exemplo, ao chamar 'abs', passamos um número como argumento. "
        "Algumas funções exigem mais de um argumento: a função 'math.pow', "
        "por exemplo, requer dois argumentos, a base e o expoente."
        "\n"
    )

    # Definição de função que requer um argumento
    def print_twice(string):  # (string) -> parâmetro da função
        print(string)
        print(string)

    print(
        "O nome da variável entre parênteses é chamado de 'parâmetro'. "
        "Quando a função é chamada, o valor passado como argumento é "
        "atribuído a esse parâmetro. Por exemplo, podemos chamar "
        "'print_twice' da seguinte forma:\n"
    )

    # Atribuindo um valor (argumento) ao parâmetro da função
    print_twice("Dennis Moore, ")
    print()

    print(
        "Executar essa função tem o mesmo efeito que atribuir o argumento "
        "ao parâmetro e, em seguida, executar o corpo da função, como no "
        "exemplo a seguir:\n"
    )

    string = "Dennis Moore, "
    print(string)
    print(string)

    print("\nTambém é possível utilizar uma variável como argumento:\n")
    line = "Dennis Moore, "

    # Utilizando uma variável para atribuir um valor ao parâmetro da função:
    # (o valor de 'line' é atribuído ao parâmetro da função)
    print_twice(line)


def chamando_funcoes():
    """
    Demonstra a composição de funções, ilustrando como pequenas funções
    especializadas podem ser combinadas dentro de outras funções para
    executar tarefas mais complexas.
    """
    print("--- Chamando Funções ---\n")
    print(
        "Uma vez que a função esteja definida, podemos utilizá-la dentro "
        "de outra função. Para ilustrar, vamos criar funções que exibem "
        "(imprimem) a letra de 'The Spam Song':\n"
    )

    # Função inicial que recebe dois parâmetros:
    def repeat(word, n):
        print(word * n)

    spam = "Spam, "

    # Exibindo a primeira linha da música:
    # repeat(spam, 4)

    def first_two_lines():
        repeat(spam, 4)
        repeat(spam, 4)

    # Exibindo as primeiras duas linhas da música:
    # first_two_lines()

    def last_three_lines():
        repeat(spam, 2)
        print("(Lovely Spam, Wonderful Spam!)")
        repeat(spam, 2)

    # Exibindo as três últimas linhas da música:
    # last_three_lines()

    def print_verse():
        first_two_lines()
        last_three_lines()

    print_verse()


def repeticao():
    """
    Demonstra o uso da instrução 'for' para repetir blocos de código e ilustra
    como encapsular loops dentro de funções parametrizadas.
    """
    print("--- Repetição ---\n")
    print(
        "Se quisermos exibir mais de um verso, podemos utilizar uma "
        "instrução 'for'. Vejamos um exemplo simples:\n"
    )
    # A primeira linha começa com a palavra reservada 'for', seguida de
    # uma nova variável chamada 'i' e outra palavra reservada, 'in'. Ela
    # utiliza a função 'range' para criar uma sequência de dois valores,
    # que são '0' e '1'. Em Python, quando começamos a contar, geralmente
    # começamos do 0.
    for i in range(2):  # Cabeçalho da instrução
        print(i)  # Corpo do for (precisa ser indentado)

    print(
        "\nAqui está um exemplo de como podemos utilizar um loop 'for' para "
        "exibir dois versos da música:\n"
    )

    # ----- Trecho da função 'chamando_funcoes' copiado para demonstração -----

    # Função inicial que recebe dois parâmetros:
    def repeat(word, n):
        print(word * n)

    spam = "Spam, "

    # Exibindo a primeira linha da música:
    # repeat(spam, 4)

    def first_two_lines():
        repeat(spam, 4)
        repeat(spam, 4)

    # Exibindo as primeiras duas linhas da música:
    # first_two_lines()

    def last_three_lines():
        repeat(spam, 2)
        print("(Lovely Spam, Wonderful Spam!)")
        repeat(spam, 2)

    # Exibindo as três últimas linhas da música:
    # last_three_lines()

    def print_verse():
        first_two_lines()
        last_three_lines()

    for i in range(2):
        print(f"Verse {i}:")
        print_verse()
        print()

    # Também é possível colocar um loop 'for' dentro de uma função:
    def print_n_verses(n):
        print(
            "Demonstrando o funcionamento de um loop 'for' dentro de uma "
            "função:\n"
            "-----------------------------\n"
        )
        # Mesmo que a variável 'i' não seja utilizada, é necessário declará-la
        for i in range(n):
            print_verse()
            print()

    print_n_verses(3)


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # definindo_novas_funcoes()
    # parametros()
    # chamando_funcoes()
    # repeticao()
    pass
