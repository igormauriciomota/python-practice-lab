"""
 CRUD de produtos, entrada/saída de estoque e valor patrimonial.

"""

produtos = []
proximo_id = 1

while True:
    print("\n==== PRODUTOS E ESTOQUE ====")
    print("[1] Cadastro produto")
    print("[2] Lista produto")
    print("[3] Buscar produto")
    print("[4] Alterar preço")
    print("[5] Excluir produto")
    print("[6] Entrada de estoque")
    print("[7] Saida de estoque")
    print("[8] Valor total de estoque")
    print("[0] Sair")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        nome = input("Produtos: ").strip().title()
        categoria = input("Categoria: ").strip().title()
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade inicial: "))

        produtos.append({
            "id": proximo_id,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        })
        proximo_id += 1
        print("Produto cadastrado.")

    elif opcao == "2":
        for produto in produtos:
            print(
                f"ID: {produto['id']} | Produto: {produto['nome']} | Categoria: {produto['categoria']} | "
                f"Qtd: {produto['quantidade']} | Preço: R$ {produto['preco']:.2f}"
            )

    elif opcao == "3":
        termo = input("Nome ou parte do nome: ").strip().lower()
        encontrados = [p for p in produtos if termo in p["nome"].lower()]
        for produto in encontrados:
            print(produto)
        if not encontrados:
            print("Nenhum produto encontrado.")

    elif opcao == "4":
        id_busca = int(input("ID: "))
        for produto in produtos:
            if produto["id"] == id_busca:
                novo_preco = float(input("Novo preço: R$ "))
                if novo_preco > 0:
                    produto["preco"] = novo_preco
                    print("Preço atualizado.")
                break
        else:
            print("preço não encontrado.")

    elif opcao == "5":
        id_busca = int(input("ID: "))
        for produto in produtos:
            if produto["id"] == id_busca:
                produtos.remove(produto)
                print("Produto excluido. ")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "6":
         id_busca = int(input("ID: "))

         for produto in produtos:
            if produto["id"] == id_busca:
                entrada = int(input("Quantidade de entrada: "))

                if entrada > 0:
                    produto["quantidade"] += entrada
                    print("Entrada registrada.")
                break
         else:
             print("Produto não encontrado.")

    elif opcao == "7":
        id_busca = int(input("ID: "))

        for produto in produtos:
            if produto["id"] == id_busca:
                saida = int(input("Quantidade de saída: "))

                if 0 < saida <= produto["quantidade"]:
                    produto["quantidade"] -= saida
                    print("Saída registrada.")
                else:
                    print("Estoque insuficiente ou quantidade invalida.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "8":
        total = sum(p["preco"] * p["quantidade"] for p in produtos)
        print(f"Valor total do estoque: R$ {total:,.2f}")

    elif opcao == "0":
        break
    else:
        print("Opção Invalida")

print("Fim do Programa.")





