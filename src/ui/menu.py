from ui.reader import Reader
from colorama import Fore, Style

class Menu:

    def __init__(self,title):
        self.title = title
        self.options = list()
        self.functions = list()
        self.reader = Reader()


    def addOption(self,option,function):
        self.options.append(option)
        self.functions.append(function)


    def printSucessMessage(self,message):
        print(f'{Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}')


    def printErrorMessage(self,message):
        print(f'{Fore.RED}{Style.BRIGHT}{message}{Style.RESET_ALL}')


    def getLine(self,message):
        print(f'{Style.BRIGHT}{message}{Style.RESET_ALL}', end = '')
        return self.reader.readLine()


    def show(self):
        print(f'{Fore.MAGENTA}{Style.BRIGHT}{self.title}{Style.RESET_ALL}')
        for option in self.options:
            print(f'{Fore.YELLOW}{Style.BRIGHT}{option}{Style.RESET_ALL}')


    def run(self):

        option = 0

        while option != len(self.options):

            self.show()
            print(f'{Style.BRIGHT}Enter an option: {Style.RESET_ALL}', end = '')

            try:
                option = self.reader.readInt()
                self.functions[option-1]()

            except FileNotFoundError:
                print(f'{Fore.RED}{Style.BRIGHT}Invalid file{Style.RESET_ALL}')

            except Exception as e:
                print(f'{Fore.RED}{Style.BRIGHT}Invalid entry{Style.RESET_ALL}')