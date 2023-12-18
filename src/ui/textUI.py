from ui.menu import Menu
from ui.reader import Reader
from business.job import Job
from utils.saver import Saver
from business.manager import Manager

class TextUI:

    def __init__(self):
        self.reader = Reader()
        self.manager = Manager()
        self.saver = Saver('solution.txt')
        self.menu = Menu("Delivery Service")


    def setMenu(self):
        self.menu.addOption('1 - Load Map', self.loadMap)
        self.menu.addOption('2 - Plot Map', self.plotMap)
        self.menu.addOption('3 - Load Jobs', self.loadJobs)
        self.menu.addOption('4 - Show Jobs', self.showJobs)
        self.menu.addOption('5 - Load Couriers', self.loadCouriers)
        self.menu.addOption('6 - Show Couriers', self.showCouriers)
        self.menu.addOption('7 - Find Best Routes (limited resources)', self.limitedResources)
        self.menu.addOption('8 - Find Best Routes (unlimited resources)', self.unlimitedResources)
        self.menu.addOption('9 - Exit', self.byMessage)


    def implementing(self):
        self.menu.printErrorMessage("Implementing...")


    def plotMap(self):
        self.manager.plotGraph()


    def byMessage(self):
        self.menu.printSucessMessage("See ya!")


    def loadMap(self):
    #   path = self.menu.getLine('Enter an file: ')
        dictionary = self.reader.readDictionary('data/usa.json')
        self.manager.loadGraph(dictionary)


    def loadJobs(self):
    #    path = self.menu.getLine('Enter an file: ')
        dictionary = self.reader.readDictionary('data/jobs.json')
        self.manager.loadJobs(dictionary)


    def loadCouriers(self):
    #    path = self.menu.getLine('Enter an file: ')
        dictionary = self.reader.readDictionary('data/aa.json')
        self.manager.loadCouriers(dictionary)

    
    def limitedResources(self):
        cost, couriers = self.manager.findRouteOneState()
        self.saver.saveSolution(cost,couriers)
        

    def unlimitedResources(self):
        cost, couriers = self.manager.findRouteMultipleStates()
        self.saver.saveSolution(cost,couriers)


    def showJobs(self):
        print(self.manager.showJobs())


    def showCouriers(self):
        print(self.manager.showCouriers())


    def run(self):
        self.setMenu()
        self.menu.run()