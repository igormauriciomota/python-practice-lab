# strip() remove espaços externos; title() padroniza cada palavra.
nome = input("Digite seu nome completo: ").strip().title()

if nome:
    print(f"Olá. {nome}!")
else:
    print("O nome não pode ficar vazio.")
    