from business.manager import Manager
from business.vehicle.bike import Bike
from business.vehicle.scooter import Scooter
from business.vehicle.car import Car
from business.vehicle.vehicle import Vehicle
from graph import Graph
from business.job import Job
from business.courier import Courier
from datetime import timedelta, datetime
from itertools import product
from ui.textUI import TextUI

"""
manager = Manager()

manager.addJob(Job(timedelta(hours=10,minutes=15),60,'Miilhazes'))
manager.addJob(Job(timedelta(hours=9,minutes=30),55,'Faria'))

manager.addCourier(Courier(Car()))
manager.addCourier(Courier(Scooter()))

combinationsJ = manager.generateJobsDistributions()
combinationsC = manager.generateCouriersDistribution()

for dictionary in combinationsJ:
    for key in dictionary:
        print(key)
        print(isinstance(key,str))
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