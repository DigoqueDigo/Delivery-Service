from datetime import timedelta

class Job:

    def __init__(self,dest,time,weight):
        self.dest = dest
        self.time = time
        self.weight = weight
        self.distance = 0

    
    def __str__(self):
        return (
            f'Distance: {self.distance}'
            f'Destination: {self.dest}\t'
            f'Time: {self.time}\t'
            f'Weight: {self.weight}\t'
            f'Distance: {self.distance}'
        )


    def getDest(self):
        return self.dest

    
    def getTime(self):
        return self.time


    def getWeight(self):
        return self.weight


    def getDistance(self):
        return self.distance

    
    def setDistance(self,distance):
        self.distance = distance