#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument."""

import MySQLdb
import sys

db=MySQLdb.connect(host="localhost",port=3306,
        user=sys.argv[1],password=sys.argv[2],db=sys.argv[3])
c=db.cursor()

c.execute("SELECT * FROM states WHERE states.name LIKE BINARY '{}'\
        ORDER BY states.id".format(sys.argv[4]))

for row in c.fetchall()
    print(row)
