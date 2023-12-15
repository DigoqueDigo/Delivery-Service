from datetime import timedelta

class Job:

    def __init__(self,dest,time,weight):
        self.dest = dest
        self.time = time
        self.weight = weight

    
    def __str__(self):
        return (
            f'Destination: {self.dest}\t'
            f'Time: {self.time}\t'
            f'weight: {self.weight}'
        )


    def getDest(self):
        return self.dest

    
    def getTime(self):
        return self.time


    def getWeight(self):
        return self.weight