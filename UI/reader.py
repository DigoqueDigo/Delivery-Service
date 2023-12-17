import json

class Reader:

    def __init__(self):
        pass

    
    def readInt(self):
        try:
            return int(input())
        except:
            raise Exception()



    def readLine(self):
        return input()


    def readDictionary(self,sourcePath):

        try:
            with open(sourcePath, 'r') as jsonfile:
                return json.load(jsonfile)

        except Exception as e:
            raise e