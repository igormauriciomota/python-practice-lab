from time import monotonic

usuario = {}
tentativas = {"falhas": 0, "ate": 0.0}
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
    if senha != input("Confirme a senha."):
        print("As senhas não coincidem.")
        return usuario
    print("Cadastro realizado.")
    return {"username": nome, "senha": senha}


def login(usuario, logado, tentariva):
    if not usuario or logado:
        print("Cadastre-se primeiro ou encerre a sessão atual.")
        return logado
    if monotonic() < tentativas["ate"]:
        print("Bloqueio temporario. aguarde até 30 segundos.")
        return False
    nome = input("Username: ").strip()
    senha = input("Senha: ")

    correto = nome == usuario["username"]
    correto = correto and senha == usuario["senha"]

    print("Login realizado." if correto else "Dados incorretos.")
    if correto:
        tentativas.update(falhas=0, ate=0.0)
    else:
        tentativas["falhas"] += 1
        if tentativas["falhas"] >= 3:
            tentativas.update(falhas=0, ate=monotonic() + 30)
            print("Tres falhas: login bloqueado por 30 segundos.")
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
    print("Logout realizado." if logado else "Voce não está logado.")
    return False

def escolher_opcao(logado):
    print("\nStatus", "Logado" if logado else "Desconectado")
    print("\n1 Cadastro\n2 Login\n3 Senha\n4 Logout\n0 Sair")
    return int(input("Opção: "))

if __name__ == "__main__":
    # Importar este módulo não inicia o menu.
    while True:
        opcao = escolher_opcao(logado)
        if opcao == 1:
            usuario = cadastrar(usuario)
        elif opcao == 2:
            logado = login(usuario, logado, tentativas)
        elif opcao == 3:
            usuario = mudar_senha(usuario, logado)
        elif opcao == 4:
            logado = logout(logado)
        elif opcao == 0:
            break
        else:
            print("Opção Invalida.")    

