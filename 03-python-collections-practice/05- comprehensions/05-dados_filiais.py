lancamentos = [
    {"codigo": "L001", "filial": "BH", "valor": 1250.0, "status": "aprovado"},
    {"codigo": "L002", "filial": "SP", "valor": -80.0, "status": "aprovado"},
    {"codigo": "L003", "filial": "BH", "valor": 930.0, "status": "pendente"}
]

aprovados = [
    {"codigo": item["codigo"], "filial": item["filial"], "valor": item["valor"]}
    for item in lancamentos
    if item["status"] == "aprovado" and item["valor"] > 0
]

print(aprovados)
