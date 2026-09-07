"""
- O que são funçoes?

- São blocos de codigo que irao executar uma tarefa especifica, podendo se reutilizavel.
- tem por papel organizar diminuir seu programa e facilitar alteraçoes e gerenciamentos.
- são declaradas após os comentarios iniciais e imports(se houver)
- já estudamos algumas funçoes nativas:
a) print()
b) input()
c) type()

# como declarar?
def nome_funcao():
    Processo

nome_funcao()

---------------------------------------------------

ex 01:

def teste_frase():
    print("Estou na funcao")

teste_frase() # executa teste_frase

---------------------------------------------------

ex 02:

def teste_frase():
    print("Estou na funcao")

# pode ser executada dentro de um for
for i in range(0,10):
    teste_frase() # executa teste_frase

----------------------------------------------------

ex 03: variaveis do tipo função, DEVE SER SEM PARENTESES
obs: se usar => frase = teste_frase() sera do tipo None:

def teste_frase():
    print("Estou na funcao")

# Variavel
frase = teste_frase
print(type(frase))
frase()

--------//---------------------------//-------------

- Há duas classificaçoes em funçoes:

1) Função com retorno e sem retorno:
- O retorno é utilizado para justamente retornar alguma operação/variavel de dentro da funão.
- Para isso utiliza-se a palavra > return
- Podemos ter mais de um return na funçao

Ex 01: Função sem retorno

# global fora da funçao
def operacao():
    contador = 60 # Isso é uma variavel local ou global?? local dentro da função
    contador += 2
    print(f"Contador = {contador}")

# operacao()
print(operacao()) # Quando não há return dentro da função retorna None

Ex 02: Função com retorno

# global fora da funçao
def operacao():
    contador = 60 # Isso é uma variavel local ou global?? local dentro da função
    contador += 2
    print(f"Contador = {contador}")
    return contador

# operacao()
print(operacao()) # Quando não há return dentro da função retorna None

Obs: Assim que a funçao reconhece a palavra > return, ela finaliza aoutomaticamente

def operacao():
    contador = 59
    if contador < 60:
        contador += 2
        return contador
    print(f"Contador = {contador}")
    return contador


print(operacao()) 

---------------------//---------------------------//--------------------------

2) Funçoes recursivas e não recursivas:

O que e recursividade?
 - Aquilo que se repete indefinidamente. em programação uma função 
 recursiva e aquela que retorna ela mesma.

 ----------------
 1º Função nao recursiva (Não retorna ela mesma, ela e executada apenas 1 vez)

def celcius_kelvin():
    celsius = int(input("Digite o valor em celcius: "))
    kelvin = celsius + 273
    return kelvin

print(celcius_kelvin())

 ----------------
 2º Função recursiva > LEMBRE-SE SEMPRE DE UMA DONDIÇAO DE PARADA NA RECURSIVIDADE.
 CASO CONTRARIO, CAIRA EM UM LOOP INFINITO.

 def celcius_kelvin():
    celsius = int(input("Digite o valor em celcius: "))
    kelvin = celsius + 273
    print(f"{kelvin}")
    # opção de parada
    opcao = input("Deseja sais [s/n]: ").lower()
    if opcao == "s":
        return 'Programa encerrado.'
    else:
        return celcius_kelvin() # Aqui usa o parenteses/ retornando para ela mesma

print(celcius_kelvin())

3° LOOP INFINITO.

def celcius_kelvin():
    celsius = int(input("Digite o valor em celcius: "))
    kelvin = celsius + 273
    print(f"{kelvin}")
    return celcius_kelvin() # Aqui usa o parenteses/ retornando para ela mesma

print(celcius_kelvin())

Vantagens de usar recursão: Tornar o codigo mais limpo e gera sequencia facilmente
Desvantagens de usar recursao: A logica pode ser mais complexa e tambem usar mais (memorias)

"""
def celcius_kelvin():
    celsius = int(input("Digite o valor em celcius: "))
    kelvin = celsius + 273
    print(f"{kelvin}")
    # opção de parada
    opcao = input("Deseja sais [s/n]: ").lower()
    if opcao == "s":
        return 'Programa encerrado.'
    else:
        return celcius_kelvin() # Aqui usa o parenteses/ retornando para ela mesma

print(celcius_kelvin())