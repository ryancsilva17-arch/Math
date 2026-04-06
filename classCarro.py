class Carro:
    def __init__(self, marca, modelo, ano):
        self.modelo = modelo
        self.ano = ano

meu_carro = Carro("Fusca", 1980)

print(meu_carro.modelo)   
print(meu_carro.ano)