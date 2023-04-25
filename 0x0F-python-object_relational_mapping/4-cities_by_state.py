"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
#!/usr/bin/bash
import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]

"""connect to mysql server"""
db = MySQLdb.connect(host='localhost', port=3306,
                     user=mysql_user, password=mysql_password, db=db_name)
"""Create a cursor object for excecuting SQL queries on the database"""
cursor = db.cursor()
"""Excecute SQL query to retrieve the rows in the database"""
cursor.execute(
    "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states\
            ON states.id=cities.state_id\
                ORDER BY cities.id ASC")
"""retrieves all the rows returned by our SQL query and stores them in a variable"""
"""iterate through all the rows and print the result"""
rows = cursor.fetchall()
for row in rows:
    print(row)
