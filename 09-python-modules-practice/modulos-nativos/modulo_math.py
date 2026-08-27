import math

continuar = "s"

while continuar == "s":

    numero = int(input("\nDigite um número: "))

    if numero >= 0:
        raiz = math.sqrt(numero) # raiz quadrada
        print(f"Raiz quadrada: {raiz: .2f}")

    else:
        print("Não é possivel calcular a raiz real de número negativo.")

    print(f"Número arredondado para cima: {math.ceil(numero)}") # arredonda para cima
    print(f"Número arredondado para baixo: {math.floor(numero)}") # Arredonda para baixo
    print(f"Fatorial de {numero} é: {math.factorial(numero)}") # Fatorial
    print(f"Valor de PI: {math.pi}") # Valor do PI

    continuar = input("\nDeseja continuar se sim [s] se nao [n]: ").lower()

print("Fim do Programa!")