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


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_3_1()
    pass
