from business.job import Job
from datetime import timedelta

class Courier:

    def __init__(self,vehicle):
        self.time = timedelta(hours = 9)
        self.vehicle = vehicle
        self.jobs = list()


    def setJobs(self,jobs):
        self.jobs = jobs


    def setCargo(self):
        cargo = sum(map(lambda x: x.getWeight(), self.jobs))
        self.vehicle.setCargo(cargo)


    def doJobs(self):

        try:

            cost = 0
            self.setCargo()

            for job in jobs:

                wastedTime = self.vehicle.wastedTime(job.getDistance())
                self.time += timedelta(hours = wastedTime)

                if self.time > job.getTime():
                    raise Exception('Too late')

                cost = self.vehicle.pollutionCost(job.getDistance())
                self.vehicle.decreaseCargo(job.getWeight())
                self.time = job.getTime()

            return cost

        except:
            return float('inf')
