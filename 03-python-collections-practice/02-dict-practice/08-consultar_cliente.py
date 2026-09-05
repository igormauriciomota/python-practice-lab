clientes = {}

while True:
    print("\n---MENU---")
    print("[1] Cadastrar")
    print("[2] Consultar")
    print("[0] Sair")
    opcao = input("\nDigite a Opção desejada: ")

    if opcao == "0":
        break

    if opcao not in {"1", "2"}:
        print("Opção invalida.")
        continue # Volta ao menu sem pedir dados de cadastro.
    codigo = input("Código: ").strip()
    if not codigo:
        print("Preencha o codigo.")
        continue
    if opcao == "1":
        if codigo in clientes:
            print("Codigo já cadastrado.")
        else:
            nome = input("Nome: ").strip()
            if not nome:
                print("Preencha o nome.")
            else:
                clientes[codigo] = nome
                print("Cliente cadastrado.")
    elif opcao == "2":
        print(clientes.get(codigo, "Não encontrado"))
print("Fim do programa!")