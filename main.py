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

# Função para cadastrar livros
def cadastrar_livro():
   titulo = input("Digite o título: ")
   autor = input("Digite o autor: ")
   ano = input("Digite o ano de publicação: ")
   codigo = input("Digite o código/ISBN: ")
   livro = {
       "titulo": titulo,
       "autor": autor,
       "ano": ano,
       "codigo": codigo,
       "status": "disponível"
   }
   livros.append(livro)
   # Salva o livro imediatamente
   salvar_livros()
   print("Livro cadastrado com sucesso!")
# Função para emprestar livros
def emprestar_livro():
   codigo = input("Digite o código/ISBN: ")
   for livro in livros:
       if livro["codigo"] == codigo:
           if livro["status"] == "disponível":
               livro["status"] = "emprestado"
               salvar_livros()
               print("Livro emprestado com sucesso!")
           else:
               print("Esse livro já está emprestado.")
           return
   print("Livro não encontrado.")
   # Função para devolver livros
def devolver_livro():
   codigo = input("Digite o código/ISBN: ")
   for livro in livros:
       if livro["codigo"] == codigo:
           if livro["status"] == "emprestado":
               livro["status"] = "disponível"
               salvar_livros()
               print("Livro devolvido com sucesso!")
           else:
               print("Esse livro já está disponível.")
           return
   print("Livro não encontrado.")
# Função para listar os livros
def listar_livros():
   if len(livros) == 0:
       print("Nenhum livro cadastrado.")
   else:
       print("\n===== LIVROS =====")
       for livro in livros:
           print("--------------------")
           print("Título:", livro["titulo"])
           print("Autor:", livro["autor"])
           print("Ano:", livro["ano"])
           print("Código:", livro["codigo"])
           print("Status:", livro["status"])
# Função para buscar livros
# Função para listar todos os livros cadastrados
def listar_livros():
   if len(livros) == 0:
       print("\nNenhum livro cadastrado.")
       return
   print("\n===== LIVROS CADASTRADOS =====")
   for livro in livros:
       print("-----------------------------")
       print("Título:", livro["titulo"])
       print("Autor:", livro["autor"])
       print("Ano:", livro["ano"])
       print("Código:", livro["codigo"])
       print("Status:", livro["status"])
   print("-----------------------------")
# Função para ordenar os livros
def ordenar_livros():
   print("\n1 - Por título")
   print("\n2 - Por autor")
   print("\n3 - Por ano")
   opcao = input("Escolha: ")
   if opcao == "1":
       livros.sort(key=lambda livro: livro["titulo"])
       print("Livros ordenados por título.")
   elif opcao == "2":
       livros.sort(key=lambda livro: livro["autor"])
       print("Livros ordenados por autor.")
   elif opcao == "3":
       livros.sort(key=lambda livro: livro["ano"])
       print("Livros ordenados por ano.")
   else:
       print("Opção inválida.")
   salvar_livros()

# Carrega os livros quando o programa começa
carregar_livros()

# Menu principal
while True:
   print("\n SISTEMA DE BIBLIOTECA ")
   print("1 - Cadastrar livro")
   print("2 - Emprestar livro")
   print("3 - Devolver livro")
   print("4 - Listar livros")
   print("5 - Buscar livro")
   print("6 - Ordenar livros")
   print("7 - Sair")
   opcao = input("Escolha uma opção: ")
   if opcao == "1":
       cadastrar_livro()
   elif opcao == "2":
       emprestar_livro()
   elif opcao == "3":
       devolver_livro()
   elif opcao == "4":
       listar_livros()
   elif opcao == "5":
       buscar_livro()
   elif opcao == "6":
       ordenar_livros()
   elif opcao == "7":
       # Salva antes de fechar o programa
       salvar_livros()
       print("Livros salvos!")
       print("Programa encerrado!")
       break
   else:
       print("Opção inválida.")
