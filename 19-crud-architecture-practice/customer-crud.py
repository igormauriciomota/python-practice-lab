"""
CRUD, lista de dicionarios while, menu: cadastrar, listar, buscar, excluir e sair

"""
# Cria uma lista vazia.
# Ela será responsável por armazenar todos os clientes cadastrados.
#
# Depois dos cadastros, ela poderá ficar assim:
#
# clientes = [
#     {"nome": "Carlos", "email": "carlos@email.com"},
#     {"nome": "Maria", "email": "maria@email.com"}
# ]

clientes = []

# Inicia um loop infinito.
while True:

    print("\n--- ESCOLHA UMA OPÇÃO ---")
    print(" 1 - Cadastrar")
    print(" 2 - Listar")
    print(" 3 - Buscar")
    print(" 4 - Excluir")
    print(" 0 - Sair")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        cliente = {
            "nome": input("Nome: ").strip().capitalize(),
            "email": input("E-mail: ").strip()
        }

        clientes.append(cliente)
        print("Cliente cadastrado.")

    # Listar clientes cadastrados
    elif opcao == "2":
        # percorre a lista clientes retornando um par com o índice e o valor de cada elemento
        # start=1): Altera o início da contagem do loop para 1, ideal para exibir listas numeradas para usuários.
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. {cliente['nome']} - {cliente['email']}")

    # código faz a busca de um cliente pelo nome em uma lista
    elif opcao == "3":
        nome = input("Nome para buscar: ").strip().lower()
        encontrado = False
        for cliente in clientes:
            if cliente["nome"].lower() == nome:
                print(cliente)
                encontrado = True
                break

        if not encontrado:
            print("Cliente não encontrado.")

    # 
    elif opcao == "4":
        nome = input("Nome para excluir: ").strip().lower()
        for cliente in clientes:
            if cliente["nome"].lower() == nome:

                clientes.remove(cliente)
                print("Cliente Excluido.")
                break
        else:
            print("Cliente não encontrado.")

    elif opcao == "0":
        break
    else:
        print("Opção invalida.")

print("Fim do Programa")