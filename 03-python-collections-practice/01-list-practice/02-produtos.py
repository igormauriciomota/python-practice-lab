produtos = []

quantidade = int(input("Quantos produtos deseja cadastra? "))

for i in range(quantidade):
    produto = input(f"Digite o {i + 1}° produto: ").strip()
    produtos.append(produto)

print("\n--- LISTA DE COMPRAS ---")
for produto in produtos:
    print(f"-{produto}")

print(f"\nTotal de itens: {len(produtos)}")



