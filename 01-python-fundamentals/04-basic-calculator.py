numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("\n---- RESULTADOS ----")
print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao:.2f}")
print(f"{numero1} x {numero2} = {multiplicacao:.2f}")
print(f"{numero1} / {numero2} = {divisao}")