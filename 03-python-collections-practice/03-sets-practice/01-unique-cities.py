""" 
cidades separadas por vírgula, normalize os nomes e exiba apenas as cidades
distintas em ordem alfabética
"""
entrada = input("Cidade separadas por virgula: ")
cidades = {
    cidade.strip().title()
    for cidade in entrada.split(",")
    if cidade.strip()
}

print("Cidade unicas:")
for cidade in sorted(cidades):
    print(f"- {cidade}")
