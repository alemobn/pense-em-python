"""
Capítulo 4: Funções e interfaces

Tópicos estudados:
- Módulo jupyturtle (turtle)
- Desenhando um quadrado
- Encapsulamento e generalização
- Desenhando um círculo por aproximação
- Refatorando o código
- Diagrama de pilha
- Docstrings
- Depuração
- Glossário
- Exercícios
"""


def modulo_turtle():
    """
    Introdução aos gráficos de tartaruga
    """
    print("--- Gráficos com a Tartaruga ---\n")

    # No livro, é utilizado o módulo 'jupyturtle'.
    # Para utilizar o módulo nativo 'turtle' no Fedora, é necessário rodar:
    # sudo dnf install python3-tkinter
    from turtle import Turtle, done, forward, left

    # Inicializa a tela gráfica e a tartaruga
    Turtle()

    # Desenha uma quina movendo-se para a frente e virando à esquerda
    forward(50)
    left(90)
    forward(50)

    # Mantém a janela gráfica aberta após a execução
    done()


if __name__ == "__main__":
    # Tire o '#' apenas da função que deseja testar

    # modulo_turtle()
    pass
