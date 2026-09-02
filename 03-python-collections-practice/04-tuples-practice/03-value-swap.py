primeiro = input("Primeiro valor: ")
segundo = input("Segundo valor: ")

# o lado direito e empacotado antes do desempacotamento, 
# então a troca funciona mesmo que os valores sejam iguais
primeiro, segundo = segundo, primeiro

print(f"Primeiro: {primeiro}")
print(f"Segundo: {segundo}")    
