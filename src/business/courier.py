import traceback
from business.job import Job
from utils.timeUtils import TimeUtils
from datetime import datetime, timedelta

class Courier:


    def __init__(self,vehicle,name='worker',startPoint='Missouri',startTime=timedelta(hours=9)):
        self.jobs = list()
        self.paths = list()
        self.name = name
        self.vehicle = vehicle
        self.startPoint = startPoint
        self.startTime = startTime
        if not(isinstance(startTime,timedelta)):
            self.startTime = TimeUtils.convertStringToTime(startTime)


    def __str__(self):
        buffer = ''
        buffer += 'Name: ' + str(self.name)
        buffer += '\tStart point: ' + str(self.startPoint)
        buffer += '\tStart time: ' + str(self.startTime)
        buffer += '\tVehicle: ' + str(self.vehicle)
        buffer += '\nJob: ' + '\nJob'.join([str(job) for job in self.jobs])
   #     buffer += '\nJob: ' + '\nJob: '.join([str(self.jobs[i]) + "\tPath: " + str(self.paths[i]) for i in range(len(self.jobs))])
        return buffer

    
    def getStartPoint(self):
        return self.startPoint


    def setJobs(self,jobs):
        cargo = sum(map(lambda x: x.getWeight(), jobs))
        self.jobs = jobs
        self.vehicle.setCargo(cargo)


    def doJobs(self,jobs,distanceBetween,pathBetween):


        try:

            currentCost = 0
            startTime = self.startTime
            currentPoint = self.startPoint
            
            self.setJobs(jobs)
            self.paths.clear()

            print(self)

            for job in self.jobs:

                self.paths.append(pathBetween(currentPoint,job.getDestination()))
                distance = distanceBetween(currentPoint,job.getDestination())
                startTime += self.vehicle.wastedTime(distance)
    
            #    print(distance)
            #    print(currentPoint)
            #    print(job.getDestination())
            #    print(f'hora de chegada: {startTime}')

                if startTime > job.getTime():
                    raise Exception('Too late')

                currentCost += self.vehicle.pollutionCost(distance)
                currentPoint = job.getDestination()

                self.vehicle.decreaseCargo(job.getWeight())
                startTime = job.getTime()

            distance = distanceBetween(currentPoint,self.startPoint)
            currentCost += self.vehicle.pollutionCost(distance)

            return currentCost

        except:
            traceback.print_exc()
            return float('inf')