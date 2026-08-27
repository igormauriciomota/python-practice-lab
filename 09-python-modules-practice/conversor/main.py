import conversores

continuar = "s"

while continuar == "s":

    print("\n == Escolha a Opção desejada ==")
    print(" 1 - celsius para Fahrenheit")
    print(" 2 - Fahrenheit para Celcius")
    print(" 3 - Metros para centimetros")
    print(" 4 - Quilometros para metros")

    # Opção que deseja converter
    opcao = input("\nDifite a Opção: ")

    # Valor deseja converter
    valor = float(input("\nDigite o Valor: "))

    if opcao == "1":
        resultado = conversores.celsius_para_fahrenheit(valor)
        print(f"\nResultado: {resultado: .2f} °F")

    elif opcao == "2":
        resultado = conversores.fahrenheit_para_celsius(valor)
        print(f"\nResultado: {resultado: .2f} °C")

    elif opcao == "3":
        resultado = conversores.metros_para_centimetros(valor)
        print(f"\nResultado: {resultado: .2f} Centímetros")

    elif opcao == "4":
        resultado = conversores.quilometros_para_metros(valor)
        print(f"\nResultado: {resultado: .2f} Metros")

    else:
        print("\nOpção invalida!")

    continuar = input("\nDeseja continuar [s] Sim [n] Não: ").lower()

print("\nFim do Programa!")
        
        

    
        
