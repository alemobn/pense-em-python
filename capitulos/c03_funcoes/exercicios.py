# Exercícios do Capítulo 3 - Funções


def exercicio_3_1():
    """Exercício 1 (Capítulo 3)"""
    print(
        "Solicite ao seu assistente virtual favorite que 'escreva uma "
        "função chamada 'repeat' que recebe uma string e um número inteiro, e "
        "imprima a string o número de vezes especificado'.\n"
    )

    # Resposta:
    def repeat(string, vezes):
        """
        Recebe uma string e um número inteiro, e imprime a string
        o número de vezes especificado.
        """
        print(string * vezes)

    repeat("string", 5)


def exercicio_3_2():
    """Exercício 2 (Capítulo 3)"""
    print(
        "Se o resultado não incluir um loop 'for', pergunte: 'Poderia fazer "
        "isso com um loop for?'.\n"
    )

    # Resposta:
    def repeat(string, vezes):
        """
        Recebe uma string e um número inteiro, e imprime a string o número
        de vezes especificado utilizando um loop for
        """
        for _ in range(vezes):
            print(string, end="")
        print()

    repeat("string", 5)


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_3_1()
    # exercicio_3_2()
    pass
