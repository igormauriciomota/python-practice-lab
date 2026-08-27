def processar(valor):
    """
    Valida e formata o valor recebido.
    """

    # Verifica se o valor é None.
    if valor is None:
        raise ValueError("Valor obrigatório.")

    # Converte para string e remove espaços externos.
    valor_formatado = str(valor).strip()

    # Verifica se ficou vazio depois da remoção dos espaços.
    if not valor_formatado:
        raise ValueError("O valor não pode ficar vazio.")

    # Coloca a primeira letra de cada palavra em maiúscula.
    return valor_formatado.title()


entrada = input("Entrada: ")

try:
    resultado = processar(entrada)
    print("Valor processado:", resultado)

except ValueError as erro:
    print("Erro:", erro)