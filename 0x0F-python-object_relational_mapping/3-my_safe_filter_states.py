#!/usr/bin/python3
""" 
a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]
state_name = sys.argv[4]

"""connect to mysql server"""
db = MySQLdb.connect(
    host="localhost", port=3306, user=mysql_user, password=mysql_password, db=db_name
)
"""create a cursor object for excecuting SQL queries on the database"""
cursor = db.cursor()

"""excecute the SQL query to retrieve all rows in the database the %s in code serve as a placeholder which protects against SQL injection attacks"""
cursor.execute("SELECT *FROM states WHERE name= %s", (sys.argv[4],))

"""retrieves all the rows returned by our SQL query and stores them in a variable"""
row = cursor.fetchall()
"""iterate through each row in our query and print them out"""
for rows in row:
    print(row)
