# Importa o modulo inteiro
from entrada import ler_numero, ler_operacao
from calculadora import calcular

def main():

    continuar = "s"

    while continuar == "s":

        print("\n === Calculadora Modular === ")

        numero1 = ler_numero("\nDigite o primeiro número: ")

        numero2 = ler_numero("\nDigite o segundo número: ")

        operacao = ler_operacao()

        resultado = calcular(numero1, numero2, operacao)

        print(f"Resultado: {resultado}")

        continuar = input("\n Deseja realizar outro cálculo? (s/n)").strip().lower()

    print("\nPrograma finalizado.")

if __name__ == "__main__":
    main()


