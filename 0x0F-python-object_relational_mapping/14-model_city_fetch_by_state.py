#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    for c, s in session.query(City, State)\
                       .order_by(City.id)\
                       .filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
