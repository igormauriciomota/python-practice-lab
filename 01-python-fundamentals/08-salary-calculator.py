nome = input("Nome do Funcionario: ").strip().title()
horas = float(input("Horas trabalhadas: "))
valor_horas = float(input("Valor da hora: R$ "))

salario = horas * valor_horas

print(f"\n Funcionario: {nome}")
print(f"Salario: R$ {salario:,.2f}")
