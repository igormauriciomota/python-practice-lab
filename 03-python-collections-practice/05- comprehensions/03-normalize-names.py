# limpar, filtrar e transformar strings.
nomes_brutos = [" ana ", "", "BRUNO", "carla souza "]

nomes = [
    nome.strip().title()
    for nome in nomes_brutos
    if nome.strip() # filtra strings vazias

]

print(nomes)  # ['Ana', 'Bruno', 'Carla Souza']