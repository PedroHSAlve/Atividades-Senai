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

    def preço_total(self):
        ptotal = self.preço * self.estoque
        print(f"O preço total de mercadorias em estoque é: {ptotal:.2f} ")

    def quantidade_vendida(self,quantidade):
        self.estoque -= quantidade

    def preço_venda(self, venda):
        pvenda = self.preço * venda
        print(f"O preço dos produtos vendidos foi de: {pvenda:.2f}")

    def repor_estoque(self, quantidade):
        self.estoque += quantidade


p1 = Produto("Arroz", 5.99, 30)
p2 = Produto("Macarrão", 8.50, 80)

    

print(type(p1))
print(p1)
print(p1 == p2)

p1.quantidade_vendida(5)
p1.repor_estoque(15)

p2.quantidade_vendida(5)
p2.repor_estoque(15)

print(f"\n Valor total em estoque - {p1.nome}: R$ {p1.preço_total()}")

p1.exibir()
p2.exibir()