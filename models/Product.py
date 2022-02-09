from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import CHAR, Float, Integer, String, Text
from sqlalchemy.schema import Sequence, Identity
from sqlalchemy.ext.declarative import declarative_base
from config.db import meta

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, Sequence("id"), primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float())
    stock = Column(Integer())
    image = Column(String(255))
    long_description = Column(Text())
    enabled = Column(CHAR(1))
#
# products = Table("products", meta,
#                  Column("id", Integer, Sequence("id"), primary_key=True),
#                  Column("name", String(255)),
#                  Column("description", String(255)),
#                  Column("price", Float()),
#                  Column("stock", Integer()),
#                  Column("image", String(255)),
#                  Column("long_description", Text()),
#                  Column("enabled", CHAR(1)),
#                  )
