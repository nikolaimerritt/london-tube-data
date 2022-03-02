import query_database

delim = ": "
userQuit = False
while not userQuit:
    userInput = input("Query: ")
    
    if ":" not in userInput:
        userQuit = True
    else:
        queryType = userInput.split(delim)[0]
        if queryType == "stations":
            lineName = userInput.split(delim)[1]

            for stationName in query_database.readStationsAlongLine(lineName):
                print(f"\tFound station {stationName}")
