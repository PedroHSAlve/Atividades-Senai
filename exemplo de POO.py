class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque 

    def exibir(self):
        print(f"Produtos: {self.nome}")
        print(f"Preço: {self.preço}")
        print(f"Estoque; {self.estoque}")
        print("-" * 80)    

p1 = Produto("Arroz", 5.99, 30)
p2 = Produto("MAcarrão", 8.50, 80)

print(type(p1))
print(p1)
print(p1 == p2)

p1.exibir()
p2.exibir()