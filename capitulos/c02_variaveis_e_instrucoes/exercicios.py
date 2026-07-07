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


def exercicio_2_3():
    """Exercício 3 (Capítulo 2)"""
    print(
        "Em algumas linguagens, cada instrução termina com um ponto e vírgula "
        "(;). O que acontece se você colocar um ponto e vírgula no final de "
        "uma instrução em Python?"
    )
    print(
        "\n"
        "O programa funciona normalmente. Em Python, o ponto e vírgula (;) "
        "não é obrigatório no final das linhas porque a quebra de linha já "
        "indica o fim da instrução."
        "\n"
        "Obs: Se estiver utilizando um linter como o Flake8, ele acusará um "
        "aviso de estilo (E703), mas o código executará sem erros."
    )


def exercicio_2_4():
    """Exercício 4 (Capítulo 2)"""
    print(
        "E se você colocar um ponto no final de uma instrução?"
    )
    print(
        "\n"
        "Se colocar um ponto (.) no final de alguma instrução, o Python "
        "acusará um erro: 'SyntaxError: invalid syntax'."
    )


def exercicio_2_5():
    """Exercício 5 (Capítulo 2)"""
    print(
        "O que ocorre se você digitar o nome de um módulo incorretamente "
        "e tentar importar 'maath'?"
    )
    print(
        "\n"
        "Se tentar importar um módulo inexistente ou digitar o nome do módulo "
        "errado (maath), o Python acusará o erro: 'ModuleNotFoundError: "
        "No module named 'maath''"
    )


def exercicio_2_6():
    """Exercício 6 (Capítulo 2)"""
    print(
        "O volume de uma esfera com raio r é: V = (4/3) * π * r³. Qual seria "
        "o volume de uma esfera com raio 5? Comece criando uma variável "
        "chamada 'radius' e depois armazene o resultado em uma variável "
        "chamada 'volume'. Exiba o resultado. Adicione comentários para "
        "indicar que 'radius' está em centímetros e 'volume' em centímetros "
        "cúbicos."
    )
    import math
    # radius está em centímetros (cm)
    radius = 5
    # o volume está em centímetros cúbicos (cm³)
    volume = (4 / 3) * math.pi * radius ** 3
    print(
        "\n"
        f"O volume de uma esfera com raio 5cm é '{volume}' (em cm³)."
    )


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_2_1()
    # exercicio_2_2()
    # exercicio_2_3()
    # exercicio_2_4()
    # exercicio_2_5()
    # exercicio_2_6()
    pass
