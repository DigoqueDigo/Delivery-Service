from combiner import Combiner

class Service:

    def __init__(self):
        self.jobsList = list()
        self.vehicleList = list()
        self.combiner = Combiner()

    
    def addJob(self,job):
        self.jobsList.append(job)


    def addVehicle(self,vehicle):
        self.vehicleList.append(vehicle)


    def generateVehiclesDistribution(self):
        return self.combiner.generateDistribution(self.vehicleList)

    
    def generateJobsDistributions(self):
        self.jobsList = sorted(self.jobsList, key=lambda x: x.getTime())
        return self.combiner.generateBoxDistributions(
            len(self.vehicleList),
            self.jobsList)