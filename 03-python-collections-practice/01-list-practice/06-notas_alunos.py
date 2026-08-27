def resulmir_nota(notas):
    # Calcula um resumo estatico das notas

    # inpede o calculo com uma lista vazia.
    if not notas:
        raise ValueError("Informe ao menos uma nota.")

    # Verifica se existe alguma nota fora do intervalo permitido
            # nota menor 0 ou nota maior 10, 
    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem ficar entre 0 e 10.")

    return {
        "quantidade": len(notas),
        "media": sum(notas) / len(notas),
        "menor": min(notas),
        "maior": max(notas)
    }

notas = []


# Pergunta quantas notas o usuario deseja cadastrar.

while True:
    try:
        quantidade = int(input("Quantas notas deseja cadastrar? "))

        if quantidade <= 0:
            print("Informe uma quantidade maior que zero.")
            continue

        break

    except ValueError:
        print("Digite uma quantidade inteira válida.")

# o rage() repete o cadastro conforme a quantidade informada.
for numero in range(1, quantidade + 1):

    while True:
        try:
            texto = input(f"Digite a {numero}ª nota: ").replace(",",".")
            nota = float(texto)

            if nota < 0 or nota > 10:
                print("A nota deve ficar entre 0 e 10.")
                continue

            notas.append(nota)
            break

        except ValueError:
            print("Digite uma nota numerica valida.")

# A funçao devolve um dicionario com os resultados.
resumo = resulmir_nota(notas)

print("\n --- RESUMO DAS NOTAS ---")
print(f"Notas cadastradas: {notas}")
print(f"Quantidade: {resumo['quantidade']}")
print(f"Média: {resumo['media']:.2f}")
print(f"Menor nota: {resumo['menor']:.2f}")
print(f"Maior nota: {resumo['maior']:.2f}")
