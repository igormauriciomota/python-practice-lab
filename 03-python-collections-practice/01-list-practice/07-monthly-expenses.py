#  Filtrar, ordenar e resumir valores.
despesas = []

for mes in range(1, 7):
    valor = float(input(f"Despesa {mes}: R$ "))
    despesas.append(valor)

total = sum(despesas)
media = total / len(despesas)
acima_media = sorted(
    [valor for valor in despesas if valor > media],
    reverse=True,
)

print(f"Total: R$ {total:.2f}")
print(f"Média: R$ {media:.2f}")
print(f"Acima da média: {acima_media}")
