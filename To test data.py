from read import Read
import pandas as pd
from datetimemod import Now

# declareation of varibles to be used 
data = Read()
data = data.lines
data = [line.replace("\n", "").split(",") for line in data]

print(data[47])