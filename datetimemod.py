import datetime as dt

class Now:
    def __init__(self):
        self.now = dt.datetime.now()
        self.day_time = [self.now.strftime('%A'), self.now.strftime('%H:%M:%S')]
        self.hour_only = self.now.strftime('%H')
        self.minute_only = self.now.strftime('%M')
        # print(f"Day: {self.day_time[0]}")
        # print(f"Time: {self.day_time[1]}")
        # print(f"Hour: {self.hour_only}")
        # print(f"Minutes: {self.minute_only}")

