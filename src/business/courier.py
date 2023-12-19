from utils.time import Time
from datetime import timedelta

class Courier:


    def __init__(self,vehicle,name='worker',startPoint='Missouri',startTime=timedelta(hours=8)):
        self.jobs = list()
        self.paths = list()
        self.name = name
        self.vehicle = vehicle
        self.startPoint = startPoint
        self.startTime = startTime
        if not(isinstance(startTime,timedelta)):
            self.startTime = Time.convertStringToTime(startTime)


    def __str__(self):
        buffer = ''
        buffer += 'Name: ' + str(self.name)
        buffer += '\tStart point: ' + str(self.startPoint)
        buffer += '\tStart time: ' + str(self.startTime)
        buffer += '\tVehicle: ' + str(self.vehicle)
        buffer += '\nJob: ' + '\nJob'.join([str(job) for job in self.jobs])
        return buffer

    """
    def __str__(self):
        buffer = ''
        buffer += 'Name: ' + str(self.name)
        buffer += '\tStart point: ' + str(self.startPoint)
        buffer += '\tStart time: ' + str(self.startTime)
        buffer += '\tVehicle: ' + str(self.vehicle)
        buffer += '\nJob: ' + '\nJob: '.join(
            [str(self.jobs[i]) + '\tDistance: ' + str(self.paths[i][0]) +
            '\tPath: ' + str(self.paths[i][1]) for i in range(len(self.jobs))])
        
        if len(self.paths) > 1:
            buffer += '\nBack home: \tDistance: ' + str(self.paths[-1][0])
            buffer += '\tPath: ' + str(self.paths[-1][1])

        return buffer
    """

    def getStartPoint(self):
        return self.startPoint


    def clearJobs(self):
        self.jobs = []


    def setJobs(self,jobs):
        cargo = sum(map(lambda x: x.getWeight(), jobs))
        self.jobs = jobs
        self.vehicle.setCargo(cargo)


    def doJobs(self,jobs,distanceBetween,pathBetween):

        try:

            currentCost = 0
            currentTime = self.startTime
            currentPoint = self.startPoint

            self.setJobs(jobs)
            self.paths.clear()

            for job in self.jobs:

                distance = distanceBetween(currentPoint,job.getDestination())
                self.paths.append((distance,pathBetween(currentPoint,job.getDestination())))
                currentTime += self.vehicle.wastedTime(distance)

                if currentTime > job.getTime():
                    raise Exception('Too late')

                currentCost += self.vehicle.pollutionCost(distance)
                currentPoint = job.getDestination()
                currentTime = job.getTime()

                self.vehicle.decreaseCargo(job.getWeight())

            distance = distanceBetween(currentPoint,self.startPoint)
            self.paths.append((distance,pathBetween(currentPoint,self.startPoint)))
            currentCost += self.vehicle.pollutionCost(distance)

            return currentCost

        except:
            return float('inf')