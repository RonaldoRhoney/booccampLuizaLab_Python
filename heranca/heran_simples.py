class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print('Ligando o motor...')

    def __str__(self):
        return f"{self.__class__.__name__}: " + ", ".join(
            [f"{chave} = {valor}" for chave, valor in self.__dict__.items()]
        )


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregando):
        super().__init__(cor, placa, rodas)
        self.carregando = carregando

    def esta_carregando(self):
        print(f"{'Sim' if self.carregando else 'Não'} estou carregando")


# Instâncias
moto = Motocicleta("preta", "ABC-1235", 2)
carro = Carro("vermelho", "DEF-5679", 4)
caminhao = Caminhao("azul", "GHI-9013", 6, True)

print(moto)
print(carro)
print(caminhao)

caminhao.esta_carregando()