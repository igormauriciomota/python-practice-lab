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

def cadastro(usuario):
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



