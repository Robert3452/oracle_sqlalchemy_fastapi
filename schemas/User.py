from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    names: str
    lastnames: str
    email: str
    password: str
    phone: str


class UserUpdate(BaseModel):
    id: Optional[str]
    names: Optional[str]
    lastnames: Optional[str]
    email: Optional[str]
    password: Optional[str]
    phone: Optional[str]