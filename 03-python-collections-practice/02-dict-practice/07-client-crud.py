clientes = {}

while True:
    print("---- Menu de Clientes ----")
    print("[1] Criar cliente")
    print("[2] Listar clientes")
    print("[3] Atualizar cliente")
    print("[4] Excluir cliente")
    print("[0] Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        codigo = input("Código do cliente: ").strip()
        if codigo in clientes:
            print("Cliente ja cadastrado.")
            continue
        clientes[codigo] = {
            "nome": input("Nome: ").strip().title(),
            "email": input("Email: ").strip().lower(),
            "telefone": input("Telefone: ").strip()
        }

    elif opcao == 2:
        for codigo, dados in clientes.items():
            print(codigo, dados)
    elif opcao == 3:
        codigo = input("Código do cliente: ").strip()
        if codigo in clientes:
            clientes[codigo]["email"] = input("Novo Email: ").strip().lower()
            clientes[codigo]["telefone"] = input("Novo Telefone: ").strip()
        else:
            print("Cliente não encontrado.")
    elif opcao == 4:
        codigo = input("Codigo do cliente: ").strip()
        removido = clientes.pop(codigo, None)
        print("Excluido" if removido else "Cliente não encontrado.")
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")
print("Programa encerrado.")