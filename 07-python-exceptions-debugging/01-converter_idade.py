def converter_idade(texto):
    try:
        idade = int(texto)
    except ValueError as erro:

        raise ValueError("Idade deve ser um número inteiro.") from erro

    if not 0 <= idade <= 130:
        raise ValueError("Idade fora da faixa permitida.")
    
    return idade

texto_digitado = int(input("Digite sua idade: "))

try:
    idade = converter_idade(texto_digitado)
    print(f"Idade cadastrada: {idade} anos.")

except ValueError as erro:
        print("Erro:", erro)