grupo_a = {"Ana", "Beatriz", "Carlos", "Daniela"}
grupo_b = {"Elena", "Francisco", "Gloria", "Héctor"}

participantes = grupo_a | grupo_b

print(f"Participantes: {sorted(participantes)}")
print(f"Total único: {len(participantes)}")
