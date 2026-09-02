entrada = input("Numeros: ")

numeros = [int(valor) for valor in entrada.split(",")]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)