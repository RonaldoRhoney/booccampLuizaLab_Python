class Bicicleta:
    def __init__(self, cor, marca, modelo, ano, valor):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim...')
    
    def parar(self):
        print("parando a bicicleta...")
        print("bicicleta parada!")

    def correr(self):
        print("Vrummm...")

    def __str__ (self):
        return f"{self.__class__.__name__}: {',' .join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Caloi", "Mountain Bike", 2020, 1500)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.marca, b1.ano, b1.valor)