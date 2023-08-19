#!/usr/bin/python3
"""lists all cities of that state,"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    c.execute("SELECT cities.name FROM cities LEFT JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = c.fetchall()

    print(", ".join([row[0] for row in rows]))
    c.close()
    db.close()
