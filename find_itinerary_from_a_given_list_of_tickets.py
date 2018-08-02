def printItinerary(dataSet):
    reverseMap = {}
    for x,y in dataSet.items():
        reverseMap[y] = x

    start = None
    for item in dataSet:
        if not(item in reverseMap):
            start = item #start of the itinerary 
            break
    
    if start == None:
        return "Invalid input. there is a cycle" #assume there is no cycle

    while(start in dataSet):
        print (start, " --> ", dataSet[start])
        start = dataSet[start]


dataSet = {}
dataSet["Chennai"] = "Banglore"
dataSet["Bombay"] = "Delhi"
dataSet["Goa"] = "Chennai"
dataSet["Delhi"] = "Goa"
printItinerary(dataSet);
# reverseMap = {}
# for x,y in dataSet.items():
#     reverseMap[y] = x

# print(reverseMap)