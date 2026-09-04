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


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # jump(100)
    # exercicio_4_1()
    pass
