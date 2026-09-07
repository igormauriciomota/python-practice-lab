def mostrar_cabecalho():
    # O corpo ´s executa quando a função é chamada.
    print("=== CADASTRO DE PESSOAS ===")
    # sem return explicito, o resultado da chamada e None.

mostrar_cabecalho() # Parenteses executam a função.
nome = input("Nome: ").strip()
print(f"Pessoa: {nome}")



def saudacao():
    # input() recebe o nome strip() remove espaços da ponta, title() adiciona maiuscula nas palavras iniciais
    nome = input("Digite seu nome: ").strip().title()
    # A funçao mostra a mensagem direta na tela
    print(f"Olá, {nome}! Bem-vindo aos estudos Python!")

saudacao()

def mostrar_soma():
    # replace() troca a vírgula por ponto antes da conversão.
    primeiro = float(input("Digite o primeiro numero: ").replace(",","."))
    segundo = float(input("Digite o segundo numero: ").replace(",","."))

    # Guarda o resultado da soma em uma variável local.
    total = primeiro + segundo

    # :.2f apresenta o número com duas casas decimais.
    print(f"Resultado da soma: {total:.2f}")

mostrar_soma()

