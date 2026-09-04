previstos = {"P1", "P2", "P3"}
entregues = {"P2", "P3", "P4"}

ausentes = previstos - entregues
inesperados = entregues - previstos

print(f"Ausentes: {sorted(ausentes)}")
print(f"Inesperados: {sorted(inesperados)}")
print(f"Quantidade de ausentes: {len(ausentes)}")
print(f"Quantidade de inesperados: {len(inesperados)}")
