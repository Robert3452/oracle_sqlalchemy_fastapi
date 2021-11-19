from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.schema import Sequence
from config.db import meta, engine

users = Table("clients", meta,
              Column("id", Integer, Sequence("id"), primary_key=True),
              Column("name", String(255)),
              Column("email", String(255), unique=True),
              Column("password", String(255)))
# Create the table structure
meta.create_all(engine)
