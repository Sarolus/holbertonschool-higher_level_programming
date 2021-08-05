#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
import sys


def main(mysql_user, mysql_password, mysql_db, state_name):
    """
    Script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument

    Args:
        mysql_user: MySQL username.
        mysql_password: MySQL password.
        mysql_db: MySQL Database name.
        state_name: State name searched.
    """
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=mysql_user,
                               password=mysql_password,
                               db=mysql_db)

    cursor = database.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            state_name
            )
        )

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    database.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
