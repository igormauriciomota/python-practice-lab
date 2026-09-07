"""
CRUD de produtos com funçoes, contendo opçoes de cadastro, buscar, listar, alterar e excluir.
"""
#  Cadastra um novo produto.
def cadastrar(produtos, proximo_id):
    nome = input("Nome: ").strip().title()
    preco = float(input("Preço: R$ "))
    produtos.append({"id": proximo_id, "nome": nome, "preco": preco})
    return proximo_id + 1

 # Busca e retorna o produto.
def buscar_por_id(produtos, produto_id):

    # Percorre os produtos cadastrados
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
              
# Exibe os produtos.
def listar(produtos):

    # Verifica primeiro se a lista esta vazia
    if not produtos:
        print("Lista Vazia.")
        return

    for produto in produtos:
        print(produto)

# Altera o preço atraves do ID
def alterar_preco(produtos):

    produto_id = int(input("ID: "))
    produto = buscar_por_id(produtos, produto_id)

    if produto:
        produto["preco"] = float(input("Novo preço: R$ "))

# Deleta o produto atravez do ID
def excluir(produtos):
    produto_id = int(input("ID: "))
    produto = buscar_por_id(produtos, produto_id)
    if produto:
        produtos.remove(produto)
        print("Produto removido com sucesso!")
        return
    else:
        print("Produto não encontrado.")


def main():
    produtos = []
    proximo_id = 1

    while True:
        print("\n === Escolha uma opção ===")
        print("[1] Cadastrar")
        print("[2] Listar")
        print("[3] Alterar")
        print("[4] Excluir")
        print("[0] Sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            proximo_id = cadastrar(produtos, proximo_id)
        elif opcao == "2":
            listar(produtos)
        elif opcao == "3":
            alterar_preco(produtos)
        elif opcao == "4":
            excluir(produtos)
        elif opcao == "0":
            print("Fim do Programa.")
            break

if __name__ == "__main__":
    main()




