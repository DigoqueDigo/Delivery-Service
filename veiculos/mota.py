from veiculos.veiculo import Veiculo


class Mota(Veiculo):

    velocidade = 35
    capacidade = 20
    decrescimo = 0.5
    poluicao = 0.2


    def __init__(self): 
        super().__init__(
            Mota.velocidade,
            Mota.capacidade,
            Mota.decrescimo,
            Mota.poluicao)