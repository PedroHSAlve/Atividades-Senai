class Livro:
    def __init__(self, título, autor, paginas, disponível):
        self.título = título
        self.autor = autor
        self.paginas = paginas
        self.disponível = disponível

    def cadastro(self):
        print("="*60)
        self.título = input("Digite o nome do livro que deseja cadastrar: ")
        self.autor = input("Digite o nome do autor responsável pelo livro: ")
        self.paginas = int(input("Digite o número de páginas do livro: "))
        self.disponível = bool(input("O livro está disponível? (True/False): "))
        print("="*60)
    def Descrição(self):
        print("="*60)
        print("Título: ",self.título)
        print("Autor: ", self.autor)
        print("Páginas: ", self.paginas)
        print("Disponível: ", self.disponível)
        print("="*60)

    def Emprestar(self):
        print("="*60)
        if self.disponível == True:
            print("Este livro pode ser emprestado")
            self.disponível = False
        else:
            print("Este livro já está emprestado")
        print("="*60)

    def Devolver(self):
        print("="*60)
        if self.disponível == True:
            print("Este livro já está disponível para emprestimo")
        else:
            print("Este livro foi devolvido")
        print("="*60)
while True:
    print("Bm vindo ao sistema da Biblioteca !")
    print("="*60)
    print(" ================ Menu de Opções ================")
    print("1- Cadastrar Livro")
    print("2- Ver Descrição do Livro")
    print("3- Emprestar Livro")
    print("4- Devolver Livro")
    print("="*60)

    l1 = Livro("A volta dos que não foram", "Ordep", 345, True)
    l2 = Livro("Poeira em alto Mar","Ary Toledo", 690, False)
    catalogo = [l1,l2]


    opção = int(input("Digite a opção desejada: "))

    if opção == 1:
        novo = Livro("","","",True)
        novo.cadastro()
        catalogo.append(novo)
    if opção == 2:
        for livro in catalogo:
            livro.Descrição()

    if opção == 3:
        titulo = input("Digite o nome do livro que deseja emprestar: ")
        for livro in catalogo:
            if livro.título == titulo:
                livro.Emprestar()
                break
        else:
            print("Livro não encontrado.")

    if opção == 4:
        titulo = input("Digite o nome do livro que deseja devolver: ")
        for livro in catalogo:
            if livro.título == titulo:
                livro.Devolver()
                break
        else:
            print("Livro não encontrado.")
        l2.Devolver()

    resposta = input("Deseja continuar? (S/N): ")
    if resposta == "S":
        continue
    else:
        print("Obrigado por utilizar o sistema da Biblioteca !")
        break
