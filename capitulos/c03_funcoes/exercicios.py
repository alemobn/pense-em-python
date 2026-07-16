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


def exercicio_3_4():
    """Exercício 4 (Capítulo 3)"""
    print(
        "Pergunte a um assistente virtual o que pode estar errado com esta "
        "versão de 'print_twice':\n"
    )

    # Função de exemplo:
    # def print_twice(string):
    #     print(cat)
    #     print(cat)

    # Reposta do assistente:
    print(
        "Erro no Escopo/Nome (NameError): A função recebe o parâmetro com o "
        "nome 'string', mas dentro do bloco tenta imprimir a variável 'cat', "
        "que não foi definida. O correto seria usar 'print(string)'."
    )


def exercicio_3_5():
    """Exercício 5 (Capítulo 3)"""
    print(
        "Escreva uma função chamada 'print_right', que receba uma string "
        "chamada 'text' como parâmetro e exiba essa string com espaços "
        "suficientes à frente para que a última letra esteja alinhada na "
        "40ª coluna da tela.\n"
        "Dica: utilize a função 'len', o operador de concatenação de strings "
        "(+) e o operador de repetição de strings (*).\n"
    )

    # Resposta:
    def print_right(text):
        spaces = 40 - len(text)
        print(" " * spaces + text)

    print_right("Monty")
    print_right("Python's")
    print_right("Flying Circus")


def exercicio_3_6():
    """Exercício 6 (Capítulo 3)"""
    print(
        "Escreva uma função chamada 'triangle' que receba uma string e um "
        "número inteiro, e desenhe um triângulo com a altura especificada, "
        "composto de múltiplas cópias da string.\n"
        "Dica: utilize a letra 'L' para imprimir o triângulo com altura de 5."
        "\n"
    )

    # Resposta:
    def triangle(letra, inteiro):
        vezes = 1
        for _ in range(0, inteiro):
            print(letra * vezes)
            vezes += 1

    triangle("L", 10)


def exercicio_3_7():
    """Exercício 7 (Capítulo 3)"""
    print(
        "Escreva uma função chamada 'rectangle' que receba uma string e dois "
        "números inteiros e desenhe um retângulo com a largura e a altura "
        "fornecidas, composto de cópias da string.\n"
        "Dica: utilize a letra 'H' para imprimir o retângulo.\n"
    )

    # Resposta:
    def rectangle(letra, largura, altura):
        for _ in range(0, altura):
            print(letra * largura)

    rectangle("H", 5, 4)


def exercicio_3_8():
    """Exercício 8 (Capítulo 3)"""
    print(
        "A música '99 Bottles of Beer' começa com este verso:\n"
        "- 99 bottles of beer on the wall,\n"
        "- 99 bottles of beer.\n"
        "- Take one down, pass it around,\n"
        "- 98 bottles of beer on the wall.\n"
        "Em seguida, o segundo verso é semelhante, exceto que começa com 98 "
        "garrafas e termina com 97. A música continua -- por um longo tempo "
        "-- até que não se reste nenhuma garrafa de cerveja (bottles of beer)."
    )
    print(
        "Escreva uma função chamada 'bottle_verse' que receba um número como "
        "parâmetro e exiba o verso que começa com o número de garrafas "
        "fornecido.\n"
        "Dica: considere começar com uma função que possa exibir a primeira, "
        "segunda ou última linha do verso, e depois utilize essa função para "
        "escrever 'bottle_verse'.\n"
        "Utilize esta chamada de função para exibir o primeiro verso: "
        "'bottle_verse(99)'\n"
        "Se quiser exibir a música inteira, pode utilizar este loop 'for', "
        "que conta de 99 até 1:\n"
    )

    # Resposta:
    def ajustar(numero):
        if numero == 0:
            return "no more bottles of beer"
        elif numero == 1:
            return "1 bottle of beer"
        else:
            return f"{numero} bottles of beer"

    def exibir_linha_topo(numero):
        sujeito = ajustar(numero)
        print(f"{sujeito.capitalize()} on the wall,")

    def exibir_linha_meio(numero):
        print(f"{ajustar(numero)}.")
        print("Take one down, pass it around,")

    def exibir_linha_fim(numero):
        print(f"{ajustar(numero - 1)} on the wall.")

    def bottle_verse(numero):
        exibir_linha_topo(numero)
        exibir_linha_meio(numero)
        exibir_linha_fim(numero)

    bottle_verse(99)  # sem loop for

    # Exemplo de loop for:
    for n in range(99, 0, -1):
        bottle_verse(n)
        print()


if __name__ == "__main__":
    # Tire o '#' apenas do exercício que deseja testar

    # exercicio_3_1()
    # exercicio_3_2()
    # exercicio_3_3()
    # exercicio_3_4()
    # exercicio_3_5()
    # exercicio_3_6()
    # exercicio_3_7()
    # exercicio_3_8()
    pass
