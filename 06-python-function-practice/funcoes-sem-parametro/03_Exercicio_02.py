def mostrar_cabecalho():
    # O corpo ´s executa quando a função é chamada.
    print("=== CADASTRO DE PESSOAS ===")
    # sem return explicito, o resultado da chamada e None.

mostrar_cabecalho() # Parenteses executam a função.
nome = input("Nome: ").strip()
print(f"Pessoa: {nome}")