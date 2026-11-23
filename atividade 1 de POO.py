class Carro:
    def __init__(self, nome, marca, modelo, ano):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Carro: {self.nome}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")    
        print(f"Ano: {self.ano}")

carro1 = Carro(911,"Porche", "esportivo", 1998 )
carro2 = Carro("Civic", "Honda", "Type R", 2000)

carro1.exibir()
carro2.exibir()


class Conta:
    def __init__(self, saldo ):
            self.__saldo = saldo

    def get_saldo(self):
         print("O seu valor em conta é de: ",self.__saldo)

    def depositar(self, valor):
         self.valor = valor
         self.__saldo += valor

pedro = Conta(20000)

pedro.depositar(2500)
pedro.get_saldo()


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
        