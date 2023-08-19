#!/usr/bin/python3
"""lists all states with a name starting with N"""

import MySQLdb
import sys

db=MySQLdb.connect(host="localhost",port=3306,user=sys.argv[1],
        password=sys.argv[2],db=sys.argv[3])
c=db.cursor()
c.execute("SELECT * FROM states WHERE states.name
        LIKE N% ORDER BY states.name;")
for row in c.fetchall():
    print(row)
