import mysql.connector


def readPassword():
    with open("password.pwd", "r") as f:
        return f.read().strip()


connection = mysql.connector.connect(user="root", password=readPassword(), database="tube_schema")


def createLine(lineName):
    cursor = connection.cursor()
    query = f"INSERT IGNORE INTO Line (line_name) " + \
        f"VALUES (%s)"

    cursor.execute(query, (lineName, ))
    connection.commit()
    cursor.close()


def createStation(stationId, name, latitude, longitude):
    cursor = connection.cursor()
    query = f"INSERT IGNORE INTO Station (station_id, station_name, latitude, longitude) " + \
        f"VALUES (%s, %s, %s, %s)"
    
    cursor.execute(query, (stationId, name, latitude, longitude))
    connection.commit()
    cursor.close()


def createConnection(stationId, lineName):
    cursor = connection.cursor()
    query = f"INSERT IGNORE INTO Connection (station_id, line_name) " + \
        f"VALUES (%s, %s)"
    
    cursor.execute(query, (stationId, lineName))
    connection.commit()
    cursor.close()


def readStationsAlongLine(lineName):
    cursor = connection.cursor()
    stationNameQuery = f"SELECT Station.station_name FROM Station " + \
        f"INNER JOIN Connection ON (Connection.station_id = Station.station_id)" + \
        f"WHERE (Connection.line_name = %s)"
    
    cursor.execute(stationNameQuery, (lineName, ))
    names = []
    for (name, ) in cursor:
        names.append(name)
    
    return names


readStationsAlongLine("District")
# createStation(stationId="940GZZLUTWH", name="Tower Hill", latitude=51.509971, longitude=-0.076546)
# createConnection(stationId="940GZZLUTWH", lineName="District")