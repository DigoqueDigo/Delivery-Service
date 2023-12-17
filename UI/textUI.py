from UI.menu import Menu
from UI.reader import Reader
from colorama import Fore, Style
from business.manager import Manager

class TextUI:

    def __init__(self):
        self.reader = Reader()
        self.manager = Manager()
        self.menu = Menu("Delivery Service")


    def setMenu(self):
        self.menu.addOption('1 - Load map', self.loadMap)
        self.menu.addOption('2 - Plot map', self.plotMap)
        self.menu.addOption('3 - Add job', self.implementing)
        self.menu.addOption('4 - Add courier', self.implementing)
        self.menu.addOption('5 - Find best routes (limited resources)', self.implementing)
        self.menu.addOption('6 - Find best routes (unlimited resources)', self.implementing)
        self.menu.addOption('7 - Exit', self.byMessage)


    def implementing(self):
        print("Implementing...")


    def loadMap(self):
        print(f'{Style.BRIGHT}Enter an file: {Style.RESET_ALL}', end = '')
        dictionary = self.reader.readDictionary(self.reader.readLine())
        self.manager.loadGraph(dictionary)
    

    def plotMap(self):
        self.manager.plotGraph()

    
    def byMessage(self):
        print(f'{Fore.GREEN}{Style.BRIGHT}See ya!{Style.RESET_ALL}')


    def run(self):
        self.setMenu()
        self.menu.run()