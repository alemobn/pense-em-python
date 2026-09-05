# Exercícios do Capítulo 4 - Funções e Interfaces

from turtle import Turtle, forward, pendown, penup, left, done

print(
    "Para esses exercícios, existem algumas outras funções da tartaruga "
    "que podem ser úteis:\n"
    "'penup' -> Levantar a caneta imaginária da tartaruga para que ela "
    "não deixe um rastro ao se mover.\n"
    "'pendown' -> Abaixar a caneta de volta no canvas.\n"
    "A função a seguir utiliza 'penup' e 'pendown' para mover a tartaruga "
    "sem deixar um rastro:\n"
)


def jump(length):
    """
    Avançar unidades de comprimento sem deixar rastro.

    Pós-condição: Deixar a caneta abaixada.
    """
    penup()
    forward(length)
    pendown()


def exercicio_4_1():
    """Exercício 1 (Capítulo 4)"""
    print(
        "Escreva uma função chamada 'rectangle' que desenhe um retângulo "
        "com os comprimentos dos lados fornecidos."
    )
    print()

    def rectangle(width, height):
        """
        Desenha um retângulo com a largura (width) e altura (height) dadas.
        """
        for _ in range(2):
            forward(width)
            left(90)
            forward(height)
            left(90)

    Turtle()
    rectangle(100, 50)
    done()


def exercicio_4_2():
    """Exercício 2 (Capítulo 4)"""
    print(
        "Escreva uma função chamada 'rhombus' que desenhe um losango com "
        "um comprimento de lado e um ângulo interno fornecidos."
    )
    print()

    def rhombus(length, angle):
        """
        Desenha um losango dados o comprimento do lado e um ângulo interno.
        """
        for _ in range(2):
            forward(length)
            left(angle)
            forward(length)
            left(180 - angle)

    Turtle()
    rhombus(100, 60)
    done()


def exercicio_4_3():
    """Exercício 3 (Capítulo 4)"""
    print(
        "Desenvolva uma função mais genérica chamada 'parallelogram', "
        "que desenhe um quadrilátero com lados paralelos. Em seguida, "
        "reescreva as funções 'rectangle' e 'rhombus' para que "
        "utilizem a função 'parallelogram'."
    )
    print()

    def parallelogram(length1, length2, angle):
        """
        Desenha um paralelogramo com lados de comprimentos 'length1' e
        'length2' e ângulo interno 'angle'.
        """
        for _ in range(2):
            forward(length1)
            left(angle)
            forward(length2)
            left(180 - angle)

    def rectangle(width, height):
        """Reescreve 'rectangle' usando a abstração 'parallelogram'."""
        parallelogram(width, height, 90)

    def rhombus(length, angle):
        """Reescreve 'rhombus' usando a abstração 'parallelogram'."""
        parallelogram(length, length, angle)

    Turtle()
    rectangle(100, 50)
    jump(150)
    rhombus(60, 60)
    jump(150)
    parallelogram(100, 60, 60)
    done()


def exercicio_4_4():
    """Exercício 4 (Capítulo 4)"""
    print(
        "Escreva um conjunto de funções mais genéricas para desenhar "
        "formas como esta (tortas divididas em triângulos)."
    )
    print()

    def triangle(length, angle):
        """
        Desenha um segmento triangular (fatia da torta) e retorna
        ao centro pronto para a próxima fatia.
        """
        angle_base = (180 - angle) / 2
        forward(length)
        left(180 - angle_base)
        import math

        base = 2 * length * math.sin(math.radians(angle / 2))
        forward(base)
        left(180 - angle_base)
        forward(length)
        left(180)

    def draw_pie(n, length):
        """Desenha um polígono dividido em 'n' fatias triangulares."""
        angle = 360 / n
        for _ in range(n):
            triangle(length, angle)

    Turtle()
    draw_pie(5, 60)
    jump(150)
    draw_pie(6, 60)
    jump(150)
    draw_pie(7, 60)
    done()


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # jump(100)
    # exercicio_4_1()
    # exercicio_4_2()
    # exercicio_4_3()
    # exercicio_4_4()
    pass
