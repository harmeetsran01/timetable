from read import Read
import pandas as pd
from datetimemod import Now

# declareation of varibles to be used 
data = Read()
data = data.lines
data = [line.replace("\n", "").split(",") for line in data]


day = Now()
day = day.day_time[0]
print(day)

time = Now()
time = time.day_time[1]
print((time[0:2]))
time_in_am = int(time[0:2]) % 12
print(time_in_am)

# Assigning the data to the respective variables


print("Only BCA22A Lectures: ")
print("""Lecture: {}
      Venue: {}
      Teacher: {}
      Time: {}""".format(data[0][0],))