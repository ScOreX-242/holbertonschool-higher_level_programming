#!/usr/bin/python3
"""Lists states starting with N from the database."""


import MySQLdb
import sys

# run only if script is executed directly
if __name__ == "__main__":

    # get MySQL credentials from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # create cursor
    cur = db.cursor()

    # select states starting with 'N', sorted by id
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # print results
    for row in cur.fetchall():
        print(row)

    # close connection
    cur.close()
    db.close()
