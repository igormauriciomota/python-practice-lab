valor = input("Informe o dado: ").strip()
while not valor:
    print("Entrada Invalida.")
    valor = input("Informe novamente: ").strip()
print("Dados válidos", valor)
