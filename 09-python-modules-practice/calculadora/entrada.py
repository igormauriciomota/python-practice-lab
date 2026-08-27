# Entrada da calculadora
def ler_numero(mensagem):
    # repete até o usuario digitar um numero valido.
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Digite um número válido.")


def ler_operacao():
    # Exibe o menu e devolve a operação escolhida.
    print("\n=== OPERAÇOES ===")
    print("1 - Somar")
    print("2 - Subitrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    return input("Escolha uma operação: ").strip()