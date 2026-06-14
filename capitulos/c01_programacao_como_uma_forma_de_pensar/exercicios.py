# Exercícios do Capítulo 1 - Programação como uma forma de pensar


def exercicio_1_1():
    """Exercício 1 (Capítulo 1)"""
    print(
        "Você pode se perguntar o que a função \"round\" faz se um número "
        "terminar em \"0.5\". A resposta é que, às vezes, ela arredonda "
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
        "chamado de \"Arredondamento Bancário (Round to Even)\". Este "
        "comportamento segue a norma \"IEEE 754\". O motivo é puramente "
        "estatístico: se você tiver uma lista enorme de números terminados "
        "em \"0.5\" e sempre arredondar para cima, o resultado final de uma "
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
        "como \"-2\". O que acontece se colocarmos um sinal de mais antes de "
        "um número? E se escrevermos assim: \"2++2\"?"
        "\n"
    )
    print(+2)
    print(2++2)
    print(
        "\n"
        "* R: Ao colocarmos \"+2\", estamos indicando explicitamente que o "
        "número \"2\" é positivo. "
        "A expressão \"2++2\" está definindo o segundo operando como positivo "
        "e somando-o com número 2."
    )


def exercicio_1_3():
    """Exercício 3 (Capítulo 1)"""
    print(
        "O que acontece se tivermos dois valores sem nenhum operador entre "
        "eles, como em \"4  2\"?"
        "\n"
    )
    # Descomente a linha abaixo caso queira testar o erro:
    # print(4  2)
    print(
        "* R: O interpretador do Python gera um erro de sintaxe (SyntaxError: "
        "invalid syntax). Isso acontece porque o Python analisa o código "
        "esperando um operador matemático para realizar uma ação entre os "
        "dois números. A mensagem complementar \"Perhaps you forgot a "
        "comma?\" surge porque a única forma válida de ter dois valores "
        "seguidos seria separando-os por uma vírgula, como em uma sequência "
        "ou passagem de argumentos."
    )


def exercicio_1_4():
    """Exercício 4 (Capítulo 1)"""
    print(
        "Se chamarmos uma função como \"round(42.5)\", o que ocorre se "
        "omitirmos um ou ambos os parênteses?"
        "\n"
    )
    # Descomente abaixo a linha de sua preferência para testar o erro:
    # print(round 42.5)
    # print(round(42.5)
    # print(round42.5))
    print(
        "* R:\n"
        "Se a função for executada sem ambos os parênteses, o Python irá "
        "gerar um erro de sintaxe (SyntaxError: invalid syntax).\n"
        "Se for executada omitindo o parênteses de fechamento, o erro será "
        "(SyntaxError: \"(\" was never closed).\n"
        "Se for executada omitindo o parênteses de abertura, o erro será "
        "(SyntaxError: unmatched \")\")."
    )


def exercicio_1_5():
    """Exercício 5 (Capítulo 1)"""
    print(
        "É importante lembrar que toda expressão tem um valor, e todo valor "
        "tem um tipo. Podemos utilizar a função \"type\" para identificar o "
        "tipo de qualquer valor."
        "\n"
        "Qual é o tipo de valor nas seguintes expressões? Faça sua melhor "
        "suposição para cada uma e depois utilize a função \"type\" para "
        "descobrir."
        "\n"
    )
    print(type(765))
    print(type(2.718))
    print(type('2 pi'))
    print(type(abs(-7)))
    print(type(abs(-7.0)))
    print(type(abs))
    print(type(int))
    print(type(type))
    print(
        "\n"
        "* R:\n"
        "\"765\" -> <class 'int'>\n"
        "\"2.718\" -> <class 'float'>\n"
        "\"'2 pi'\" -> <class 'str'>\n"
        "\"abs(-7)\" -> <class 'int'> (O valor retornado pela função é int)\n"
        "\"abs(-7.0)\" -> <class 'float'> (O valor retornado é float)\n"
        "\"abs\" -> <class 'builtin_function_or_method'> (É uma função "
        "nativa)\n"
        "\"int\" -> <class 'type'> (É a classe que define os inteiros)\n"
        "\"type\" -> <class 'type'> (É a classe que define os próprios tipos)"
    )


def exercicio_1_6():
    """Exercício 6 (Capítulo 1)"""
    print(
        "Quantos segundos existem em 42 minutos e 42 segundos?"
        "\n"
    )
    segundos_totais = 42 * 60 + 42
    print(segundos_totais)
    print(
        "\n*R: "
        f"Em 42 minutos e 42 segundos, existem {segundos_totais} segundos"
    )


def exercicio_1_7():
    """Exercício 7 (Capítulo 1)"""
    print(
        "Quantas milhas existem em 10 quilômetros? Dica: uma milha é "
        "equivalente a 1,61 quilômetro."
        "\n"
    )
    uma_milha_em_km = 1.61
    quilometros_totais = 10
    milhas_totais = quilometros_totais / uma_milha_em_km
    milhas_totais_arredondado = round(milhas_totais, 1)
    print(milhas_totais_arredondado)
    print(
        "\n*R: "
        f"Em 10 quilômetros existem {milhas_totais_arredondado} milhas."
    )


def exercicio_1_8():
    """Exercício 8 (Capítulo 1)"""
    print(
        "Se você correr 10 quilômetros em 42 minutos e 42 segundos, "
        "qual será o seu passo médio (tempo por milha em minutos e "
        "segundos)?"
        "\n"
    )
    km_total = 10
    minutos_base = 42
    segundos_base = 42
    milhas_total = km_total / 1.61
    # Tempo total convertido puramente para segundos
    tempo_total_segundos = (minutos_base * 60) + segundos_base
    # Passo médio em segundos por milha
    passo_em_segundos = tempo_total_segundos / milhas_total
    # Conversão para minutos e segundos
    passo_minutos = int(passo_em_segundos // 60)
    passo_segundos = int(passo_em_segundos % 60)
    passo_medio = f"{passo_minutos} minutos e {passo_segundos} segundos"
    print(passo_medio)
    print(
        "\n"
        f"*R: O passo médio é de {passo_medio} por milha."
    )


def exercicio_1_9():
    """Exercício 9 (Capítulo 1)"""
    print(
        "Qual é a sua velocidade média em milhas por hora?"
        "\n"
    )
    km_total = 10
    minutos_base = 42
    segundos_base = 42
    milhas_total = km_total / 1.61
    # Tempo total convertido puramente para horas
    tempo_em_horas = (minutos_base + (segundos_base / 60)) / 60
    # Velocidade = Distância / Tempo
    velocidade_media = milhas_total / tempo_em_horas
    velocidade_media_arredondada = f"{round(velocidade_media, 1)}"
    print(velocidade_media_arredondada)
    print(
        "\n"
        f"*R: A velocidade média é de {velocidade_media_arredondada} milhas "
        "por hora."
    )


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_1_1()
    # exercicio_1_2()
    # exercicio_1_3()
    # exercicio_1_4()
    # exercicio_1_5()
    # exercicio_1_6()
    # exercicio_1_7()
    # exercicio_1_8()
    # exercicio_1_9()
    pass
