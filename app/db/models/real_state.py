""" RealState model """
from sqlalchemy import Boolean, Column, String, Integer, DECIMAL
from app.db.base import BasePsql
from app.db.mixins.timestamp_mixin import TimestampMixin

class RealState(BasePsql, TimestampMixin):
    """ The real states table """
    __tablename__ = 'real_states'
    id = Column(Integer, primary_key=True)
    square_meter = Column(DECIMAL(20, 2, asdecimal=False), nullable=True)
    price = Column(DECIMAL(20, 2, asdecimal=False), nullable=True)
    rental_price = Column(DECIMAL(20, 2, asdecimal=False), nullable=True)
    search_source = Column(String, nullable=True)
    link = Column(String, nullable=True)
    n_bedrooms = Column(Integer, nullable=True)
    n_bathrooms = Column(Integer, nullable=True)
    n_kitchens = Column(Integer, nullable=True)
    district = Column(String, nullable=True)
    province = Column(String, nullable=True)
    number_floor = Column(Integer, nullable=True)
    antiquity = Column(Integer, nullable=True)
    zone_score = Column(Integer, nullable=True)
    state_score = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)
    deleted = Column(Boolean, default=False)
