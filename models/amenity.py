#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Blueprint for a Review Table in the hbnb database

    Attributes <PUBLIC>:
        __tablename__ (str): The name of the MySQL table that tracks Amenities.
        name (sqlalchemy.String): The name of the city
        places_amenities (sqlalchemy.Relationship): Entails many-to-many
        relationship with a place
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False, overlaps='place_amenities')
