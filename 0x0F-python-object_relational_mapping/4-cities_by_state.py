#!/usr/bin/python3
""" lists all cities from the databas"""

if __name__=="__main__":

    import MySQLdb
    import sys

    db=MySQLdb.connect(host="localhost",port=3306,
            user=sys.argv[1],password=sys.argv[2],db=sys.argv[3])
    c=db.cursor()

    c.execute("SELECT * FROM cities LEFT JOIN states ON cities.state_id=states.id\
            ORDER BY cities.id ASC")

    for row in c.fetchall()
        print(row)
