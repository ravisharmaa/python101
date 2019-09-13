from datetime import datetime


class Date:

    def __init__(self):
        self.dateTimeObj = datetime

    def get_date(self):
        return self.dateTimeObj.today()


class Time(Date):

    def get_time(self):
        return self.dateTimeObj.now()


datetime = Time()
print(datetime.get_time())
