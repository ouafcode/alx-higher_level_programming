#!/usr/bin/python3
""" Create class State """

import MySQLdb
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


db = MySQLdb.connect(host='localhost', port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
