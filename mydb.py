import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Amit#2003'

)

#prepare a cursor object
cursorObject=dataBase.cursor()

#Create a database
cursorObject.execute('CREATE DATABASE crmdatabase')

print('All Done!')