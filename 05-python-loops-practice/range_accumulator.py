# O programa percorre um intervalo configurável, mostra cada número e calcula quantidade, soma e média.
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

if passo == 0:
    print("O passo não pode ser zero.")
else:
    total = 0
    quantidade = 0

    # Ajuda o limite para tentar incluir o valor final.
    limite = fim + 1 if passo > 0 else fim - 1

    # range() gera os números sem criar manualmente uma lista.
    for numero in range(inicio, limite, passo):
        print(numero)
        total += numero
        quantidade += 1

    if quantidade > 0:
        media = total / quantidade
        print(f"Quantidade: {quantidade}")
        print(f"Soma: {total}")
        print(f"Média: {media:.2f}")
    else:
        print("O intervalo não produziu números.")