"""
Coordenadas XY formam um par de números que indicam a 
posição exata de um ponto em um plano bidimensional, 
usando um eixo horizontal (x) e um eixo vertical (y)

"""

x = float(input("Cordenada x: "))
y = float(input("Cordenada y: "))

ponto = (x, y)
eixo_x, eixo_y = ponto

print(f"x = {eixo_x}")
print(f"y = {eixo_y}")
print(f"Ponto: {ponto}")