#!/usr/bin/python3
"""Lists all cities of a given state (SQL injection safe)."""

import MySQLdb
import sys


def strip_quotes(s):
    """Remove wrapping single/double quotes if present."""
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = strip_quotes(sys.argv[4])

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (state_name,)
    )

    cities = cur.fetchall()
    output = ", ".join([c[0] for c in cities])
    print(output)  # always prints newline, even if output is empty

    cur.close()
    db.close()
