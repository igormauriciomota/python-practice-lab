"""
1 - Criar uma funcao recursiva (que retorne ela mesma) para armazenar N termos dea sequencia de Fibonacci
em uma lista. N é definido pelo usuario. Ao encontrar os termos, imprimir a lista e finalizar a função.

2 - Criar 5 funçoes: uma para um cadastro, outra para realizar o login, outra para mudar a senha,
outra para realizar logout e ainda uma para definir qual opção o usuario deseja escolher.
Utilize um loop while para sari do sistema apenas se o usuario desejar (Criar a opsão 'sair')
Atente-se as regras:

 - Só é possivel realizar um cadastro se não houver nehum anterior.
 - Só é possivel realizar login se houver um cadastro. 
 - Só é possivel realizar login se usuario informar corretamente username e senha.
 - Só é possivel realizar a senha se o usuario estiver logado.
 - Só é possivel realizar a senha se o usuario informar corretamente a senha atual.
 - Só é possivel realizar logout se o usuario estiver logado
 
 """

# 1

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