from veiculos.veiculo import Veiculo


class Bicicleta(Veiculo):

    velocidade = 10
    capacidade = 5
    decrescimo = 0.6
    poluicao = 0.05

    
    def __init__(self):
        super().__init__(
            Bicicleta.velocidade,
            Bicicleta.capacidade,
            Bicicleta.decrescimo,
            Bicicleta.poluicao)