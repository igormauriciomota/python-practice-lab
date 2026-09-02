"""
Criar um set comprehension.
Extraia as iniciais distintas de uma lista de produtos, em maiúsculas
"""
produtos = ['arroz', 'feijão', 'macarrão', 'carne', 'frango', 'peixe']

iniciais = {produto[0].upper() for produto in produtos if produto}  # Adiciona uma verificação para garantir que o produto não seja uma string vazia 

print(sorted(iniciais))  # ['A', 'C', 'F', 'M', 'P']
