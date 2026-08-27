"""
Criar um dicionário com nome, idade e cidade informados pelo usuário.
Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída

"""

# Variaveis com input
nome = input("Nome: ").strip()
idade = int(input("Idade: "))
cidade = input("Cidade: ").strip()

pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

print("\n--- DaDOS ---")
for chave, valor in pessoa.items():
    print(f"{chave.title()}: {valor}")

