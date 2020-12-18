import datetime
from env import host 
import mysql.connector

def printtime():
    ct = datetime.datetime.now() 
    return ct

def difftime(e,s):
    return e -s

def sqlquery():
    cnx = mysql.connector.connect(user='monisha', password='monisha',
                                    host= host,
                                    port=3306,
                                    database='monisha')
    cursor = cnx.cursor()
    cursor.execute("select * from student")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    cnx.close()

s = printtime()    
print("Start Time=", s )

sqlquery()

e = printtime()
print("End Time =", e)

print("Query Running Time =",difftime(e,s))




