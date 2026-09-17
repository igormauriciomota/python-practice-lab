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
usuario = {}
logado = False

def cadastrar(usuario):
    if usuario:
        print("Já exixte cadastro.")
        return usuario
    nome = input("Username: ").strip()
    senha = input("Senha: ")
    if not nome or not senha.strip():
        print("Preencha todos os campos.")
        return usuario
    if senha != input("Confime a senha: "):
        print("As senhas são coincidem.")
        return usuario
    print("Cadastro realizado.")
    return {"username": nome, "senha": senha}

def login(usuario, logado):
    if not usuario or logado:
        print("Cadastre-se primeiro ou encerre a sessão atual.")
        return logado
    nome = input("username: ").strip()
    senha = input("Senha: ")
    # and exige que as duas comparaçoes sejam verdadeiras
    correto = nome == usuario["username"]
    correto = correto and senha == usuario["senha"]
    print("Login realizado." if correto else "Dados incorretos.")
    return correto

def mudar_senha(usuario, logado):
    if not logado:
        print("Faça login primeiro.")
        return usuario
    if input("Senha atual: ") != usuario["senha"]:
        print("Senha atual incorreta.")
        return usuario
    nova = input("Nova senha: ")
    if not nova.strip() or nova != input("Confirme: "):
        print("Senha vazia ou confirmação diferente.")
        return usuario

    usuario["senha"] = nova
    print("Senha alterada.")
    return usuario

def logout(logado):
    print("Logout realizado." if logado else "Voce não esta logado.")
    return False

def escolher_opcao(logado):
    print("\nStatus:", "Logado" if logado else "Deslogado")
    print("\n1 Cadastro\n2 Login\n3 Senha\n4 Logout\n0 sair")
    return int(input("\nOpção desejada: "))

if __name__ == "__main__":
    while True:
        opcao = escolher_opcao(logado)
        if opcao == 1:
            usuario = cadastrar(usuario)
        elif opcao == 2:
            logado = login(usuario, logado)
        elif opcao == 3:
            usuario = mudar_senha(usuario, logado)
        elif opcao == 4:
            logado = logout(logado)
        elif opcao == 0:
            break
        else:
            print("Opção invalida.")
        
print("Fim do Programa.")

