import traceback
from business.job import Job
from utils.timeUtils import TimeUtils
from datetime import datetime, timedelta

class Courier:


    def __init__(self,vehicle,name='worker',startPoint='Missouri',startTime=timedelta(hours=9)):
        self.jobs = list()
        self.name = name
        self.vehicle = vehicle
        self.startPoint = startPoint
        self.startTime = startTime
        if not(isinstance(startTime,timedelta)):
            self.startTime = TimeUtils.convertStringToTime(startTime)


    def __str__(self):
        return (
            f'Name: {self.name}\t'
            f'Start point: {self.startPoint}\t'
            f'Start time: {self.startTime}\t'
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

            for job in self.jobs:

                distance = distanceBetween(currentPoint,job.getDestination())
                self.startTime += self.vehicle.wastedTime(distance)
    
                print(distance)
                print(currentPoint)
                print(job.getDestination())
                print(f'hora de chegada: {self.startTime}')

                if self.startTime > job.getTime():
                    raise Exception('Too late')

                currentCost += self.vehicle.pollutionCost(distance)
                currentPoint = job.getDestination()

                self.vehicle.decreaseCargo(job.getWeight())
                self.startTime = job.getTime()

            distance = distanceBetween(currentPoint,self.startPoint)
            currentCost += self.vehicle.pollutionCost(distance)

            print(distance)

            return currentCost

        except:
            traceback.print_exc()
            return float('inf')