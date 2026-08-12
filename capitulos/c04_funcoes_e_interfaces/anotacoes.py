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


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # modulo_turtle()
    # desenhando_um_quadrado()
    # encapsulamento_e_generalizacao()
    # desenhando_um_circulo_por_aproximacao()
    # refatorando_o_codigo()
    pass
