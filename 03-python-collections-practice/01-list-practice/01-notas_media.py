"""
Armazenar notas em uma lista, calcular a soma e a média e informar a maior e a menor nota.
Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída.

"""

notas = []

quantidade = int(input("Digite quantas notas deseja informar? "))

for i in range(quantidade):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)
    
# media das notas com sum e len
media = sum(notas) / len(notas)

print(f"\nNotas: {notas}")
print(f"Média: {media: .2f}")
print(f"Maior nota: {max(notas):.2f}")
print(f"Menor nota: {min(notas):.2f}")

