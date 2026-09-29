"""
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



