import copy
from graph import Graph
from random import randint
from utils.combiner import Combiner
from utils.creator import Creator
from business.job import Job
from business.courier import Courier

class Manager:

    def __init__(self):
        self.graph = Graph()
        self.jobsList = list()
        self.courierList = list()


    def plotGraph(self):
        self.graph.plot()


    def showJobs(self):
        result = [str(jobs) for jobs in self.jobsList]
        return '\n'.join(result)


    def showCouriers(self):
        result = [str(courier) for courier in self.courierList]
        return '\n'.join(result)


    def loadJobs(self,dictionary):
        for job in dictionary:
            self.jobsList.append(Job(
                job['code'],
                job['time'],
                job['weight'],
                job['destination']))


    def loadCouriers (self,dictionary):
        for courier in dictionary:
            self.courierList.append(Courier(
                Creator.createVehicle(courier['vehicle']),
                courier['name'],
                courier['startPoint'],
                courier['startTime']))


    def loadGraph(self,dictionary):
        for sourceNode in dictionary:
            self.graph.addNode(sourceNode)
            for neighbourNode in dictionary[sourceNode]:
                self.graph.addEdge(sourceNode,neighbourNode,randint(0,5))
        self.graph.loadDictionary()


    def generateCouriersDistribution(self):
        courierList = []
        combinations = Combiner.generateDistribution(
            ['car','bike','scooter'],
            len(self.jobsList))

        for i in range(len(combinations)):
            courierList.append(list())
            for vehicle in combinations[i]:
                courierList[i].append(Courier(Creator.createVehicle(vehicle)))

        return courierList


    def generateJobsDistributions(self):
        return Combiner.generateBoxDistributions(
            len(self.courierList),
            self.jobsList)


    def findRouteOneState(self):

        bestCost = float('inf')
        bestCourierCombination = []

        jobCombinations = Combiner.generateBoxDistributions(
            len(self.courierList),
            self.jobsList
        )

        for currentJobCombination in jobCombinations:

            currentCost = 0

            for key in range(len(self.courierList)):

                currentCost += self.courierList[key].doJobs(
                    currentJobCombination[str(key)],
                    self.graph.distanceBetween,
                    self.graph.pathBetween)

                if currentCost == float('inf'):
                    break

            if currentCost < bestCost:
                bestCost = currentCost
                bestCourierCombination = copy.deepcopy(self.courierList)

            for courier in self.courierList:
                courier.clearJobs()

        return bestCost, bestCourierCombination


    def findRouteMultipleStates(self):

        bestCost = float('inf')
        bestCourierCombination = []

        temp = self.courierList
        couriersCombinations = self.generateCouriersDistribution()

        for currentCourierCombination in couriersCombinations:

            self.courierList = currentCourierCombination
            currentCost, currentCourierCombination = self.findRouteOneState()

            if currentCost < bestCost:
                bestCost = currentCost
                bestCourierCombination = copy.deepcopy(currentCourierCombination)

        self.courierList = temp
        return bestCost, bestCourierCombination
