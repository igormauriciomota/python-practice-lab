def menu():
    print("=== Escolha a Opção desejada ===")

menu()

def calculadora():

    while True:

        numero1 = int(input("Digite o Primeiro numero: "))
        numero2 = int(input("Digite o Segundo numero: "))

        print("[1] Soma")
        print("[2] Subitração")
        print("[3] Multiplicação")
        print("[4] Divisão")
        print("[5] Potencia")
        print("[0] Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            resultado = numero1 + numero2
            print(f"{numero1} + {numero2} = {resultado}")

        elif opcao == 2:
            resultado = numero1 - numero2
            print(f"{numero1} - {numero2} = {resultado}")

        elif opcao == 3:
            resultado = numero1 * numero2
            print(f"{numero1} x {numero2} = {resultado}")

        elif opcao == 4:
            if numero2 != 0:
                resultado = numero1 / numero2
                print(f"{numero1} / {numero2} = {resultado}")
            else:
                print("Zero nao e um numero valido")

        elif opcao == 5:
            resultado = numero1 ** numero2
            print(f"{numero1} Potencia {numero2} = {resultado}")

        elif opcao == 0:
            break

calculadora()
