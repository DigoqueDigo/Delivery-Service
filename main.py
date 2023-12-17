from business.manager import Manager
from business.vehicle.bike import Bike
from business.vehicle.scooter import Scooter
from business.vehicle.car import Car
from business.vehicle.vehicle import Vehicle
from graph import Graph
from datetime import timedelta
from itertools import product
from UI.textUI import TextUI

"""
service = Service()

service.addJob(Job('Milhazes',timedelta(hours=10,minutes=15),60))
service.addJob(Job('Faria',timedelta(hours=9,minutes=30),55))


service.addVehicle(Bike())
service.addVehicle(Scooter())

combinationsJ = service.generateJobsDistributions()
combinationsV = service.generateVehiclesDistribution()

for dictionary in combinationsJ:
    for key in dictionary:
        print(key)
        for objeto in dictionary[key]:
            print(objeto)

        print('()')

    print('-----------------')


bike = Bike()
scooter = Scooter()
car = Car()


graph = Graph()

graph.addNode('Faria')
graph.addNode('Milhazes')
graph.addNode('Cristelo')
graph.addNode('Vilar de Figos')

graph.addEdge('Faria','Milhazes',15)
graph.addEdge('Milhazes','Vilar de Figos',30)
graph.addEdge('Vilar de Figos','Faria',55)
graph.addEdge('Cristelo','Faria',5)
graph.addEdge('Milhazes','Cristelo',30)
graph.addEdge('Vilar de Figos','Milhazes',100)

aa = graph.dijkstraAll('Faria')

print(aa)

graph.plot()

graph.loadDictionary()

graph.plot()

print(bike)
print(scooter)
print(car)
"""

textUI = TextUI()
textUI.run()