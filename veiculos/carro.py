from veiculos.veiculo import Veiculo


class Carro(Veiculo):

    velocidade = 50
    capacidade = 100
    decrescimo = 0.1
    poluicao = 0.5

    
    def __init__(self):
        super().__init__(
            Carro.velocidade,
            Carro.capacidade,
            Carro.decrescimo,
            Carro.poluicao)