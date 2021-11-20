from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import CHAR, Float, Integer, String, Text
from sqlalchemy.schema import Sequence
from config.db import meta

products = Table("products", meta,
              Column("id", Integer, Sequence("id"), primary_key=True),
              Column("name", String(255)),
              Column("description", String(255)),
              Column("price", Float()),
              Column("stock", Integer()),
              Column("image", String(255)),
              Column("long_description", Text()),
              Column("enabled", CHAR(1))
              )
