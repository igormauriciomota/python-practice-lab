import math

continuar = "s"

while continuar == "s":

    print("\n --- Calculadora com modulo meth ---")
    print("\n - Escolha a Opção desejada pra realizar o calculo! -")
    print("[1] Soma")
    print("[2] Subitração")
    print("[3] Divisão")
    print("[4] Mutiplicação")
    print("[5] Potencia")
    print("[6] Raiz Quadrada")
    print("[7] Fatorial")
    print("[8] MDC")

    opcao = input("Digite a Opção desejada de 1 a 8: ")

    #--- Soma de Dois Numeros
    if opcao == "1":
        numero1 = int(input("Digite o Primeiro Numero: "))
        numero2 = int(input("Digite o Segundo Numero: "))

        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")
    
    #--- Subtração
    elif opcao == "2":
        numero1 = int(input("Digite o Primeiro Numero: "))
        numero2 = int(input("Digite o Segundo Numero: "))

        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")
    
    #--- Divisão
    elif opcao == "3":
        numero1 = int(input("Digite o Primeiro Numero: "))
        numero2 = int(input("Digite o Primeiro Numero: "))

        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"{numero1} / {numero2} = {resultado}")
        else:
            print("Zero não e um numero valido")

    #--- Mutiplicação
    elif opcao == "4":
        numero1 = int(input("Digite o Primeiro Numero: "))
        numero2 = int(input("Digite o Segundo Numero: "))
        
        resultado = numero1 * numero2
        print(f"{numero1} x {numero2} = {resultado}")

    #--- Potencia
    elif opcao == "5":
        numero1 = int(input("Digite o Primeiro Numero: "))
        numero2 = int(input("Digite o Segundo Numero: "))

        resultado = math.pow(numero1, numero2)
        print(f"{numero1} x {numero2} = {resultado}")
    
    #--- Raiz Quadrada
    elif opcao == "6":
        numero1 = int(input("Digite o Primeiro Numero: "))

        if numero1 >= 0:
            resultado = math.sqrt(numero1)
            print(f"Raiz Quadrada de {numero1} é: {resultado}")

    #--- Fatorial
    elif opcao == "7":
        numero1 = int(input("Digite o Primeiro Numero: "))

        if numero1 >= 0:
            resultado = math.factorial(numero1)
            print(f"O Fatorial de {numero1} é: {resultado}")

    #--- MDC 
    elif opcao == "8":
        numero1 = int(input("Digite o Primeiro Numero: "))
        numero2 = int(input("Digite o Segundo Numero: "))

        resultado = math.gcd(numero1, numero2)
        print(f"O MDC de {numero1} e {numero2} é: {resultado}")

    else:
        print("Opção Invalida.")

    continuar = input("\nDeseja continuar[s/n]: ").lower()

print("Calculadora encerrada!")



    

  
 
