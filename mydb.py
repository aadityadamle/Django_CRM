# pip install mysql
# pip install mysql connector
# OR pip install mysql connector python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass12345'

)

#prepare a cursor object
curObj = dataBase.cursor()

#Create a db
curObj.execute("CREATE DATABASE crm_data")

print("CRM Database created!")