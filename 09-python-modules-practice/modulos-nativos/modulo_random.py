# random e um modulo gerar números pseudoaleatórios, realizar sorteios de elementos em sequências e embaralhar coleções de dados

import random

numero_secreto = random.randint(1, 10)

tentativa = int(input("Adivinhe um número entre 1 e 10: "))

if tentativa == numero_secreto:
    print("Voce acertou!")

else:
    print("Voce errou.")
    print(f"O numero correto era: {numero_secreto}.")

