#!/usr/bin/env python3
"""
a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]
state_name = sys.argv[4]

"""connect to the mysql server"""
db = MySQLdb.connect(
    host="localhost", port=3306, user=mysql_user, password=mysql_password, db=db_name
)

"""create a cursor object for excecuting SQL queries on the database"""
cursor = db.cursor()

"""excecute SQL query to retrieve all rows in our database"""
cursor.execute(
    "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
)

"""retrieves all the rows returned by our queries and stores them in a variable called rows"""
rows = cursor.fetchall()

"""iterate through all the rows returned by our query and print them out"""
for row in rows:
    print(row)
