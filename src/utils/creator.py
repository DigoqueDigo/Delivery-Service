from business.vehicle import Car, Scooter, Bike


class Creator:

    def __init__(self):
        pass


    def createVehicle(string):

        if string == 'car':
            vehicle = Car()

        elif string == 'scooter':
            vehicle = Scooter()

        else:
            vehicle = Bike()

        return vehicle