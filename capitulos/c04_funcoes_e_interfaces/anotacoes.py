"""
Capítulo 4: Funções e interfaces

Tópicos estudados:
- Módulo jupyturtle (turtle)
- Desenhando um quadrado
- Encapsulamento e generalização
- Desenhando um círculo por aproximação
- Refatorando o código
- Diagrama de pilha
- Docstrings
- Depuração
- Glossário
- Exercícios
"""


def modulo_turtle():
    """
    Introdução aos gráficos de tartaruga
    """
    print("--- Gráficos com a Tartaruga ---\n")

    # No livro, é utilizado o módulo 'jupyturtle'.
    # Para utilizar o módulo nativo 'turtle' no Fedora, é necessário rodar:
    # sudo dnf install python3-tkinter
    from turtle import Turtle, done, forward, left

    # Inicializa a tela gráfica e a tartaruga
    Turtle()

    # Desenha uma quina movendo-se para a frente e virando à esquerda
    forward(50)
    left(90)
    forward(50)

    # Mantém a janela gráfica aberta após a execução
    done()


def desenhando_um_quadrado():
    """
    Introdução aos gráficos de tartaruga
    """
    print("--- Desenhando um Quadrado ---\n")
    from turtle import Turtle, forward, left

    # Turtle()

    # forward(50)
    # left(90)

    # forward(50)
    # left(90)

    # forward(50)
    # left(90)

    # forward(50)
    # left(90)

    # done()

    # Como esse programa repete o mesmo par de linha quatro vezes,
    # podemos fazer a mesma coisa de forma mais concisa utilizando
    # um loop for:

    Turtle()
    for i in range(4):
        forward(50)
        left(90)


def encapsulamento_e_generalizacao():
    """
    Demonstra os conceitos de encapsulamento e generalização
    desenhando polígonos com o módulo turtle (Capítulo 4)
    """
    print("--- Encapsulamento e Generalização ---\n")

    from turtle import Turtle, done, forward, left

    # Coloca o código de desenho do quadrado em uma função 'square',
    # encapsulando a repetição do fluxo em um único bloco.
    def square(length):
        for _ in range(4):
            forward(length)
            left(90)

    Turtle()
    # square(30)
    # square(60)

    # Generaliza o conceito do quadrado para desenhar qualquer polígono
    # regular de 'n' lados com comprimento 'length'.
    def polygon(n, length):
        angle = 360 / n
        for _ in range(n):
            forward(length)
            left(angle)

    # Quando uma função tem vários argumentos numéricos, é fácil esquecer
    # o que eles representam ou a ordem em que devem ser fornecidos. Por isso
    # é boa prática incluir os nomes dos parâmetros (argumentos nomeados).
    polygon(n=7, length=30)

    done()


def desenhando_um_circulo_por_aproximacao():
    """
    Demonstra a criação de um círculo aproximando-o por um polígono
    com múltiplos lados usando o módulo turtle (Capítulo 4)
    """
    print("--- Desenhando um Círculo por Aproximação ---\n")

    import math
    from turtle import Turtle, done, forward, left

    # Reutiliza a função de polígono para desenhar uma figura de 'n' lados
    def polygon(n, length):
        angle = 360 / n
        for _ in range(n):
            forward(length)
            left(angle)

    # A função 'circle' recebe o raio do círculo como parâmetro. Ela calcula
    # a circunferência de um círculo com o raio fornecido.
    # O parâmetro 'n' representa o número de lados do polígono aproximado,
    # e o valor de 'circumference / n' determina o comprimento de cada um
    # desses lados.
    def circle(radius):
        circumference = 2 * math.pi * radius
        n = 30
        length = circumference / n
        polygon(n, length)

    Turtle()
    circle(30)
    done()


def refatorando_o_codigo():
    """
    Demonstra a refatoração do código de desenho criando a função
    'polyline' para reutilização em polígonos, arcos e círculos (Capítulo 4)
    """
    print("--- Refatorando o Código (Polyline) ---\n")

    # Agora, vamos escrever uma versão mais geral da função 'circle',
    # chamada 'arc', que recebe um segundo parâmetro, 'angle', e desenha
    # um arco de círculo correspondente ao ângulo especificado.

    import math
    from turtle import Turtle, done, forward, left

    # A função 'polyline' recebe como parâmetros o número de segmentos de
    # linha a serem desenhados, 'n'; o comprimento dos segmentos, 'length',
    # e o ângulo entre eles, 'angle'.
    def polyline(n, length, angle):
        for _ in range(n):
            forward(length)
            left(angle)

    # Reescrevendo a função 'polygon' para utilizar 'polyline':
    def polygon(n, length):
        angle = 360.0 / n
        polyline(n, length, angle)

    # A função 'arc' é similar à 'circle', mas com a diferença de que ela
    # calcula 'arc_length' (comprimento do arco), que corresponde a uma
    # fração da circunferência de um círculo.
    # Utilizando 'polyline' para escrever a função 'arc':
    def arc(radius, angle):
        arc_length = 2 * math.pi * radius * angle / 360
        n = 30
        length = arc_length / n
        step_angle = angle / n
        polyline(n, length, step_angle)

    # Reescrevendo a função 'circle' para utilizar a função 'arc'
    def circle(radius):
        arc(radius, 360)

    # Para garantir que essas funções funcionem como esperado, vamos
    # utilizá-las para desenhar algo que se assemelhe a um caracol.
    Turtle()
    polygon(n=20, length=9)
    arc(radius=70, angle=70)
    circle(radius=10)
    done()


def diagrama_de_pilha():
    """
    Explica a sequência de chamadas de funções e o escopo local de parâmetros
    utilizando um diagrama de pilha (Capítulo 4)
    """
    print("--- Diagrama de Pilha e Escopo Local ---\n")

    # Na função 'refatorando_o_codigo', quando chamamos a função 'circle', ela
    # chama a função 'arc', que por sua vez chama a função 'polyline'.
    #
    # Representação da sequência de frames na pilha de chamadas (Stack):
    # ------------------------------------------------------------------------
    # __main__:
    #   └── circle(radius=30)
    #         └── arc(radius=30, angle=360)
    #               └── polyline(n=30, length=6.28, angle=12.0)
    # ------------------------------------------------------------------------
    #
    # É importante observar que o parâmetro 'angle' na função 'polyline'
    # armazena o ângulo de cada passo (step_angle), enquanto 'angle' na
    # função 'arc' representa o ângulo total do arco. Como os parâmetros e
    # variáveis são locais ao frame de execução da função, eles residem em
    # endereços de memória independentes na pilha.

    print("Conceito teórico: Variáveis locais e pilha de execução.")
    print("Cada chamada de função empilha um novo frame isolado na memória.\n")


def plano_de_desenvolvimento():
    """
    Sintetiza o processo de desenvolvimento via encapsulamento,
    generalização e refatoração (Capítulo 4)
    """
    print("--- Plano de Desenvolvimento de Software ---\n")

    import math
    from turtle import forward, left

    # Explicação do fluxo de design incremental
    print("Passos do Plano de Desenvolvimento:")
    print("1. Escreva um script pequeno e funcional sem funções.")
    print("2. Encapsule o código funcional dentro de uma função.")
    print("3. Generalize a função adicionando os parâmetros necessários.")
    print("4. Repita os passos anteriores estruturando o código em módulos.")
    print("5. Refatore para eliminar código duplicado e melhorar abstrações.")
    print()

    print("Interface vs. Implementação:")
    print(
        "- Interface: O 'o quê' (nome da função, parâmetros e o que ela "
        "promete fazer)."
    )
    print("- Implementação: O 'como' (o código interno que executa a lógica).")
    print()

    # ------ Trecho copiado da função 'encapsulamento_e_generalizacao' ------
    def polygon(n, length):
        angle = 360 / n
        for _ in range(n):
            forward(length)
            left(angle)

    # ------ Trecho copiado da função 'refatorando_o_codigo' ------
    def polyline(n, length, angle):
        for _ in range(n):
            forward(length)
            left(angle)

    def arc(radius, angle):
        arc_length = 2 * math.pi * radius * angle / 360
        n = 30
        length = arc_length / n
        step_angle = angle / n
        polyline(n, length, step_angle)

    # Primeira versão da interface 'circle' usando a implementação via
    # 'polygon'
    def circle(radius):
        circumference = 2 * math.pi * radius
        n = 30
        length = circumference / n
        polygon(n, length)

    # Versão refatorada que altera a implementação interna para usar 'arc',
    # mantendo a interface (uso) exatamente idêntica para o chamador.
    def re_circle(radius):
        arc(radius, 360)

    print("Implementações 'circle' e 're_circle' prontas para teste.")


def docstrings():
    """
    Explica a importância das docstrings e como documentar interfaces
    de funções em Python (Capítulo 4)
    """
    print("--- Docstrings e Documentação de Interface ---\n")

    from turtle import forward, left

    def polyline(n, length, angle):
        """
        Desenha segmentos de linha com o comprimento (length) e o ângulo
        (angle) fornecidos entre eles.

        n: número inteiro de segmentos de linha
        length: comprimento dos segmentos (número)
        angle: ângulo entre os segmentos em graus (número)
        """
        for _ in range(n):
            forward(length)
            left(angle)

    print("O que é uma Docstring?")
    print("- Uma string no início da função para explicar sua interface.")
    print("- Por convenção, utiliza-se aspas triplas (strings multilinhas).\n")

    print("Boas práticas para escrever Docstrings:")
    print("- Explicar o que a função faz (sem focar no 'como' funciona).")
    print("- Descrever como cada parâmetro influencia o comportamento.")
    print("- Indicar o tipo esperado de cada parâmetro se não for óbvio.\n")

    print(
        "Escrever documentação é parte vital do design de interface. "
        "Se for difícil descrever uma função, a interface provavelmente "
        "precisa ser simplificada ou aprimorada."
    )


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # modulo_turtle()
    # desenhando_um_quadrado()
    # encapsulamento_e_generalizacao()
    # desenhando_um_circulo_por_aproximacao()
    # refatorando_o_codigo()
    # diagrama_de_pilha()
    # plano_de_desenvolvimento()
    # docstrings()
    pass
