from read import Read
import pandas as pd
from datetimemod import Now
from realtimeset import Timeset

# declareation of varibles to be used 
# IMPORTANT This data element number is 1 Addition to actual data
# in CSV 10 but in data[9] because of 0 index

data = Read()
data = data.lines
data = [line.replace("\n", "").split(",") for line in data]
# print(data[0])
# print(data)

# TIME and DATE
day = Now()
day = day.day_time[0]
# print(day)

time = Now()
time = time.day_time[1]
time_in_am = int(time[0:2]) % 12
# print((time[0:2]))
# print(time_in_am)


# print(data[0].split(","))    
# print(type(data[0]))

# Assigning Days to the respective variables
checkday = {"Monday": data[9][0], "Tuesday": data[47][0], "Wednesday": data[85][0], "Thursday": data[123][0], "Friday": data[160][0], "Saturday": data[198][0], "Sunday": "No Lectures"}
print(checkday[day])

# if else timming:

# if time_in_am >= 9 :
#     print("""Lecture: {}
#       Venue: {}
#       Teacher: {}
#       Time: {}""".format(data[9][0], data[9][1], data[9][2], data[9][3]))

