#!/usr/bin/python3
""" list all states in database """

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC",(sys.argv[4],))
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
