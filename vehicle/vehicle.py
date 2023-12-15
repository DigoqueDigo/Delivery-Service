class Vehicle:

    def __init__(self,speed,capacity,decrease,pollution):
        self.speed = speed
        self.capacity = capacity
        self.decrease = decrease
        self.pollution = pollution


    def __str__(self):
        return (
            f'Speed: {self.speed}\t'
            f'Capacity: {self.capacity}\t'
            f'Decrease: {self.decrease}\t'
            f'Pollution: {self.pollution}'
        )


    def getspeed(self):
        return self.speed


    def getcapacity(self):
        return self.capacity

    
    def getdecrease(self):
        return self.decrease


    def getpollution(self):
        return self.pollution