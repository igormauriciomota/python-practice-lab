# ["igor", "mota", "contábil"]
nome = input("Nome Completo: ").strip()
partes = nome.split() # O método .split() separa a string nos espaços e cria uma lista:

# Para cada parte existente em partes, pegue o caractere de índice 0 e 
# transforme-o em maiúsculo.
iniciais = [parte[0].upper() for parte in partes]
# ["I", "M", "C"] → "I-M-C"
resultado = "-".join(iniciais)

print(f"Iniciais: {resultado}")
