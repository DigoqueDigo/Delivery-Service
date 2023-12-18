import traceback
from business.job import Job
from datetime import timedelta

class Courier:


    def __init__(self,vehicle,name='worker',startPoint='Missouri'):
        self.name = name
        self.vehicle = vehicle
        self.startPoint = startPoint
        self.time = timedelta(hours = 9)
        self.jobs = list()


    def __str__(self):
        return (
            f'Name: {self.name}\t'
            f'Start time: {self.time}\t'
            f'Start point: {self.startPoint}\t'
            f'Vehicle: {self.vehicle}'
        )

    
    def getStartPoint(self):
        return self.startPoint


    def setJobs(self,jobs):
        self.jobs = jobs


    def setCargo(self):
        cargo = sum(map(lambda x: x.getWeight(), self.jobs))
        self.vehicle.setCargo(cargo)


    def doJobs(self,distanceBetween):

        try:

            currentCost = 0
            currentPoint = self.startPoint
            
            self.setCargo()

            for job in jobs:

                distance = distanceBetween(currentPoint,job.getDestination())
                wastedTime = self.vehicle.wastedTime(distance)
                self.time += timedelta(hours = wastedTime)

                print(distance)
                print(currentPoint)
                print(job.getDestination())

                if self.time > job.getTime():
                    raise Exception('Too late')

                currentCost += self.vehicle.pollutionCost(distance)
                currentPoint = job.getDestination()

                self.vehicle.decreaseCargo(job.getWeight())
                self.time = job.getTime()

            distance = distanceBetween(currentPoint,self.startPoint)
            currentCost += self.vehicle.pollutionCost(distance)

            return currentCost

        except:
            traceback.print_exc()
            return float('inf')