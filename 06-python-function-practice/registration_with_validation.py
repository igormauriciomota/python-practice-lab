"""
Separar leitura, validação e cadastro em funções com responsabilidades diferentes.

Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída

"""
def ler_nome():
    return input("Nome: ").strip().lower().capitalize()

def ler_idade():
    return int(input("Idade: "))

def validar_nome(nome):
    return len(nome) >= 3

def validar_idade(idade):
    return 0 < idade <= 120

def cadastrar(lista, nome, idade):
    lista.append({"nome": nome, "idade": idade})


usuarios = []

nome = ler_nome()
idade = ler_idade()

if validar_nome(nome) and validar_idade(idade):
    cadastrar(usuarios, nome, idade)
    print("Cadastro realizado.")
else:
    print("Dados Invalidos.")

print(usuarios)




