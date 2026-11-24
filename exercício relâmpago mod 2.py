class Veículo:
    def __init__(self,nome,velocidade,combustível):
        self.nome = nome
        self.velocidade_max = velocidade
        self.combustível = combustível

    def mover(self):
        return (f"O veículo pode chegar a {self.velocidade_max}")

class Carro(Veículo):

    def __init__(self,nome,velocidade,combustível, qnt_portas,nome_marca):
        super.__init__(nome,velocidade,combustível)
        self.qnt_portas = qnt_portas
        self.nome_marca = nome_marca

    def marca(self):
        return self.nome_marca
    
    def velocidade_max(self, velocidade):
        return super().velocidade_max(velocidade)

    def mover(self,combustível):
        return (f" o carro ainda tem {combustível} litros de combustível")

class Bicicleta(Veículo):
    def marca(self):
        return self.nome_marca

    def velocidade_max(self, velocidade):
        return super().velocidade_max(velocidade)

    def mover(self, combustível):
        return combustível

v1 = Carro("Corvette", 250, 20 , 2 , "Ford")
v2 = Bicicleta("Monark", 35, "Tração Humana")

v = input("Deseja ver a situação do primeiro veículo? ")
v1.marca()
v1.velocidade_max()
v1.mover()

v2 = input("Deseja ver a situação do veículo 2 ? ")
v2.marca()
v2.velocidade_max()
v2.mover()

v1.exibir()
v2.exibir()