#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

mysql_user = argv[1]
mysql_password = argv[2]
db_name = argv[3]
"""create a connection to the mysql server"""

db = MySQLdb.connect(host='localhost', port=3306,
                     user=mysql_user, password=mysql_password, db=db_name)

"""create a cursor object for excecuting SQL queries on the database"""
cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'ORDER BY id ASC")
"""retrieves all rows returned by the query and stores them in the num_of_rows variable"""
num_of_rows = cursor.fetchall()
for row in num_of_rows:
    print(row)
