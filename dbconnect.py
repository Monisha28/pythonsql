import mysql.connector

cnx = mysql.connector.connect(user='monisha', password='monisha',
                              host='34.77.119.137',
                              port=3306,
                              database='monisha')
cnx.close()