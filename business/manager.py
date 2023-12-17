from graph import Graph
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

    
    def addNode(self,node):
        self.graph.addNode(node)


    def addEdge(self,source,dest,weigth):
        self.graph.addEdge(source,dest,weigth)


    def plotGraph(self):
        self.graph.plot()


    def generateCourierDistribution(self):
        return self.combiner.generateDistribution(self.courierList)

    
    def generateJobsDistributions(self):
        self.jobsList = sorted(self.jobsList, key=lambda x: x.getTime())
        return self.combiner.generateBoxDistributions(
            len(self.courierList),
            self.jobsList)


    def findRouteOneState(self):

        bestCost = float('inf')
        bestCombination = []

        jobsCombinations = self.combiner.generateBoxDistributions(
            len(self.courierList),
            self.jobsList
        )

        for currentCombination in jobsCombinations:
            currentCost = 0

            for i in range(len(self.courierList)):

                self.courierList[i].setJobs(currentCombination[i])
                currentCost += self.courierList[i].doJobs()

                if currentCost == float('inf'):
                    break

            if currentCost < bestCost:
                bestCost = currentCost
                bestCombination = currentCombination

        return (bestCost,bestCombination)