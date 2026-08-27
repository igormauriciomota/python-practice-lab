produto = input("Produto: ")
preco = float(input("Preço: R$ "))
quantidade = int(input("Quantidade: "))

total = preco * quantidade

print(f"\nProduto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {total:.2f}")
