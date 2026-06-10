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
    print("--- Demonstrando o que é uma Expressão ---\n")
    print("Expressão: 6 + 6 ** 2 =", 6 + 6 ** 2)
    print("Expressão: 12 + 5 * 6 =", 12 + 5 * 6)
    print("Expressão: (12 + 5) * 6 =", (12 + 5) * 6)
    # Nota de estudo: Uma expressão é composta por um ou mais operadores
    # e números.
    # Toda expressão resulta em um valor.


def funcoes_aritmeticas():
    """Aborda funções aritméticas"""
    print(
        "--- Demonstrando algumas Funções Aritméticas "
        "(Funções que operam com números) ---\n"
    )
    # Nota de estudo: O Python oferece diversas funções que operam com
    # números. Por exemplo, a função "round" recebe um número do tipo float
    # e o arredonda para o número inteiro mais próximo.
    print("round(42.4) =", round(42.4))
    print("round(42.6) =", round(42.6))
    # A função "abs" calcula o valor absoluto de um número.
    # Em caso de um número positivo, o valor absoluto é o próprio número.
    print("abs(42) =", abs(42))
    # Em caso de um número negativo, o valor absoluto é o valor positivo
    # correspondente.
    print("abs(-42) =", abs(-42))
    # Quando utilizamos uma função dessa forma, dizemos que estamos
    # "chamando" a função. Uma expressão que chama uma função é chamada
    # de "chamada de função".
    # Ao chamar uma função, é obrigatório utilizar parênteses. Caso você
    # os omita, uma mensagem de erro será exibida.
    # Para testar o erro, descomente a linha abaixo:
    # print(abs 42) # SyntaxError: invalid syntax


def strings():
    """Aborda strings"""
    print("--- Demonstrando o que é uma String ---\n")
    # Nota de estudo: Uma string é uma sequência de caracteres dentro
    # de aspas:
    print('Hello')
    # Também podemos utilizar aspas duplas:
    print("World")
    # Aspas duplas são úteis quando precisamos incluir um apóstrofo
    # na string, já que o apóstrofo é o mesmo símbolo que uma aspa
    # simples:
    print("it's a small ")
    # Strings podem conter espaços, pontuações e números:
    print('Well, ')
    # O operador "+" funciona com strings; ele une duas strings em
    # uma única string, o que é chamado de "concatenação":
    print('Well, ' + "it's a small " + 'world.')
    # O operador "*" também funciona com strings; ele cria múltiplas
    # cópias de uma string e as concatena:
    print('Spam, ' * 4)
    # O Python disponibiliza a função "len", que calcula o comprimento
    # de uma string:
    print(len('Spam'))
    # Ao criar uma string, certifique-se de utilizar apenas aspas retas.
    # Utilizar crases (backticks), aspas inteligentes ou aspas curvas
    # é considerado inválido e resultará em um erro de sintaxe:
    # Para testar o erro, descomente a linha abaixo:
    # print(`Hello`) # SyntaxError: invalid syntax


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # operadores_aritmeticos()
    # expressoes()
    # funcoes_aritmeticas()
    # strings()
    pass
