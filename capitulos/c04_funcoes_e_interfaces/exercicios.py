# Exercícios do Capítulo 4 - Funções e Interfaces

from turtle import forward, pendown, penup

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


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # jump(100)
    pass
