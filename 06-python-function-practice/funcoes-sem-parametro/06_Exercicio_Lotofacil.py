import random

def sortear_lotofacil():
    numeros = random.sample(range(1, 26), 15)
    numeros.sort()
    return numeros

resultado = sortear_lotofacil()

print("\n=== SORTEIO LOTOFACIL ===")

for numero in resultado:
    print(f"{numero:02d}", end=",")

print()