from utils.time import Time
from datetime import timedelta

class Job:

    def __init__(self,code,time,weight,destination):
        self.code = code
        self.time = time
        self.weight = weight
        self.destination = destination
        if not(isinstance(time,timedelta)):
            self.time = Time.convertStringToTime(time)


    def __str__(self):
        return (
            f'Code: {self.code}\t'
            f'Time: {self.time}\t'
            f'Weight: {self.weight}\t'
            f'Destination: {self.destination}'
        )


    def getDestination(self):
        return self.destination


    def getTime(self):
        return self.time


    def getWeight(self):
        return self.weight