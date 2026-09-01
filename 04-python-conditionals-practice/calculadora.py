continuar = "s"

while continuar == "s":

    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))

    print("Escolha a opção desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")

    opcao = int(input("Opção: "))

    if opcao == 1:
        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")

    elif opcao == 2:
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")

    elif opcao == 3:
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2} = {resultado}")

    elif opcao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"{numero1} / {numero2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif opcao == 5:
        resultado = numero1 ** numero2
        print(f"{numero1} Potência {numero2} = {resultado}")

    continuar = input("Deseja continuar? (s/n): ").lower()

print("Programa encerrado.")