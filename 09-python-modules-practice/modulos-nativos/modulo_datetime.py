"""
módulo "datetime" em Python é utilizado para criar, manipular, formatar e realizar cálculos com datas, horas e intervalos de tempo

"""
from datetime import datetime

#  armazena um objeto com a data e o horário atual do sistema na variável agora
agora = datetime.now()

print(f"Data e hora completa: {agora}")
print(f"Dia: {agora.day}")
print(f"Mes: {agora.month}")
print(f"Ano: {agora.year}")
print(f"Hora: {agora.hour}")
print(f"Minutos: {agora.minute}")

ano_nascimento = int(input("\nDigite seu ano de nascimento: "))

ano_atual = datetime.now().year

idade_proximada = ano_atual - ano_nascimento

print(f"Idade aproximada: {idade_proximada} anos")


