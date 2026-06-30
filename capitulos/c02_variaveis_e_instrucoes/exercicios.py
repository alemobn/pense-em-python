# Exercícios do Capítulo 1 - Variáveis e instruções


def exercicio_2_1():
    """Exercício 1 (Capítulo 2)"""
    print(
        "Vimos que n = 17 é válido. Mas e 17 = n?"
    )
    print(
        "\n"
        "* R: 17 = n é inválido. No Python, a atribuição é feita da direita "
        "para a esquerda, ou seja, o lado esquerdo do '=' deve ser sempre o "
        "nome de uma variável (um identificador) e não um valor literal como "
        "o número 17. O Python retornará um 'SyntaxError: cannot assign to "
        "literal'."
    )


def exercicio_2_2():
    """Exercício 2 (Capítulo 2)"""
    print(
        "E quanto a x = y = 1?"
    )
    print(
        "\n"
        "x = y = 1 é válido, mas não é recomendável. "
        "O Python lê o valor literal (1) e faz com que, tanto x quanto y "
        "apontem para o mesmo literal na memória (1)."
    )


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_2_1()
    # exercicio_2_2()
    pass
