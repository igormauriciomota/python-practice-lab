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

# Exemplo 03

def separar(lista):
    for num in lista:
        if num > 10:
            print(num, end='-')

listaCriada = [21, 3, 213, 543, 54, 65, 12, 0, 21, 24, 432.121, 532]
separar(listaCriada)

# Exemplo 04

# Nomear argumeots
def cidade(parte1, parte2):
    print(parte1 + ' ' + parte2)

cidade('São', 'Paulo')
cidade('Paulo', 'São')

cidade(parte1='São', parte2= 'Paulo')
cidade(parte2='Paulo', parte1='São')

# Parametro padrão

# Funçoes que não exige parametros
print()
input()

# Funçoes que exige parametro
def soma(num1, num2):
    print(num1 + num2)

soma(10, 18)

# Exemplo 05

# Funcao com parametro padrao (default)
# referencia pode ser o padrao de uma formula
# Obs: Parametro padrao de ve ser sempre o ultimo dos ragumentos na função.
# def medida(numero=60, referencia): SyntaxErro: Parameter without a default
def medida(numero, referencia=60): # Correto
    if numero > referencia:
        print(f'{numero} é maior que {referencia}')
    else:
        print(f'{numero} é menor que {referencia}')

medida(70)
medida(30)

"""

# Exemplo 06


