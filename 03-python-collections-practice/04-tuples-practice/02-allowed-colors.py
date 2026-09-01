"""
Usar tupla como conjunto fixo de opções.
Enunciado: Defina uma tupla de cores válidas e verifique se a escolha do usuário está nela.
"""
cores_permitidas = ("azul", "verde", "vermelho")
escolha = input("Escolha uma cor: ").strip().lower()

if escolha in cores_permitidas:
    print("cor permitida.")
else:
    print(f"Use uma destas cores: {', '.join(cores_permitidas)}")
