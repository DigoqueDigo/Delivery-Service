from graph import Graph
from random import randint
from combiner import Combiner

class Manager:

    def __init__(self):
        self.graph = Graph()
        self.jobsList = list()
        self.courierList = list()
        self.combiner = Combiner()


    def addJob(self,job):
        self.jobsList.append(job)


    def addCourier(self,courier):
        self.courierList.append(courier)


    def loadGraph(self,dictionary):

        for sourceNode in dictionary:
            self.graph.addNode(sourceNode)

            for neighbourNode in dictionary[sourceNode]:
                self.graph.addEdge(sourceNode,neighbourNode,randint(0,100))


    def plotGraph(self):
        self.graph.plot()


    def generateCourierDistribution(self):
        courierList = list()
        courierList.append(Courier(Car()))
        courierList.append(Courier(Bike()))
        courierList.append(Courier(Scooter()))
        return self.combiner.generateDistribution(courierList,len(self.jobsList))

    
    def generateJobsDistributions(self):
        self.jobsList = sorted(self.jobsList, key=lambda x: x.getTime())
        return self.combiner.generateBoxDistributions(
            len(self.courierList),
            self.jobsList)


    def findRouteOneState(self):

        bestCost = float('inf')
        bestJobCombination = []

        jobCombinations = self.combiner.generateBoxDistributions(
            len(self.courierList),
            self.jobsList
        )

        for currentJobCombination in jobCombinations:
            
            currentCost = 0

            for i in range(len(self.courierList)):

                self.courierList[i].setJobs(currentJobCombination[i])
                currentCost += self.courierList[i].doJobs()

                if currentCost == float('inf'):
                    break

            if currentCost < bestCost:
                bestCost = currentCost
                bestJobCombination = currentJobCombination

        return (bestCost,bestJobCombination)


    def findRouteMultipleStates(self):

        bestCost = float('inf')
        bestJobCombination = []
        bestCourierCombination = []

        courierCombinations = self.generateCourierDistribution()

        for currentCourierCombination in courierCombinations:

            self.courierList = currentCourierCombination
            (currentCost,currentJobCombination) = self.findRouteOneState()

            if cost < best:
                bestCost = currentCost
                bestJobCombination = currentJobCombination
                bestCourierCombination = currentCourierCombination

        return (bestCost,bestJobCombination,bestCourierCombination)