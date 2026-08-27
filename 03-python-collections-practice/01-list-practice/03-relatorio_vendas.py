"""
Cadastrar vendedores e suas vendas e calcular total, média e melhor venda usando loops.
Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída.

"""

vendas = []

quantidade = int(input("Quantos vendedores deseja cadastrar? "))

for i in range(quantidade):

    print(f" {i + 1}ª Vendedor")
    nome = input("Vendedor: ").strip().capitalize()
    valor = float(input("Valor vendido: R$ "))
    vendas.append({"nome": nome, "valor": valor})

total = 0
for venda in vendas:
    total += venda["valor"]

media = total / len(vendas)
melhor = max(vendas, key=lambda item: item["valor"])

print(f"Total: R$ {total:,.2f}")
print(f"Média: R$ {media:,.2f}")
print(f"Melhor vendedor: {melhor['nome']} - R$ {melhor['valor']:,.2f}")

