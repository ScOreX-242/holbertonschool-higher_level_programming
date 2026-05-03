#!/usr/bin/python3
import MySQLdb
import sys

# run only if script is executed directly
if __name__ == "__main__":

    # get arguments from command line
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

    # create cursor to execute queries
    cur = db.cursor()

    # select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch and print all rows
    for row in cur.fetchall():
        print(row)

    # close cursor and connection
    cur.close()
    db.close()
