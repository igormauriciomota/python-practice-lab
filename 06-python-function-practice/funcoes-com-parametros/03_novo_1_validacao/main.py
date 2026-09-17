def validar_senha(senha, confirmacao):
    if not 8 <= len(senha) <= 128 or not senha.strip():
        return "Use de 8 a 128 caracteres e evite senha em branco."
    if senha != confirmacao:
        return "A confirmação está diferente."
    return ""

def ler_senha():
    senha = input("Nova senha(8 a 128 caracteres): ").strip()
    confirmacao = input("Confirme: ").strip()
    erro = validar_senha(senha, confirmacao)
    if erro:
        print(erro)
        return None
    return senha

usuariu = {}
logado = False

