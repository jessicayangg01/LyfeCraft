import pandas as pd
import os
import random

path = os.path.join("assets", "events.xlsx")
events = pd.read_excel(path)
 
allEvents = {}
totalEventsNum = 0

# puts all events in the events from excel into allEvents
for i in events:
    data = events.loc[:,i]
    allEvents[i] = []
    for j in events.loc[:,i]:
        allEvents[i].append(j)
    totalEventsNum = len(allEvents[i])

# returns a random event
def getEvent():
    randNum = random.randint(0,totalEventsNum-1)
    print(randNum)
    returnDict = {}
    for i in allEvents:
        returnDict[i] = allEvents[i][randNum]
    
    return returnDict






