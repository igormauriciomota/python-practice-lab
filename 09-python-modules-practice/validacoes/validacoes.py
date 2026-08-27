# validacoes faz parte do pacote de validações do sistema.
def validar_nome(nome):
    """
    Retorna True se o nome possuir pelo menos 3 caracteres.
    """
    if len(nome) >= 3:
        return True

    return False


def validar_idade(idade):
    """
    Retorna True se a idade for maior ou igual a 18.
    """
    if idade >= 18:
        return True

    return False

def validar_email(email):
    """
    Retorna True se o email possuir o caractere "@".
    """
    if "@" in email and "." in email:
        return True

    return False
