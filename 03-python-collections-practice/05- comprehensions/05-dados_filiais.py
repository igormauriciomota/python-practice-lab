# Lista que armazena vários lançamentos financeiros.
# Cada lançamento é representado por um dicionário.
lancamentos = [
    {"codigo": "L001", "filial": "BH", "valor": 1250.0, "status": "aprovado"},
    {"codigo": "L002", "filial": "SP", "valor": -80.0, "status": "aprovado"},
    {"codigo": "L003", "filial": "BH", "valor": 930.0, "status": "pendente"}
]

# Cria uma nova lista chamada "aprovados".
aprovados = [

    # Para cada lançamento válido, cria um novo dicionário.
    # O novo dicionário terá apenas código, filial e valor.
    {"codigo": item["codigo"], "filial": item["filial"], "valor": item["valor"]}

    # Percorre cada dicionário da lista "lancamentos".
    # Durante cada repetição, "item" representa um lançamento.
    for item in lancamentos

    # Adiciona o lançamento somente se:
    # 1. O status for "aprovado";
    # 2. O valor for maior que zero.
    if item["status"] == "aprovado" and item["valor"] > 0
]

# Exibe a nova lista contendo os lançamentos que passaram pelo filtro.
print(aprovados)
