import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password123.',
)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrm")

print("Database dcrm created successfully")
