caminho_arquivo = "aula116.txt"


with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Atenção\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
