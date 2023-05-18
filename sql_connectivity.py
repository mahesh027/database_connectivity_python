from tabulate import tabulate  #to print data neatly in a table
import mysql.connector
con= mysql.connector.connect(host="localhost",user="root",password="123456",database="python_db3")

if con:
    print("connected")
else:
    print("connection error")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into student (name,age,city) values (%s,%s,%s)"
    stud=(name,age,city)
    res.execute(sql,stud)
    con.commit()
    print("data inserted")

def update(name,age,city,id):
    res = con.cursor()
    sql = "update student set name=%s,age=%s,city=%s where id=%s"
    stud = (name, age, city, id)
    res.execute(sql,stud)
    con.commit()
    print("data updated")

def select():
    res=con.cursor()  #cursor is used  to connect python and mysql
    sql="select ID,NAME,AGE,CITY from student "
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def delete(id):
    res = con.cursor()
    sql = "delete from student where id=%s"
    stud = (id,) #tuple
    res.execute(sql,stud)
    con.commit()
    print("data delete")

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
        id=int(input("enter id:"))
        name=input("enter the name")
        age = int(input("enter the age:"))
        city = input("enter the city:")
        update(name, age, city,id)
    elif choice==3:
        select()
    elif choice==4:
        id=int(input("enter the ID to delete"))
        delete(id)
    elif choice==5:
        quit()
    else:
        print("invalid selection")

