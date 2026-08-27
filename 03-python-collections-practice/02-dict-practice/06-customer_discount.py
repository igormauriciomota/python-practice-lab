"""
Uma loja precisa calcular descontos diferentes para clientes novos, regulares e VIP, respeitando
também o valor da compra.
"""
valor_compra = float(input("Valor da compra: R$ ").replace(",","."))

tipo_cliente = input("Tipo [novo/regular/vip]: ").strip().lower()

# Validação impeditivas aparecem primeiro.
if valor_compra <= 0:
    print("O valor da compra deve ser positivo.")

elif tipo_cliente not in ("novo", "regular", "vip"):
    print("Tipo de cliente invalido.")

else:
    # Dentro de VIP existe uma segunda decisão.
    if tipo_cliente == "vip":
        if valor_compra >= 500:
            desconto = 15
        else:
            desconto = 10

    elif tipo_cliente == "regular":
        if valor_compra >= 1000:
            desconto = 8
        elif valor_compra >= 500:
            desconto = 5

    elif tipo_cliente == "novo" and valor_compra >= 300:
        desconto = 3

    valor_desconto = valor_compra * desconto / 100
    valor_final = valor_compra - valor_desconto

    print(f"Desconto: {desconto}%.")
    print(f"Valor descontado: R$ {valor_desconto:.2f}")
    print(f"Total: R$ {valor_final:.2f}")

