#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""
    
    __tablename__ = "places"
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place")
        
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            back_populates="place_amenities",
        )
    
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        
        @property
        def reviews(self):
            """
            returns list of review instance with place_id
            equals to the current place.id
            """
            from models import storage
            from models.review import Review
            
            obj = storage.all()
            lst = list(obj)
            new = []
            
            for i in lst:
                if "Review" in i:
                    temp = Review(obj[i])
                    if temp.place_id == self.id:
                        new.append(temp)
                        
    # @property
    # def reviews(self):
    #     """
    #     Returns a list of review instances associated with the current place.
    #     """
    #     from models import storage
    #     from models.review import Review
    
    #     reviews_dict = storage.get(Review, place_id=self.id)
    #     return list(reviews_dict.values()) if reviews_dict else []

