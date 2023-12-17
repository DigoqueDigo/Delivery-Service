class Vehicle:

    def __init__(self,speed,capacity,decrease,pollution):
        self.cargo = 0
        self.speed = speed
        self.capacity = capacity
        self.decrease = decrease
        self.pollution = pollution


    def __str__(self):
        return (
            f'Cargo: {self.cargo}\t'
            f'Speed: {self.speed}\t'
            f'Capacity: {self.capacity}\t'
            f'Decrease: {self.decrease}\t'
            f'Pollution: {self.pollution}'
        )


    def getSpeed(self):
        return self.speed


    def getCapacity(self):
        return self.capacity

    
    def getDecrease(self):
        return self.decrease


    def getPollution(self):
        return self.pollution


    def getCargo(self):
        return self.getCargo


    def setCargo(self,cargo):
        if (self.capacity < cargo):
            raise Exception("Too much cargo")
        self.cargo = cargo

    
    def decreaseCargo(self,cargo):
        self.cargo -= cargo


    def pollutionCost(self,distance):
        return self.pollution*distance


    def wastedTime(self,distance):
        velocity = self.speed-(self.decrease*self.cargo)
        return timedelta(hours = distance.velocity)