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


