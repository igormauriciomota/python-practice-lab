def normalizar_perfil(dados):
    """
    Recebe um dicionário com os dados do usuário,
    valida as informações e devolve um novo dicionário normalizado.
    """
    # o campo "nome" é obrigatorio.
    # Usamos dados["nome"] porque queremos que o python gere
    # um KeyError caso essa chave não exixta no dicionario.
    nome = dados["nome"].strip().title()

    # Depois de remover os espaços, verificamos se o nome ficou vazio.
    if not nome:
        raise ValueError("Nome Obrigatorio.")

    # o campo "idade" támbem é obrigatorio.
    # Ele chega como string porque foi recebido por input().
    idade_texto = dados["idade"].strip()

    # tenta converter a idade para um numero inteiro
    # se o usuario digitar letras, int() gerara um valuerror.
    idade = int(idade_texto)

    # validação da faixa de idade.
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos.")

    # O campo "cidade" e opcional
    # get() devolve uma string vazia caso a chave não exixta.

    cidade = dados.get("cidade", "").strip().title()

    if not cidade:
        cidade = "Não informada"

    # copy() cria uma copia do dicionario original.
    # Isso evita modificar diretamente o dicionario
    perfil = dados.copy()

    # update() substitui os dados do dicionario original
    # já convertidos, validos e normalizados
    perfil.update({
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    })

    return perfil

try:
    # Criamos o dicionario que sera enviado para a função.
    dados_usuario = {
        "nome": input("Digite seu nome: "),
        "idade": input("Digite sua idade: "),
        "cidade": input("Digite sua cidade (opcional): ")
    }

    # Chamamos a função e armazenamos o dicionario retornado
    normalizar_perfil = normalizar_perfil(dados_usuario)

    # Acessamos os valores do dicionario pela respectivas chaves.
    print("\n--- PERFIL NORMALIZADO ---")
    print(f"Nome: {normalizar_perfil['nome']}")
    print(f"Idade: {normalizar_perfil['idade']}")
    print(f"Cidade: {normalizar_perfil['cidade']}")

except ValueError as erro:
    # Capitura erro de conversão e das validaçoes realizadas.
    print(f"Erro de validação: {erro}")
except KeyError as erro:
    # Capitura erro de conversão e das validaçoes realizadas.
    print(f"Campo obrigatorio ausente: {erro}")