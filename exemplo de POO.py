class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque 

p1 = Produto("Arroz", 5.99, 30)
p2 = Produto("MAcarrão", 8.50, 80)

print(type(p1))
print(p1)
print(p1 == p2)