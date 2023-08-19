#!/usr/bin/python3
"""List states in the databse"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db=MySQLdb.connect(host="localhost",port=3306,user=sys.argv[1],
            password=sys.argv[2],database=sys.argv[3])
    q=db.cursor()
    q.execute("SELECT * FROM states ORDER BY states.id;")
    for each in q.fetchall():
        print(each)
