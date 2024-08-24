import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mwangi@2024',
)
cursorobject = database.cursor()

cursorobject.execute("create database school_records")

print("all done")
