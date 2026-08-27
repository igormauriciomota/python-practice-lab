"""
Permitir no máximo três tentativas de autenticação.
Observe os dados que entram pelo input(), como eles são convertidos, processados e exibidos. Tente 
identificar quais variáveis pertencem à entrada, à regra de negócio e à saída.

"""

login_cadastro = input("Cadastre seu login: ").strip().lower()
senha_cadastro = input("Cadastre sua senha: ").strip()

tentativas = 0

while tentativas < 3:
    login = input("Login: ").strip().lower()
    senha = input("Senha: ").strip()

    if login == login_cadastro and senha == senha_cadastro:
        print("Login realizado com sucesso.")
        break

    tentativas += 1
    print(f"Dados incorretos. restam {3 - tentativas} tentativas(s).")
else:
    print("Acesso bloqueado.")
