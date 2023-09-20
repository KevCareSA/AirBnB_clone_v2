#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Blueprint for a Review Table in the hbnb database

    Attributes <PUBLIC>:
        __tablename__ (str): The name of the MySQL table that tracks reviews.
        text (sqlalchemy.String): The name of the state
        place_id (sqlalchemy.String): A Foreign key reference to place id's
        user_id (sqlalchemy.String): A Foreign key reference to users id's
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
