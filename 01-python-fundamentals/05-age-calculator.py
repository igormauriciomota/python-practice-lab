nome = input("Digite seu nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

print(f"{nome}, voce tem aproximadamente {idade} anos. ")