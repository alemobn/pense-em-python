"""
Capítulo 3: Funções

Tópicos estudados:
- Definindo novas funções
- Parâmetros
- Chamando funções
- Repetição
- Variáveis e parâmetros são locais
- Diagrama de pilha
- Tracebacks
- Por que utilizar funções?
- Depuração
- Glossário
- Exercícios
"""


def definindo_novas_funcoes():
    """
    Explica a criação de uma função básica, a diferença entre o objeto da
    função na memória e a sua execução real através do operador de chamada.
    """
    print("--- Definindo novas funções ---\n")

    def print_lyrics():  # <- cabeçalho da função
        # Tudo que está abaixo do cabeçalho e indentado -> corpo da função
        print("I'm a lumberjack, and I'm okay.")
        print("I sleep all night and I work all day.")

    print(
        "'def' é uma palavra reservada que indica uma definição de função. "
        "O nome da função é 'print_lyrics'. Qualquer nome de variável "
        "válido também pode ser utilizado como nome de função."
        "\n\n"
        "Os parênteses vazios após o nome da função indicam que ela não "
        "recebe argumentos."
        "\n\n"
        "Definir uma função cria um 'objeto de função', que é alocado na "
        "memória RAM e pode ser referenciado como qualquer outra variável. "
        "Podemos exibir o ponteiro desse objeto da seguinte maneira:"
        "\n"
    )
    print(print_lyrics)  # Exibindo o objeto da função
    print()
    print_lyrics()  # Chamando a função (execução)


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # definindo_novas_funcoes()
    pass
