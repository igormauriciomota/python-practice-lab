"""
Cadastrar vários funcionários como dicionários dentro de uma lista.

Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída

"""

funcionarios = []

quantidade = int(input("Quantidade de funcionarios deseja cadastrar? "))

for i in range(quantidade):
    funcionario = {
        "nome": input("Nome: ").strip().capitalize(),
        "idade": int(input("Idade: ")),
        "funcao": input("Função: ").strip(),
        "salario": float(input("Salário: R$ "))
    }

    funcionarios.append(funcionario)


print("\n --- FUNCIONÁRIOS ---")
for funcionario in funcionarios:
    print(f"\n{funcionario['nome']} | {funcionario['idade']} | {funcionario['funcao']} | R$ {funcionario['salario']:,.2f}")






