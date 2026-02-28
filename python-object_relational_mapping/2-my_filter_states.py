#!/usr/bin/python3
"""Lists all states matching user input (vulnerable to injection)"""

import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
