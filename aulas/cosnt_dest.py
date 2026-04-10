class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print('Incializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def __del__(self):
        print('Destruindo a classe...' )

    def falar(self):
        print('Au au...')

def criar_cachorro():
    c = Cachorro('Rex', 'Marrom', False)
    print(c.nome)
criar_cachorro()