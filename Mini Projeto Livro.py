class Livro:
    def __init__(self, título, autor, paginas, disponível):
        self.título = título
        self.autor = autor
        self.paginas = paginas
        self.disponível = disponível

    def Descrição(self):
        print("Título: ",self.título)
        print("Autor: ", self.autor)
        print("Páginas: ", self.paginas)
        print("Disponível: ", self.disponível)

    def Emprestar(self):
        if self.disponível == True:
            print("Este livro pode ser emprestado")
            self.disponível = False
        else:
            print("Este livro já está emprestado")

    def Devolver(self):
        if self.disponível == True:
            print("Este livro já está disponível para emprestimo")
        else:
            print("Este livro foi devolvido")

l1 = Livro("A volta dos que não foram", "Ordep", 345, True)
l2 = Livro("Poeira em alto Mar", "Ary Toledo", 690, False)

x1 = input("Deseja ver a situação do livro 1? ")
l1.Emprestar()
x1 = input("Deseja ver a Descrição do livro 1? ")
l1.Descrição()
x1 = input("Já devolveu entao? ")
l1.Devolver()

x1 = input("Deseja ver a situação do livro 2? ")
l2.Emprestar()
x1 = input("Deseja ver a Descrição do livro 2? ")
l2.Descrição()
x1 = input("Já devolveu entao? ")
l2.Devolver()