previstos = {"P1", "P2", "P3", "P4", "P5", "P35"}
entregues = {"P2", "P3", "P4", "P6", "P7"}

ausentes = previstos - entregues
inesperados = entregues - previstos

print(f"Ausentes: {sorted(ausentes)}")
print(f"Inesperados: {sorted(inesperados)}")
print(f"Quantidade de ausentes: {len(ausentes)}")
print(f"Quantidade de inesperados: {len(inesperados)}")
