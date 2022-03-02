import mysql.connector


def readPassword():
    with open("password.pwd", "r") as f:
        return f.read().strip()


connection = mysql.connector.connect(user="root", password=readPassword(), database="tube_schema")


def createLine(lineName):
    cursor = connection.cursor()
    query = f"INSERT IGNORE INTO Line (line_name) " + \
        f"VALUES ('{lineName}')"

    cursor.execute(query)
    connection.commit()
    cursor.close()


def createStation(stationId, name, latitude, longitude):
    cursor = connection.cursor()
    query = f"INSERT IGNORE INTO Station (station_id, station_name, latitude, longitude) " + \
        f"VALUES ('{stationId}', '{name}', {latitude}, {longitude})"
    
    cursor.execute(query)
    connection.commit()
    cursor.close()


def createConnection(stationId, lineName):
    cursor = connection.cursor()
    query = f"INSERT IGNORE INTO Connection (station_id, line_name) " + \
        f"VALUES ('{stationId}', '{lineName}')"
    
    cursor.execute(query)
    connection.commit()
    cursor.close()


# createLine(lineName="District")
# createStation(stationId="940GZZLUTWH", name="Tower Hill", latitude=51.509971, longitude=-0.076546)
# createConnection(stationId="940GZZLUTWH", lineName="District")