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


def nomes_de_variaveis():
    """
    Explicar as regras de nomenclatura de variáveis e identificar palavras
    reservadas.
    """
    print("--- Demonstração de Nomes de Variáveis ---\n")
    # Nomes de variáveis não têm limite de tamanho.
    # Podem conter tanto letras quanto números, mas não podem
    # começar com um número.
    # É possível utilizar letras maiúsculas, mas a recomendação
    # é utilizar apenas letras minúsculas.
    # O único sinal de pontuação permitido em nomes de variáveis
    # é o "underscore(_)".
    # -------------------------------------------------------------
    # Se atribuirmos um nome inválido a uma variável, receberemos
    # um erro de sintaxe. Por exemplo, o nome "million!" é inválido
    # porque contém pontuação.
    # Para testar o erro, descomente a linha abaixo:
    # million! = 1000000
    # -------------------------------------------------------------
    # "76trombones = 'big parade'" é inválido porque começa com um
    # número
    # Para testar o erro, descomente a linha abaixo:
    # 76trombones = 'big parade'
    # -------------------------------------------------------------
    # "class" também é inválido, mas pode não ser óbvio o porquê
    # Para testar o erro, descomente a linha abaixo:
    # class = 'Self-Defense Against Fresh Fruit'
    # Acontece que class é uma "palavra reservada", ou seja, é
    # uma palavra especial utilizada para especificar a estrutura
    # de um programa. Palavras reservadas não podem ser utilizadas
    # como nomes de variáveis.
    # -------------------------------------------------------------
    # Aqui está uma lista completa das palavras reservadas do
    # Python (não é necessário memorizar essa lista):
    palavras_reservadas = [
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "case", "class", "continue", "def", "del", "elif", "else",
        "except", "finally", "for", "from", "global", "if", "import", "in",
        "is", "lambda", "match", "nonlocal", "not", "or", "pass", "raise",
        "return", "try", "while", "with", "yield"
    ]
    print(", ".join(palavras_reservadas))


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # variaveis()
    # diagramas_de_estado()
    # nomes_de_variaveis()
    pass
