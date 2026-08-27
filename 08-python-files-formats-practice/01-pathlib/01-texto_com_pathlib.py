from pathlib import Path

caminho = Path("laboratorio") / "anotacoes.txt"
caminho.parent.mkdir(parents=True, exist_ok=True)

conteudo = "Python exige pratica.\nRepetir melhora a fluencia.\n"

# writ_text abre, grava e fecha o arquivo.
caminho.write_text(conteudo, encoding="utf-8")

# read_text abre devolve todo o conteudo com string.
lido = caminho.read_text(encoding="utf-8")
print(lido)