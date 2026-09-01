codigos = input("Códigos: ").upper().split(",")
vistos = set()
duplicados = set()

for codigo in codigos:
    if codigo in vistos:
        duplicados.add(codigo)
    else:
        vistos.add(codigo)

print(f"Duplicados: {sorted(duplicados)}")