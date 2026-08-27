"""
Usar um dicionário em que o nome é a chave e o telefone é o valor.

Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída.

"""

agenda = {}

continuar = "s"

while continuar == "s":
    nome = input("Nome do contato: ").strip().capitalize()
    telefone = input("Telefone: ").strip()
    agenda[nome] = telefone
    continuar = input("Cadastrar outro? (s/n): ").strip().lower()

busca = input("\nNome para buscar: ").strip().title()
if busca in agenda:
    print(f"Telefone: {agenda[busca]}")
else:
    print("Contato não encontrado.")


    