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


def exercicio_3_3():
    """Exercício 3 (Capítulo 3)"""
    print(
        "Escolha qualquer outra função mencionada neste capítulo e solicite "
        "ao assistente virtual que a escreva. O desafio é descrever a função "
        "com precisão suficiente para que o assistente virtual entenda "
        "exatamente o que você deseja. Utilize o vocabulário que você "
        "aprendeu até agora neste livro.\n"
    )
    # Função escolhida: 'print_twice'
    # Texto: Escreva uma função com o nome de 'print_twice', que recebe uma
    # string como argumento, e exibe essa string duas vezes com uma quebra
    # de linha.
    # Resposta:

    def print_twice(string):
        """
        Recebe uma string como argumento e a exibe duas vezes,
        com uma quebra de linha entre elas.
        """
        print(string)
        print(string)

    print_twice("String.")


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_3_1()
    # exercicio_3_2()
    # exercicio_3_3()
    pass
