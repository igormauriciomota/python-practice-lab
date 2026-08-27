
# Entrada do nome
def ler_nome():
    return input("Digite o nome: ").strip()

# Entrada da Idade
def ler_idade():
    while True:
        try:
            idade = int(input("Digite a Idade: "))
            return idade
        except ValueError:
            print("Digite uma idade valida.")

# Entrada da Função
def ler_funcao():
    return input("Digite a Função: ")

# Entrada do E-mail
def ler_email():
    return input("Digite o e-mail: ").strip().lower()



