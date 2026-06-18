"""
Capítulo 2: Variáveis e instruções

Tópicos estudados:
- Variáveis
- Diagramas de estado
- Nomes de variáveis
- Instrução import
- Expressões e instruções
- Função print
- Argumentos
- Comentários
- Depuração
- Glossário
- Exercícios
"""


def variaveis():
    """
    Demonstrar o conceito de atribuição e uso de variáveis na memória.
    """
    print("--- Demonstração de Variáveis ---\n")
    # Uma "variável" é um nome que se refere a um valor.
    n = 17
    pi = 3.141592653589793
    message = 'And now for something completely different'
    # Podemos utilizar uma variável como parte de uma expressão
    # com operadores aritméticos:
    print(n + 25)
    print(2 * pi)
    # Também é possível empregar uma variável ao chamar uma
    # função:
    print(round(pi))
    print(len(message))


def diagramas_de_estado():
    """
    Exemplificar a representação visual de variáveis e seus valores na memória.
    """
    print("--- Demonstração de Diagramas de Estado ---\n")
    # Uma forma comum de representar variáveis por escrito é
    # colocar o nome com uma seta apontada para o seu valor:
    print('n ----> 17')
    print('pi ----> 3.141592653589793')
    print('message ----> \'And now for something completely different\'')
    # Esse tipo de figura é denominado "diagrama de estado" porque
    # ilustra a condição atual de cada uma das variáveis (pense
    # nisso como o estado da variável).
    # Utilizaremos diagramas de estado ao longo deste livro para
    # representar um modelo de como o Python armazena variáveis
    # e seus respectivos valores.


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # variaveis()
    # diagramas_de_estado()
    pass
