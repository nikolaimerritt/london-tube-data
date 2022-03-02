import query_database
import json


def readJson():
    filename = "train-network.json"
    with open(filename, "r") as file:
        return json.load(file)


def populateStations(stations):
    for station in stations:
        id = station["id"]
        name = station["name"]
        latitude = float(station["latitude"])
        longitude = float(station["longitude"])
        query_database.createStation(id, name, latitude, longitude)



def populateLines(lines):
    for line in lines:
        lineName = line["name"]
        query_database.createLine(lineName)
        for stationId in line["stations"]:
            query_database.createConnection(stationId, lineName)



jsonRead = readJson()
stations = jsonRead["stations"]
lines = jsonRead["lines"]

query_database.createLine("Circle")
populateStations(stations)
populateLines(lines)