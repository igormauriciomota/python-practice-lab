# Simulando abertura de recurso, consulta e encerramento garantido.
def consultar(registros, indice):
    recurso_aberto = True
    print("Recurso aberto")
    try:
        resultado = registros[indice]
    except IndexError:
        print("Posição inexixtente")
        return None
    else:
        # O else roda apenas quando o acesso funcionou.
        print("Consulta concluida")
        return resultado
    finally:
        # O encerramento acontece mesmo com return ou exceção.
        recurso_aberto = False
        print("Recurso fechado", not recurso_aberto)

print(consultar(["A", "B"], 1))
print(consultar(["A", "B"], 9))