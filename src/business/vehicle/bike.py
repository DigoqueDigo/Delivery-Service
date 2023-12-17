from business.vehicle.vehicle import Vehicle

class Bike(Vehicle):

    speed = 10
    capacity = 5
    decrease = 0.6
    pollution = 0.05


    def __init__(self):
        super().__init__(
            Bike.speed,
            Bike.capacity,
            Bike.decrease,
            Bike.pollution)