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

