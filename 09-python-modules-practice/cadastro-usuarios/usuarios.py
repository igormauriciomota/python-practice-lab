#
def cadastrar_usuario(usuarios, nome, idade, funcao, email):
    usuario = {
        "nome": nome,
        "idade": idade,
        "funcao": funcao,
        "email": email
    }

    usuarios.append(usuario)

def lista_usuarios(usuarios):
    if not usuarios:
        print("\nNenhum usuário cadastrado.")

    print("\n=== USUARIOS CADASTRADOS ===")

    for indice, usuario in enumerate(usuarios, start=1):
        print(f"Usuário {indice}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Função: {usuario['funcao']}")
        print(f"E-mail: {usuario['email']}")


def buscar_usuario(usuarios, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return usuario

    return None