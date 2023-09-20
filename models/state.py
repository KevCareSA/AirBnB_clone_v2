#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Blueprint for a State Table in the hbnb database

    Attributes <PUBLIC>:
        __tablename__ (str): The name of the MySQL table that tracks states.
        name (sqlalchemy.String): The name of the state
        citites (sqlalchemy.Relationship): The State<->City of cities within
                                           a state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns list of all related City objects."""
            city_ls = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_ls.append(city)
            return city_ls
