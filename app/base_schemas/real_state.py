""" RealState Schema """
from pydantic import BaseModel

class RealStateBase(BaseModel):
    """ RealState data """
    id: int
    square_meter: float
    price: float
    rental_price: float
    search_source: str
    link: str
    n_bedrooms: int
    n_bathrooms: int
    n_kitchens: int
    district: str
    province: str
    number_floor: int
    antiquity: int
    zone_score: int
    state_score: int
    comment: str
    deleted: bool
    comment: str
