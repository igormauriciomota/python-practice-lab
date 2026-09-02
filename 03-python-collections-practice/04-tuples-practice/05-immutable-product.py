catalogo = (
    ("PO1", "Teclado", 120.0),
    ("PO2", "Mouse", 80.0),
    ("PO3", "Monitor", 300.0),
    ("PO4", "Impresora", 150.0),
)

for codigo, nome, preco in catalogo:
    if preco > 130.0:
        print(f"{codigo}: {nome} - R${preco:.2f}")
