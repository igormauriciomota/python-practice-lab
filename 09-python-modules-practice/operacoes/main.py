# Importa somente a função soma

from operacoes import soma

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("\nDigite o segundo numero: "))

resultado = soma(numero1, numero2)
print(f"\nA soma de {numero1} + {numero2} = {resultado}")

