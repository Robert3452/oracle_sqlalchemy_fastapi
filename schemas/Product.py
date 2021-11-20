from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    image: str
    long_description: str
    enabled: Optional[bool]
