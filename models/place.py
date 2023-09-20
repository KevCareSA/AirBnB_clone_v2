#!/usr/bin/python3
"""Defines the Place class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

"""
The association table allows the many-to-many relationship between a place and
it's amenities
"""
association_table = Table(
    "place_amenity", Base.metadata,
    Column(
        "place_id", String(60),
        ForeignKey("places.id"),
        primary_key=True, nullable=False
           ),
    Column(
        "amenity_id", String(60),
        ForeignKey("amenities.id"),
        primary_key=True, nullable=False
           )
    )


class Place(BaseModel, Base):
    """Blueprint for a Place Table in the hbnb database

    Attributes <PUBLIC>:
        __tablename__ (str): The name of the MySQL table that tracks reviews.
        name (sqlalchemy.String): The name of the place
        description (sqlalchemy.String): The description of place
        city_id (sqlalchemy.String): A Foreign key reference to city id's
        user_id (sqlalchemy.String): A Foreign key reference to user id's
        number_rooms (sqlalchemy.Integer): Number of rooms in place
        number_bathrooms (sqlalchemy.Integer): Number of bathrooms in place
        max_guest (sqlalchemy.Integer): max guests allowed in place
        price_by_night (sqlalchemy.Integer): cost of staying the night
        latitude (sqlalchemy.Float): latitudinal position of a place
        longitude (sqlalchemy.Float): longitudinal position of a place
        reviews (sqlalchemy.Relationship): reviews related to a place
        amenities (sqlalchemy.Relationship): amenities related to a place
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, overlaps='place_amenities')
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """returns a list of all linked Reviews."""
            rev_ls = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    rev_ls.append(review)
            return rev_ls

        @property
        def amenities(self):
            """get list of amenities objects"""
            amenity_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """append amneity id's"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
