"""
Volte à regra de cadastro único e grave o cadastro em usuario.json.
Armazene um hash em vez da senha original e recupere o cadastro ao
reiniciar.

generate_password_hash produz a representação para armazenamento e
check_password_hash verifica uma tentativa. Hash não é criptografia
reversível. O arquivo temporário é substituído após a gravação; isso evita
JSON parcialmente escrito, mas não resolve concorrência entre vários
processos.


"""
import json
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

ARQUIVO =   Path(__file__).with_name("usuario.json")

def carregar():
    if not ARQUIVO.exists():
        return {}
    dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))

    if not isinstance(dados, dict) or not all(
        isinstance(dados.get(k), str) for k in ("username", "senha")
        ):
        raise ValueError("Cadastro JSON com estrututa invalida.")
    return dados

def cadastrar(usuario):
    # Bloqueia um segundo cadastro antes de pedir novos dados.
    if usuario:
        print("Já existe cadastro.")
        return usuario
    nome = input("Username: ").strip()
    senha = input("Senha: ")
    if not nome or not senha.strip():
        print("Preencha todos os campos.")
        return usuario
    if senha != input("confirme a senha: "):
        print("As senhas não coincidem.")
        return usuario
    print("Cadastro realizado.")
    return {"username": nome, "senha": generate_password_hash(senha)}

def login(usuario, logado):
    if not usuario or logado:
        print("Cadastre-se primeiro ou encerre a sessão atual.")
        return logado
    nome = input("Username: ").strip()
    senha = input("Senha: ")
    # and exige que as duas comparações sejam verdadeiras.
    correto = nome == usuario["username"]
    correto = correto and check_password_hash(usuario["senha"], senha)
    print("Login realizado." if correto else "Dados incorretos.")
    return correto

def mudar_senha(usuario, logado):
    if not logado:
        print("Faça login primeiro.")
        return usuario
    if not check_password_hash(usuario["senha"], input("Senha atual: ")):
        print("Senha atual incorreta.")
        return usuario
    nova = input("Nova senha: ")
    if not nova.strip() or nova != input("Confirme: "):
        print("Senha vazia ou confirmação diferente.")
        return usuario
    # O dicionario e mutavel: esta atribuição altera seu conteudo.
    usuario["senha"] = generate_password_hash(nova)
    print("Senha alterada.")
    return usuario

def logout(logado):
    print("Logado realizado." if logado else "Voce não está logado.")
    return False


def escolher_opcao(logado):
    print("\nStatus:", "Logado" if logado else "Deslogado")
    print("\n1 Cadastro\n2 Login\n3 Senha\n4 Logout\n0 Sair")
    return int(input("Escolha a Opção: "))

def salvar(usuario):
    # Grava primeiro em um arquivo temporario.
    temporario = ARQUIVO.with_name(ARQUIVO.name + ".tmp")

    temporario.write_text(
        json.dumps(usuario, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )

    # Substitui o JSON após concluir a gravação.
    temporario.replace(ARQUIVO)



if __name__ == "__main__":
    # Falha explicita: não sobrescreve um arquivo invalido.
    try:
        usuario = carregar()
    except (OSError, ValueError) as erro:
        raise SystemExit(f"Não foi possivel ler o cadastro: {erro}")

    # Define o estado da sessão antes de usar o menu.
    logado = False

    # Importar este módulo não inicia o menu.
    while True:
        try:
            opcao = escolher_opcao(logado)
        except ValueError:
            print("Digite um numero valido.")
            continue

        try:
            if opcao == 1:
                usuario = cadastrar(usuario)

                if usuario: 
                    salvar(usuario)

            elif opcao == 2:
                # Atualiza o estado da sessão com o retorno do login
                logado = login(usuario, logado)

            elif opcao == 3:
                usuario = mudar_senha(usuario, logado)

                if logado:
                    salvar(usuario)

            elif opcao == 4:
                # Logout() retorna False
                logado = logout(logado)

            elif opcao == 0:
                print("Programa encerrado.")
                break

            else:
                print("Opção invalida. Escolha de 0 a 4.")

        except OSError as erro:
            raise SystemExit(
                f"Não foi possivel salvar os dados: {erro}"
            )





