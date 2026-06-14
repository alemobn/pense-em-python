# Exercícios do Capítulo 1 - Programação como uma forma de pensar


def exercicio_1_1():
    """Exercício 1 (Capítulo 1)"""
    print(
        'Você pode se perguntar o que a função "round" faz se um número '
        'terminar em "0.5". A resposta é que, às vezes, ela arredonda '
        "para cima e, às vezes, arredonda para baixo. Experimente os "
        "seguintes exemplos e veja se consegue descobrir qual regra ela "
        "segue:"
        "\n"
    )
    print(round(42.5))
    print(round(43.5))
    print(
        "\n"
        "* R: Em Python, o arredondamento não segue a mesma regra da "
        "Matemática. O motivo de o Python arredondar para cima e, às vezes, "
        "para baixo é porque ele segue um padrão internacional "
        'chamado de "Arredondamento Bancário (Round to Even)". Este '
        'comportamento segue a norma "IEEE 754". O motivo é puramente '
        "estatístico: se você tiver uma lista enorme de números terminados "
        'em "0.5" e sempre arredondar para cima, o resultado final de uma '
        "soma ou média desses dados será artificialmente inflado. "
        "Arredondando metade das vezes para cima e metade para baixo "
        "(em direção ao par), o erro de arredondamento se cancela mutuamente, "
        "mantendo as estatísticas financeiras e científicas muito mais "
        "precisas."
    )


def exercicio_1_2():
    """Exercício 2 (Capítulo 1)"""
    print(
        "Podemos utilizar um sinal de menos para indicar um número negativo, "
        'como "-2". O que acontece se colocarmos um sinal de mais antes de um '
        'número? E se escrevermos assim: "2++2"?'
        "\n"
    )
    print(+2)
    print(2++2)
    print(
        "\n"
        '* R: Ao colocarmos "+2", estamos indicando explicitamente que o '
        'número "2" é positivo. '
        'A expressão "2++2" está definindo o segundo operando como positivo '
        "e somando-o com número 2."
    )


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_1_1()
    # exercicio_1_2()
    pass
