#

from entrada import ler_nome, ler_idade, ler_funcao, ler_email

from validacoes import (
    validar_nome,
    validar_idade,
    validar_funcao,
    validar_email,
    email_ja_cadastrado
)

from usuarios import (
    cadastrar_usuario,
    lista_usuarios,
    buscar_usuario
)

def mostrar_menu():
    print("\n=== CADASTRO DE USUÁRIOS ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("0 - Sair")

    return input("Escolha uma opção: ").strip()

def main():
    usuarios = []

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            nome = ler_nome()
            idade = ler_idade()
            funcao = ler_funcao()
            email = ler_email()

            if not validar_nome(nome):
                print("Nome inválido.")

            elif not validar_idade(idade):
                print("Idade inválida.")

            elif not validar_funcao(funcao):
                print("Função inválida.")

            elif not validar_email(email):
                print("Nome inválido.")  

            elif email_ja_cadastrado(usuarios, email):
                print("Este e-mail já esta cadastrado.")

            else:
                cadastrar_usuario(usuarios, nome, idade, funcao, email)
                print("Usuario cadastrado com Sucesso.")

        elif opcao == "2":
            lista_usuarios(usuarios)

        elif opcao == "3":
            email = ler_email()
            usuario = buscar_usuario(usuarios, email)

            if usuario:
                print("\nUsuario encontrado: ")
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Função: {usuario['funcao']}")
                print(f"E-mail: {usuario['email']}")
            else:
                print("Usuario não encontrado.")

        elif opcao == "0":
            print("\nPrograma finalizado.")
            break
        else:
            print("Operação Invalida.")


if __name__ == "__main__":
    main()            
                                     