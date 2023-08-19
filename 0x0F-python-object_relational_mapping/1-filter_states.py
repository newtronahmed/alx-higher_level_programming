#!/usr/bin/python3
"""lists all states with a name starting with N"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db=MySQLdb.connect(host="localhost",port=3306,user=sys.argv[1],
            password=sys.argv[2],db=sys.argv[3])
    c=db.cursor()
    c.execute("""SELECT * FROM states WHERE name
            LIKE BINARY 'N%' ORDER BY states.id ASC""")
    for row in c.fetchall():
        print(row)
