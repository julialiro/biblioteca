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
# Salva os livros no arquivo livros.csv
def salvar_livros():
   arquivo = open("livros.csv", "w", newline="", encoding="utf-8")
   escritor = csv.writer(arquivo)
   # Cria o cabeçalho do arquivo
   escritor.writerow(["titulo", "autor", "ano", "codigo", "status"])
   # Salva todos os livros
   for livro in livros:
       escritor.writerow([
           livro["titulo"],
           livro["autor"],
           livro["ano"],
           livro["codigo"],
           livro["status"]
       ])
   arquivo.close()
