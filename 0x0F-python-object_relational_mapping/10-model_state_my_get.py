#!/usr/bin/python3
"""
    Script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(mysql_user, mysql_password, mysql_db, state_name):
    """
    Script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa

    Args:
        mysql_user: MySQL username.
        mysql_password: MySQL password.
        mysql_db: MySQL Database name.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_user, mysql_password, mysql_db), pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(
        State.name == state_name
    ).order_by(State.id)

    if query.count() == 0:
        print("Not found")
    else:
        for state in query.all():
            print(state.id)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
