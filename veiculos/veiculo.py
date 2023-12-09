class Veiculo:

    def __init__(self,velocidade,capacidade,decrescimo,poluicao):
        self.velocidade = velocidade
        self.capacidade = capacidade
        self.decrescimo = decrescimo
        self.poluicao = poluicao


    def __str__(self):
        return (
            f'Velocidade: {self.velocidade}\t'
            f'Capacidade: {self.capacidade}\t'
            f'Decrescimo: {self.decrescimo}\t'
            f'Poluição: {self.poluicao}'
        )


    def getVelocidade(self):
        return self.velocidade


    def getCapacidade(self):
        return self.capacidade

    
    def getDecrescimo(self):
        return self.decrescimo


    def getPoluicao(self):
        return self.poluicao