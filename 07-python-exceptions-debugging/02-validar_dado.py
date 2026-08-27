def validar_dado(texto):


    try:
        dado_valido = int(texto)

    except ValueError as erro:
        raise ValueError("Digite um número valido.") from erro

    if dado_valido < 18:
        raise ValueError("Cadastro permitido somente para maiores de idade.")        

    return dado_valido


def solicitar_dado():

    while True:
        texto = input("Digite sua Idade: ").strip()

        try:
            return validar_dado(texto)

        except ValueError as erro:
            print("Erro:", erro)

def main():
    idade = solicitar_dado()

    print("\n--- RESULTADO ---")
    print(f"Idade cadastrada {idade} anos.")


main()