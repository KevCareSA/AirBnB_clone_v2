#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Blueprint for a Review Table in the hbnb database

    Attributes <PUBLIC>:
        __tablename__ (str): The name of the MySQL table that tracks cities.
        name (sqlalchemy.String): The name of the city
        state_id (sqlalchemy.String): A Foreign key reference to city id's
        places (sqlalchemy.Relationship): Entails the Place<->City relationship
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
