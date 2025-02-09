from read import Read
import pandas as pd
from datetimemod import Now
from realtimeset import Timeset

# time = Timeset().actual_time
time = "09:00"
time = int(time[0:2] + time[3:5])




class lecture_status:
    def __init__(self,time):
        # if else statements:
        if time >= 900 and time < 1000:
            self.status = "Lecture in progress"
            print(self.status)
        elif time >= 1005 and time < 1105:
            pass
        elif time >= 1105 and time < 1125:
            status = "Tea Break"
        elif time >= 1125 and time < 1225:
            pass
        elif time >= 1230 and time < 1330:
            pass
        elif time >= 1335 and time < 1435:
            pass
        elif time >= 1440 and time < 1340:
            pass
        elif time >= 1440 and time < 1540:
            pass
    
