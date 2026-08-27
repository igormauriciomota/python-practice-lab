#
def validar_nome(nome):
    return len(nome) >= 3

def validar_idade(idade):
    return 18 <= idade <= 120

def validar_funcao(funcao):
    return len(funcao) >= 3

def validar_email(email):
    return "@" in email and "." in email

def email_ja_cadastrado(usuarios, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return True

    return False