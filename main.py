import csv
# Lista onde ficam os livros
livros = []

# Carrega os livros que estão salvos no arquivo
def carregar_livros():
   try:
       arquivo = open("livros.csv", "r", newline="", encoding="utf-8")
       leitor = csv.DictReader(arquivo)
       for livro in leitor:
           livros.append(livro)
       arquivo.close()
   except FileNotFoundError:
       # Se o arquivo ainda não existir, ele será criado quando salvar
       pass
