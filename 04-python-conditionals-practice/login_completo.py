""" 
Perceba a sequência:

1-Primeiro verifica o usuário;
2-Depois solicita a senha;
3-Se a senha estiver correta, verifica o perfil;
4-Conforme o perfil, libera diferentes áreas.

Esse é um exemplo de condições dependentes.

"""

usuario = input("Digite o usuario: ").strip().lower()

if usuario == "admin":
    print("Usuario encontrado")

    senha = input("Digite sua senha: ")

    if senha == "1234":
        print("Login realizado com sucesso.")

        perfil = input("Digite o perfil: ").strip().lower()

        if perfil == "financeiro":
            print("Acesso ao módulo financeiro.")

        if perfil == "compras":
            print("Acesso ao módulo de compras.")