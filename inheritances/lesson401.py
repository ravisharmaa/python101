from datetime import datetime


class Date:

    def __init__(self):
        self.date_time_obj = datetime

    def get_date(self):
        return self.date_time_obj.today()


class Time(Date):

    def get_time(self):
        return self.date_time_obj.now().strftime("%Y-%m-%d %H:%M")


datetime = Time()
print(datetime.get_time())
print(datetime.get_date())
