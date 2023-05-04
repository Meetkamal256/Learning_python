#!/usr/bin/python3
"""
This script lists all the states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], password=argv[2], port=3306, db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows_selected = db_cursor.fetchall()
    for row in rows_selected:
        print(row)


# from sqlalchemy import create_engine, text

# # create an engine to connect to the database
# engine = create_engine(
#     "mysql+mysqlconnector://{}:{}@localhost:3306/hbtn_0e_0_usa")

# # establish a connection and execute a SELECT statement
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM states"))
#     rows = result.fetchall()
#     for row in rows:
#         print(row)
