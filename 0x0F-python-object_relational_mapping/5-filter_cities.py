#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def main(mysql_user, mysql_password, mysql_db, state_name):
    """
    Script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa

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
        "SELECT c.name\
        FROM cities c INNER JOIN states s ON\
        c.state_id = s.id WHERE s.name = %s\
        ORDER BY c.id ASC", (state_name, )
        )

    results = cursor.fetchall()

    print(", ".join([element[0] for element in results]))

    cursor.close()
    database.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
