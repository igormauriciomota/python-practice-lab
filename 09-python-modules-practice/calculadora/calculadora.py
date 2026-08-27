# calculadora
def somar(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    if numero2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return numero1 / numero2

def calcular(numero1, numero2, operacao):
    #  A função decide qual operação deve ser executada.
    if operacao == "1":
        return somar(numero1, numero2)
    elif operacao == "2":
        return subtracao(numero1, numero2)
    elif operacao == "3":
        return multiplicacao(numero1, numero2)
    elif operacao == "4":
        return divisao(numero1, numero2)

    return "Operação invalida. "

