"""
1 - Criar uma funcao recursiva (que retorne ela mesma) para armazenar N termos dea sequencia de Fibonacci
em uma lista. N é definido pelo usuario. Ao encontrar os termos, imprimir a lista e finalizar a função.

 """

listaSF = []
stop = 0

def fibonacci(stop, a, b, aux):
    global listaSF # Utiliza uma variavel global dentro de uma função
    listaSF.append(a) # Adiciona os valores na lista 'listaSF'
    a, b = b, a + b # Acumula os valores para determinar os proximos termos é sempre 
    # a soma dos dois termos anteriores

    aux += 1
    if stop == aux:
        print(listaSF)
        return 0
    else:
        return fibonacci(stop, a, b, aux) # chama a propria função ate que stop == aux.

while stop < 1:
    stop = int(input('Digite a quantidade de termos: '))

fibonacci(stop, a=1, b=1, aux=0)