#PROGRAM

import sys
import mysql.connector
from mysql.connector import Error 

#[ADM, NAME, DOB, STREAM]
def createDB():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="tiger")
    mycursor = mydb.cursor()
    mycursor.execute("create database SCHOOL89")
    mydb.commit()
    mycursor.close()
    mydb.close()

    
def createTable():
    mydb=mysql.connector.connect(host="localhost", user="root", password="tiger", database="school89")
    mycursor=mydb.cursor()
    mycursor.execute("create table student(\
                 Adm int(5) primary key,\
                 Name varchar(35),\
                 DOB date, stream varchar(15))")
    #mycursor.commit()
    mycursor.close()
    mydb.close()


def AdmSearch():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='tiger', database='school89')
    cursor=mydb.cursor()
    A=int(input("Enter Adm No to search: "))
    sql="select * from student where adm={}".format(A)
    #sql="select * from student where adm="+str(A)
    cursor.execute(sql)
    for row in cursor:
        print(row)
    cursor.close()
    mydb.close()


def StreamSearch():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='tiger', database='school89')
    cursor=mydb.cursor()
    S=input("Enter Stream to search: ")
    sql="select * from student where stream='{}'".format(S)
    #sql="select * from student where stream="+str('\'')+S+str('\'')
    cursor.execute(sql)
    data=cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    mydb.close()

def YearSearch():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='tiger', database='school89')
    cursor=mydb.cursor()
    sql="select * from student where dob like '2000%'"
    cursor.execute(sql)
    for row in cursor:
        print(row)
    cursor.close()
    mydb.close()


def Insert():
    mydb=mysql.connector.connect(host="localhost", user="root",\
                            passwd="tiger", database="school89")
    cursor=mydb.cursor()
    Adm=int(input("Adm No: "))
    Name=input("Name: ")
    DOB=input("DOB(yyyy-mm-dd): ")
    stream=input("Stream: ")
    sql="insert into student values\
    ({},'{}','{}','{}')".format(Adm, Name, DOB, stream)
    cursor.execute(sql)
    mydb.commit()
    cursor.close()
    mydb.close()


def Delete():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='tiger', database='school89')
    cursor=mydb.cursor()
    A=int(input("Enter Adm No to delete: "))
    sql="delete from student where adm={}".format(A)
    cursor.execute(sql)
    mydb.commit()
    cursor.close()
    mydb.close()


def Modify():
    mydb=mysql.connector.connect(host="localhost", user='root',\
                            passwd='tiger', database='school89')
    cursor=mydb.cursor()
    A=int(input("Enter Adm No to update record: "))
    N=input("Enter correct name: ")
    sql="update student set name='{}' where adm={}".format(N,A)
    cursor.execute(sql)
    mydb.commit()
    cursor.close()
    mydb.close()


def Display():
    try:
        db = mysql.connector.connect(host='localhost',\
                database='school89', user='root', password='tiger')
        if db.is_connected():
            print('Connected to MySQL database')
    except Error as e:
    	print(e)
    	return
    	#sys.exit() ->to kill program execution
    pysql=db.cursor()
    pysql.execute("select * from student")
    data=pysql.fetchall()
    for row in data:
    	print(row)
    pysql.close()
    db.close()


createDB()
createTable()
for i in range(3):
    Insert()
choice=1
while choice!=5:
    print("Enter your choice:-")
    print("1. Search Record")
    print("2. Delete Record")
    print("3. Modify Record")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter your choice:-"))
    if choice==1:
        print('SEARCH PROCESS STARTS NOW:-')
        print('1. Search by Adm No')
        print('2. Search by Stream')
        print('3. Search by Year')
        op=int(input('Enter your choice:-'))
        if op==1:
            AdmSearch()
        elif op==2:
            StreamSearch()
        elif op==3:
            YearSearch()
        else:
            print('Invalid option entered')
    elif choice==2:
        Delete()
    elif choice==3:
        Modify()
    elif choice==4:
        Display()
    else:
        print("Thank you")