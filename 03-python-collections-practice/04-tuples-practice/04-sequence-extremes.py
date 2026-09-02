def calcular_extremos(numeros):
    menor = min(numeros)
    maior = max(numeros)
    amplitude = maior - menor
    return menor, maior, amplitude

valores = [10, 5, 8, 12, 3, 7]
menor, maior, amplitude = calcular_extremos(valores)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Amplitude: {amplitude}")
