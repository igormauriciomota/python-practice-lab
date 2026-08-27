"""
Cadastro de vários usuários

"""
usuarios = []

quantidade = int(input("Quantos usuarios deseja cadastrar? "))

# 1 CADASTRO DOS USUÁRIOS

for i in range(quantidade):
    print(f"\nCadastro {i + 1}")

    usuario = {
        "nome": input("Nome: ").strip().lower(),
        "login": input("Login: ").strip().lower(),
        "senha": input("Senha: ").strip()
    }

    usuarios.append(usuario)

# 2 LOGIN
# Este codigo esta FORA do primeiro for
# portanto, só será executado depois que 
# todos os usuarios forem cadastrados.

print("\n--- LOGIN ---")
    
login = input("Login: ").strip().lower()
senha = input("Senha: ").strip()

encontrado = False

for usuario in usuarios:
    if usuario["login"] == login and usuario["senha"] == senha:
        print(f"Bem-vindo, {usuario['nome']}!")
        encontrado = True
        break

if not encontrado:
    print("Credenciais invalidas.")






