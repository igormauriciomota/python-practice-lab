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

def login(usuario, atual):
    if atual is not None:
        print("Faça logout primeiro.")
        return atual
    if not usuario:
        print("Cadastre-se primeiro.")
        return None
    nome = input("Username: ").strip().casefold()
    senha = input("Senha: ")
    pessoa = usuario.get(nome)
    if pessoa and pessoa["senha"] == senha:
        print("Login realizado.")
        return nome
    print("Credenciais incorretas.")
    return None

def mudar_senha(usuarios, atual):
    if atual in None:
        print("Faça login.")
        return
    pessoa = usuarios[atual]
    if input("Senha atual: ") != pessoa["senha"]:
        print("Senha incorreta.")
        return
    nova = input("Nova senha: ")
    if nova.strip() and nova == input("Confirme: "):
        pessoa["Senha"] = nova
        print("Senha alterada.")
    else:
        print("Nova senha invalida.")

def editar_perfil(usuarios, atual):

    if atual is None:
        print("Faça login.")
        return
    nome = input("Nome de exibição: ").strip()
    if nome:
        usuarios[atual]["nome"] = nome
        print("Perfil atualizado:", nome)

def logout(atual):
    print("Logout ralizado." if atual else "voce não está logado.")
    return None

def menu():
    # Esta função não precisa receber dados para mostrar opções fixas.
    print("\n1 Cadastro\n2 Login\n3 Senha\n4 Logout\n5 Perfil")
    return int(input("Opção (0 sair): "))

if __name__ == "__main__":
    usuarrios, atual = {}, None
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar(usuarrios)
        elif opcao == 2:
            atual = login(usuarrios, atual)
        elif opcao == 3:
            mudar_senha(usuarrios, atual)
        elif opcao == 4:
            atual = logout(atual)
        elif opcao == 5:
            editar_perfil(usuarrios, atual)
        elif opcao == 0:
            break
        else:
            print("Opção invalida.")    