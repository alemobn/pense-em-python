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


def variaveis_e_parametros_locais():
    """
    Demonstra o conceito de variáveis e parâmetros locais, ilustrando como
    o escopo limita a existência e a visibilidade de dados dentro de funções.
    """
    print("--- Variáveis e Parâmetros Locais ---\n")
    print(
        "Quando criamos uma variável dentro de uma função, ela é 'local', "
        "o que significa que só existe dentro do escopo dessa função. Esta "
        "função, por exemplo, recebe dois argumentos, concatena-os e exibe "
        "o resultado duas vezes.\n"
    )

    # ----- Trecho da função 'parametros' copiado para demonstração -----

    # Definição de função que requer um argumento
    def print_twice(string):  # (string) -> parâmetro da função
        print(string)
        print(string)

    def cat_twice(part1, part2):
        cat = part1 + part2
        print_twice(cat)

    line1 = "Always look on the "
    line2 = "bright side of life."

    cat_twice(line1, line2)

    # Quando 'cat_twice' é executada, ela cria uma variável local chamada
    # 'cat', que é destruída assim que a função termina. Se tentarmos exibi-la,
    # receberemos um 'NameError'.
    # Para testar o erro, descomente a linha abaixo:
    # print(cat)  # NameError: name 'cat' is not defined

    # Fora da função, 'cat' não está definida.
    # Os parâmetros também são locais. Por exemplo, fora de 'cat_twice', não
    # existem 'part1' ou 'part2'.


def diagrama_de_pilha():
    """
    Demonstra o conceito de diagrama de pilha (Call Stack) utilizando
    dicionários simples para representar de forma legível os frames
    de memória ativos.
    """
    print("--- Diagrama de Pilha ---\n")
    print(
        "Para acompanhar quais variáveis podem ser utilizadas e onde, é útil "
        "desenhar um 'diagrama de pilha'. Semelhante aos diagramas de estado, "
        "os diagramas de pilha mostram o valor de cada variável, mas também "
        "indicam a função à qual cada variável pertence.\n"
    )
    print(
        "Cada função é representada por um 'frame' (quadro). Um frame é uma "
        "caixa que contém o nome da função e, dentro dela, os parâmetros e as "
        "variáveis dessa função.\n"
        "Aqui está o diagrama de pilha para o exemplo anterior:\n"
    )

    # OBS: No caso da arquitetura deste repositório, as variáveis 'line1' e
    # 'line2' não estão no escopo global (__main__), e sim no escopo da função
    # 'variaveis_e_parametros_locais'.
    __main__ = {
        "line1": "Always look on the ",
        "line2": "bright side of life."
    }
    cat_twice = {
        "part1": "Always look on the ",
        "part2": "bright side of life.",
        "cat": "Always look on the bright side of life."
    }
    print_twice = {
        "string": "Always look on the bright side of life."
    }
    _print = {
        "?": "Always look on the bright side of life."
    }

    print("[ Frame: __main__ ]")
    for variavel in __main__:
        print(" ", variavel, "->", __main__[variavel])
    print("-" * 40)

    print("[ Frame: cat_twice ]")
    for variavel in cat_twice:
        print(" ", variavel, "->", cat_twice[variavel])
    print("-" * 40)

    print("[ Frame: print_twice ]")
    for variavel in print_twice:
        print(" ", variavel, "->", print_twice[variavel])
    print("-" * 40)

    print("[ Frame: print ]")
    for variavel in _print:
        print(" ", variavel, "->", _print[variavel])
    print("-" * 40)
    print()

    print(
        "Os frames são organizados em uma pilha, indicando a sequência de "
        "funções que foram chamadas uma pela outra, e assim por diante. "
        "Lendo de baixo para cima, 'print' foi chamada por 'print_twice', que "
        "foi chamada por 'cat_twice', que por sua vez foi chamada por "
        "'__main__' -- que é um nome especial para o frame mais alto na "
        "pilha. Quando criamos uma variável fora de qualquer função, ela "
        "pertence ao escopo de '__main__'.\n"
    )
    print(
        "No frame de 'print', o ponto de interrogação indica que não sabemos "
        "o nome do parâmetro interno por se tratar de uma função nativa."
    )


def tracebacks():
    """
    Demonstra o conceito de traceback (pilha de rastreamento de erros),
    ilustrando como o Python rastreia a sequência de chamadas de funções
    de volta até a origem de um erro de tempo de execução.
    """
    print("--- Tracebacks (Rastreamento de Erros) ---\n")
    print(
        "Quando ocorre um erro de tempo de execução em uma função, o Python "
        "exibe o nome da função que estava sendo executada, seguido pelo "
        "nome da função que a chamou, e assim por diante, subindo na pilha de "
        "chamadas.\n"
    )
    print(
        "Para ilustrar, vamos definir uma versão da função 'print_twice' que "
        "contém um erro -- ela tenta exibir 'cat', que é uma variável local "
        "em outra função:\n"
    )

    # Para testar o erro, descomente as linhas com 'print(cat)' abaixo:
    def print_twice(string):
        pass
        # print(cat)  # NameError
        # print(cat)  # NameError

    # ----- Trecho da função 'parametros' copiado para demonstração -----

    def cat_twice(part1, part2):
        cat = part1 + part2
        print_twice(cat)

    line1 = "Always look on the "
    line2 = "bright side of life."

    print("Executando a cadeia de funções para gerar o traceback:\n")
    cat_twice(line1, line2)

    print(
        "\nA mensagem de erro inclui um 'traceback', que revela a função que "
        "estava sendo executada quando o erro ocorreu, a função que a chamou, "
        "e assim por diante. Nesse exemplo, o traceback indica que "
        "'cat_twice' chamou 'print_twice', e o erro aconteceu dentro de "
        "'print_twice'."
    )
    # A ordem das funções no traceback é a mesma que a ordem dos frames no
    # diagrama de pilha. A função que está sendo executada no momento
    # aparece no final.


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # definindo_novas_funcoes()
    # parametros()
    # chamando_funcoes()
    # repeticao()
    # variaveis_e_parametros_locais()
    # diagrama_de_pilha()
    # tracebacks()
    pass
