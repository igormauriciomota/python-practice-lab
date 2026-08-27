nome = input("Nome: ").strip().title()
salario_base = float(input("Salario Base: R$ "))
horas_trabalhadas = float(input("Horas de Trabalho: "))

salario_hora = salario_base / horas_trabalhadas

print(f"{nome}, sua hora de trabalho é R$ {salario_hora:,.2f}")
