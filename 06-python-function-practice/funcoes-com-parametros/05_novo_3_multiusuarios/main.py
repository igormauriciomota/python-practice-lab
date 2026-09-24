# Aqui a regra evolui: varios cadastros, mas username únicos.
def cadastrar(usuarios):
    nome = input("Username: ").strip().casefold()
    if not nome or nome in usuarios:
        print("Nome vazio ou ja cadastrado.")
        return
    senha = input("Senha: ")
    if not senha.strip() or senha != input("Confirme: "):
        print("Senha inválida.")
        return
    usuarios[nome] = {"senha": senha, "nome": nome}
    print("Cadastro realizado.")

