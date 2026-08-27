from validacoes import validar_nome, validar_idade, validar_email

continuar = "s"

while continuar == "s":

    nome = input("\nDigite o Nome: ").strip()
    idade = int(input("\nDigite a Idade: "))
    email = input("\nDigite o E-mail: ").strip()

    if not validar_nome(nome):
        print("\nNome Invalido.")

    elif not validar_idade(idade):
        print("\nIdade Invalida.")

    elif not validar_email(email):
        print("\nE-mail Invalido.")

    else:
        print("\nCadastro realizado com sucesso!")
        print(f"\nNome: {nome}")
        print(f"\nIdade: {idade}")
        print(f"\nE-mail: {email}")

        continuar = input("\nDeseja cadastrar outro usuario? (s/n): ").strip().lower()

print("\nPrograma finalizado.")