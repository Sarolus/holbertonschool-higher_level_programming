#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def main(mysql_user, mysql_password, mysql_db):
    """
    Script that lists all cities from the database hbtn_0e_4_usa

    Args:
        mysql_user: MySQL username.
        mysql_password: MySQL password.
        mysql_db: MySQL Database name.
    """
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=mysql_user,
                               password=mysql_password,
                               db=mysql_db)

    cursor = database.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states ON\
        cities.state_id = states.id ORDER BY cities.id"
        )

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    database.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
