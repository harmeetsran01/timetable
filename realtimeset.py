from read import Read
import pandas as pd
from datetimemod import Now

class Timeset:
    def __init__(self):
        self.day = Now()
        self.day = self.day.day_time[0]
        # print(self.day)

        self.time = Now()
        self.time = self.time.day_time[1]
        if int(self.time[0:2]) >= 12:
            self.period = "PM"
        else:
            self.period = "AM"
        self.time_in_am = int(self.time[0:2]) % 12
        self.time_12hr_format = f"{self.time_in_am:02}:{self.time[3:5]} {self.period}"
        # print(self.time_12hr_format)
        self.timefront = int(self.time_12hr_format[0:2])
        self.timeback = int(self.time_12hr_format[3:5])
        self.actual_time = f"{self.timefront:02}:{self.timeback}"
        print(self.actual_time)
        # print(type(self.actual_time))

    # print((time[0:5]))
    # time_in_am = int(time[0:2]) % 12
    # print((time_in_am))

