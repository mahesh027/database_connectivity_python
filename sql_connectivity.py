import mysql.connector
con= mysql.connector.connect(host="localhost",user="root",password="123456",database="python_db3")

if con:
    print("connected")
else:
    print("connection error")