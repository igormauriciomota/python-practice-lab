fila = []

while True:
    print("\n1-Adicionar 2-Atender 3-listar 0-sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        nome = input("Cliente: ").strip().title()
        if nome:
            fila.append(nome)
    elif opcao == 2:
        if fila:
            print(f"Atendendo: {fila.pop(0)}")
        else:
            print("Fila vazia!")
    elif opcao == 3:
        print(f"Fila atiual: {fila}")
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")
print("Fim do programa!")