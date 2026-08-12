
O meu projeto e um sistema de biblioteca. Ele serve para cadastrar livros e controlar se eles estao disponiveis ou emprestados.
Primeiro, criei uma lista chamada livros = []. Essa lista serve para guardar os livros enquanto o programa esta funcionando. Cada livro tem informacoes como titulo, autor, ano, codigo e status.
A funcao carregar_livros() serve para pegar os livros que ja estao salvos no arquivo livros.csv. Assim, quando eu fechar o programa e abrir novamente, os livros continuam salvos. Se o arquivo ainda nao existir, o programa nao da erro.
A funcao salvar_livros() serve para salvar os livros no arquivo CSV. Ela coloca as informacoes de cada livro dentro do arquivo, como titulo, autor, ano, codigo e status.
A funcao cadastrar_livro() serve para cadastrar um novo livro. O programa pergunta o titulo, autor, ano e codigo do livro. Depois, coloca o status como "disponivel" e salva o livro.
A funcao emprestar_livro() serve para emprestar um livro. O usuario digita o codigo do livro e o programa procura ele. Se o livro estiver disponivel, o status muda para "emprestado". Se ele ja estiver emprestado, o programa avisa.
A funcao devolver_livro() serve para devolver um livro. O programa procura o livro pelo codigo e, se ele estiver emprestado, muda o status para "disponivel" novamente.
A funcao listar_livros() mostra todos os livros cadastrados. Ela mostra o titulo, autor, ano, codigo e se o livro esta disponivel ou emprestado.
A funcao buscar_livro() serve para procurar um livro. O usuario pode pesquisar pelo titulo ou pelo autor. Se o programa encontrar o livro, ele mostra algumas informacoes sobre ele.
A funcao ordenar_livros() serve para organizar os livros. Eu coloquei tres opcoes: ordenar pelo titulo, pelo autor ou pelo ano.
Depois dessas funcoes, eu uso carregar_livros() para carregar os livros salvos antes de comecar o programa.
Por ultimo, fiz um menu usando while True. Esse menu fica aparecendo ate o usuario escolher a opcao 7, que e sair.
O menu tem as opcoes de cadastrar, emprestar, devolver, listar, buscar, ordenar e sair.
Entao, de forma geral, o meu programa e um sistema simples de biblioteca. Ele permite cadastrar e organizar livros, controlar emprestimos e devolucoes e salvar tudo em um arquivo para nao perder os dados quando o programa for fechado.
 