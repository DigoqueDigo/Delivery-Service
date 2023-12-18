from datetime import datetime, timedelta

class Job:

    def __init__(self,time,weight,destination):
        self.time = time
        self.weight = weight
        self.destination = destination

        if not(isinstance(time,timedelta)):
            time_datetime = datetime.strptime(time,'%H:%M:%S')
            self.time = timedelta(
                hours = time_datetime.hour,
                minutes = time_datetime.minute,
                seconds = time_datetime.second)


    def __str__(self):
        return (
            f'Time: {self.time}\t'
            f'Weight: {self.weight}\t'
            f'Destination: {self.destination}'
        )


    def getDestination(self):
        return self.destination


    def getTime(self):
        return self.time


    def getWeight(self):
        return self.weight