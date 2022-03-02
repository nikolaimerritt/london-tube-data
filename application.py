import query_database

userQuit = False
while not userQuit:
    userInput = input("Query: ")
    
    if ":" not in userInput:
        userQuit = True
    else:
        print(f"Read input '{userInput}'")
        queryType = userInput.split(":")[0]
        if queryType == "stations":
            lineName = userInput.split(": ")[1]

            for stationName in query_database.readStationsAlongLine(lineName):
                print(f"\tFound station {stationName}")
