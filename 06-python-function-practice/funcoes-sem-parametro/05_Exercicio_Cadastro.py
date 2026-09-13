"""

2 - Criar 5 funçoes: uma para um cadastro, outra para realizar o login, outra para mudar a senha,
outra para realizar logout e ainda uma para definir qual opção o usuario deseja escolher.
Utilize um loop while para sari do sistema apenas se o usuario desejar (Criar a opsão 'sair')
Atente-se as regras:

 - Só é possivel realizar um cadastro se não houver nehum anterior.
 - Só é possivel realizar login se houver um cadastro. 
 - Só é possivel realizar login se usuario informar corretamente username e senha.
 - Só é possivel realizar a senha se o usuario estiver logado.
 - Só é possivel realizar a senha se o usuario informar corretamente a senha atual.
 - Só é possivel realizar logout se o usuario estiver logado

"""

# Cadastro unico em memoria: os dados some ao encerrar
usuario = {}
logado = False

def cadastrar():
    global usuario
    if usuario:
        print("Já exixte cadastrado.")
        return
    nome = input("Username: ").strip()
    senha = input("Senha: ")
    if not nome or not senha.strip():
        print("Preencha todos os campos.")
        return
    if senha != input("Confirmar senha: "):
        print("As senhas não coincidem.")
        return
    print("Cadastro realizado.")
    usuario = {"username": nome, "senha": senha}

def login():
    global logado
    if not usuario or logado:
        print("Cadastre-se primeiro ou encerre a sessão atual.")
        return
    nome = input("Username: ").strip()
    senha = input("Senha: ")
    # and exige que as duas comparaçoes sejam verdadeiras.
    correto = nome == usuario["username"]
    correto = correto and senha == usuario["senha"]
    print("Logo realizado." if correto else "Dados incorretos.")
    logado = correto

def mudar_senha():
    if not logado:
        print("Faça login primeiro.")
        return
    if input("Senha atual: ") != usuario["senha"]:
        print("Senha atual incorreta.")
        return
    nova = input("Nova senha: ")
    if not nova.strip() or nova != input("Confirme: "):
        print("Senha vazia ou confimação diferente.")
        return
    # o dicionario e mutavel: esta atribuição altera seu conteudo
    usuario["senha"] = nova
    print("Senha alterada.")
    return

def logout():
    global logado
    print("Logout realizado." if logado else "Voce não esta logado.")
    logado = False

def escolher_opcao():
    print("\nStatus:", "Logado" if logado else "Deslogado")
    print("\n----- Escolha a Opção desejada -----")
    print("\n1 Cadastro\n2 Login\n3 Senha\n4 Logout\n0 Sair do Programa")
    return int(input("Escolha a Opção: "))

if __name__ == "__main__":
    while True:
        opcao = escolher_opcao()
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            login()
        elif opcao == 3:
            mudar_senha()
        elif opcao == 4:
            logout()
        elif opcao == 0:
            break
        else:
            print("Opção invalida.")

print("Fim do Programa.")
