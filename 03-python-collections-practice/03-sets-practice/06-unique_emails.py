# Cria dois conjuntos vazios:
# unicos guardará todos os e-mails sem duplicação.
# repetidos guardará apenas os e-mails digitados mais de uma vez.
unicos, repetidos = set(), set()

quantidade = int(input("Quantidade de e-mail deseja cadastrar?"))
# Repete o cadastro de acordo com a quantidade informada.
# O caractere "_" representa uma variável que não será utilizada.
for _ in range(quantidade):
    # Solicita o e-mail.
    # strip() remove espaços no início e no final.
    # casefold() transforma as letras para minúsculas de maneira abrangente.
    email = input("E-mail: ").strip().casefold()

     # Verifica se o e-mail já está no conjunto unicos.
    if email in unicos:


        # Se já estiver, significa que foi digitado novamente.
        # O e-mail é então adicionado ao conjunto repetidos.
        repetidos.add(email)

    # Adiciona o e-mail ao conjunto de e-mails únicos.
    # Se ele já existir, o set não cria outra cópia.
    unicos.add(email)

# sorted() organiza os e-mails em ordem alfabética.
print("ùnicos:", sorted(unicos))

# Exibe somente os endereços digitados mais de uma vez.
print("Repetidos:", sorted(repetidos))
