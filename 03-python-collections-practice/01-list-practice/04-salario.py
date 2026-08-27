"""
Cadastrar salários em uma lista e calcular total da folha, média salarial e salários acima da média.
Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída

"""

salarios = []

quantidade = int(input("Quantos salarios deseja cadastrar? "))

for i in range(quantidade):
    salario = float(input(f"Salario do funcionario {i + 1}: R$ "))
    # append adiciona salario na lista salarios
    salarios.append(salario)

# Total soma de todos os salarios
total = sum(salarios)
media = total / len(salarios)

print(f"\nTotal da folha: R$ {total:.5f}")
print(f"Media salarial: R$ {media:.5f}")

print(f"\nSalário acima da media:")
for salario in salarios:
    if salario > media:
        print(f"R$ {salario:.5f}")

