"""
Capítulo 1: Programação como uma forma de pensar

Tópicos estudados:
- Operadores aritméticos
- Expressões
- Funções aritméticas
- Strings
- Valores e tipos
- Linguagens formais e naturais
- Depuração
"""


def operadores_aritmeticos():
    """Aborda operadores aritméticos"""
    print("--- Demonstração dos Operadores Aritméticos ---\n")
    print("Adição (+): 30 + 12 =", 30 + 12)
    print("Subtração (-): 43 - 1 =", 43 - 1)
    print("Multiplicação (*): 6 * 7 =", 6 * 7)
    print("Divisão (/): 84 / 2 =", 84 / 2)
    # Nota de estudo: O resultado de (/) é 42.0 (float) em vez de 42 (int).
    # Divisões comuns em Python sempre retornam um número de ponto flutuante.
    # O operador (//) realiza a divisão inteira (floor division),
    # que sempre arredonda o resultado para baixo, em direção ao "piso".
    print("Divisão inteira (//): 85 // 2 =", 85 // 2)
    print("Exponenciação (**) 7 ** 2 =", 7 ** 2)


def expressoes():
    """Aborda o que é uma expressão"""
    print("--- Demostrando o que é uma Expressão ---\n")
    print("Expressão: 6 + 6 ** 2 =", 6 + 6 ** 2)
    print("Expressão: 12 + 5 * 6 =", 12 + 5 * 6)
    print("Expressão: (12 + 5) * 6 =", (12 + 5) * 6)
    # Nota de estudo: Uma expressão é composta por um ou mais operadores
    # e números.
    # Toda expressão resulta em um Valor.


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # operadores_aritmeticos()
    # expressoes()
    pass
