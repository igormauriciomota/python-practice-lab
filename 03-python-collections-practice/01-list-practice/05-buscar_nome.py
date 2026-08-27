
clientes = []

quantidade = int(input("Digite a quantidade que deseja cadastrar: "))

for i in range(quantidade):
    print(f"Cliente {i + 1}º")

    nome = input("Nome: ").strip().title()

    clientes.append(nome)

busca = input("Nome para buscar: ").strip().title()


if busca in clientes:
    print(f"Encontrado: {busca}")
else:
    print("Nome não encontrado!")



