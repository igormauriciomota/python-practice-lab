"""
Exercicio soma as notas dos alunos em diversas atividades escolares, e realiza a soma, media e statuas do aluno
"""
nome = input("Nome do aluno: ").strip().title()
prova = float(input("Nota da prova: "))
exercicio = float(input("Nota do exercicio: "))
trabalho = float(input("Nota do trabalho: "))
caderno = float(input("Nota de caderno: "))

total = prova + exercicio + trabalho + caderno
media = total / 4

print(f"\n{nome}, sua nota total foi de {total:.2f}, sua media e de {media:.2f}")

if media >= 7:
    print("Aprovado Parabens!")
elif media >= 5:
    print("Voce esta de Recuperação!")
else:
    print("Reprovado!")