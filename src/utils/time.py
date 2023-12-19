from datetime import datetime, timedelta

class Time:

    def __init__(self):
        pass


    def convertStringToTime(time):
        time_datetime = datetime.strptime(time,'%H:%M:%S')
        return timedelta(
            hours = time_datetime.hour,
            minutes = time_datetime.minute,
            seconds = time_datetime.second)