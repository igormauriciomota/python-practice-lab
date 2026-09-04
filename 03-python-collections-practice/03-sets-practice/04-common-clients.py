mes_anterior = {"C01", "C02", "C03"}
mes_atual = {"C02", "C03", "C04"}

recorrentes = mes_anterior & mes_atual

print(f"Clientes recorrentes: {recorrentes}")
print(f"Quantidade: {len(recorrentes)}")