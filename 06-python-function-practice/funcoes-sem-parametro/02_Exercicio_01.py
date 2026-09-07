"""
Foi realizado uma pesquisa de algumas caracteristicas e gostos de quatro habitantes incluido:
nome, sexo, esporte favorito (Natação, Futebol, Volei, Tenis) e idade. com esses dados faça:

- funçao que armazene os dados em uma lista. dica: use dicionarios dentro da lista.
- Calcule a idade media de homens que gostam de natação, caso nao haja homens que gostam de natação 
chame uma função e imprima um aviso de que não ha homens que goste de natação.

"""

# criar uma função cadastro
def cadastro():
    # cria a lista do enunciado
    list = []
    # cria uma quantidade para o range()
    quantidade = int(input("Quantos cadastro deseja fazer? "))
    # criar um for
    for i in range(quantidade):
        dicionario = dict(
            nome = input('Digite seu nome: ').strip().title(), 
            sexo = input('Digite M para masculino e F para feminino: ').lower(), 
            esporte = input('Escolha seu esporte favoritoentre Natação, Futebol, Volei, Tenis:  ').strip().lower(), 
            idade = int(input('digite sua idade: '))
        )
        list.append(dicionario)
    return list

lista = cadastro()
cont = 0
soma = 0
print(lista)

