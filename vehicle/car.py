from vehicle.vehicle import Vehicle

class Car(Vehicle):

    speed = 50
    capacity = 100
    decrease = 0.1
    pollution = 0.5

    
    def __init__(self):
        super().__init__(
            Car.speed,
            Car.capacity,
            Car.decrease,
            Car.pollution)