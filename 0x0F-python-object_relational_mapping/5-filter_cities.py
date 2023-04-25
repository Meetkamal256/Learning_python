#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]
states_name = sys.argv[4]

"""connect to MYSQL server"""
db = MySQLdb.connect(host='localhost', port=3306,
                     user=mysql_user, password=mysql_password, db=db_name)
"""create a cursor object to execute queries in the database"""
cursor = db.cursor()
cursor.execute(
    "SELECT cities.id, states.name, cities.name\
        FROM cities\
            INNER JOIN states\
                ON states.id=cities.state_id\
                    WHERE states.name= %s ORDER BY cities.id ASC", (sys.argv[4],))
rows = cursor.fetchall()
for row in rows:
    print(row)
