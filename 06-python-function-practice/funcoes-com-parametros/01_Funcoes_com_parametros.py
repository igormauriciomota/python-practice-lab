"""
- Funçoes com parametro:

- recebem dados e variaveis sao chamados de (argumentos) para utilizar em processos internos

- Podem ter inumeros parametros (separado por virgula)

ex:

- São funçoes que recebem parametros

sum() -
max() -
min() -
index() -
print() -
input() -

# Exemplo 1
# def funcao(argumento):
def imparPar(numero):
    # parametro
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

digitar = int(input("Digite um numero: "))

imparPar(digitar)

# Exemplo 2

# Mine calculadora

def soma(num1, num2):
    print(num1 + num2)

def subitracao(num1, num2):
    print(num1 - num2)

def multiplica(num1, num2):
    print(num1 * num2)

def divisao(num1, num2):
    print(num1 / num2)

def potencia(num1, num2):
    print(num1 ** num2)

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma(n1, n2)
subitracao(n1, n2)
multiplica(n1, n2)
divisao(n1, n2)
potencia(n1, n2)

"""

