from business.vehicle.vehicle import Vehicle

class Scooter(Vehicle):

    speed = 35
    capacity = 20
    decrease = 0.5
    pollution = 0.2


    def __init__(self): 
        super().__init__(
            Scooter.speed,
            Scooter.capacity,
            Scooter.decrease,
            Scooter.pollution)