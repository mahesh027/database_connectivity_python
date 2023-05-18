import mysql.connector
con= mysql.connector.connect(host="localhost",user="root",password="123456",database="python_db3")

if con:
    print("connected")
else:
    print("connection error")

def insert(name,age,city):
    pass
def update(name,age,city):
    pass
def select():
    pass
def delete(id):
    pass

while True:
    print("1.insert data")
    print("2.Update data")
    print("3.select data")
    print("4.Delete data")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter the name:")
        age=int(input("enter the age:"))
        city=input("enter the city:")
        insert(name,age,city)
    elif choice==2:
        name=input("enter the name")
        age = int(input("enter the age:"))
        city = input("enter the city:")
        update(name, age, city)
    elif choice==3:
        select()
    elif choice==4:
        id=int(input("enter the ID to delete"))
        delete(id)
