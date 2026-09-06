clientes = [
    {"id": 1, "nome": " ana silva ", "email": " ANA@EXEMPLO.COM "},
    {"id": 2, "nome": "bruno lima", "email": ""},
]

normalizados = [
    {
        "id": cliente["id"],
        "nome": cliente["nome"].strip().title(),
        "email": cliente["email"].strip().casefold(),
    }
    for cliente in clientes
    if cliente.get("email", "").strip()
]

print(normalizados)