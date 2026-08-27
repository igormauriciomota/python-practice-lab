"""
except especificos, ZeroDivisionError e TypeError

"""
def dividir(a, b):
    try:
        numerador = float(a)
        denominador = float(b)
        return numerador / denominador
    except ValueError:
        return {"OK": False, "erro": "User valores numericos."}
    except ZeroDivisionError:
        return {"OK": False, "erro": "Divisão por zero não e permitida."}
    except TypeError:
        return {"OK": False, "erro": "Tipo de entrada incompativel."}

a = input("Digite o primeiro numero: ")
b = input("Digite o segundo numero: ")

resultado = dividir(a, b)

print(f"{a} dividido {b} = {resultado}")


