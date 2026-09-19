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


