import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'nurikshurik1'

)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE gmed")

print("Done!")