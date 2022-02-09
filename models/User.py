from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.schema import Sequence
from sqlalchemy.ext.declarative import declarative_base
from config.db import meta
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("id"), primary_key=True)
    names = Column(String(255))
    lastnames = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    phone = Column(String(255))

# users = Table("clients", meta,
#               Column("id", Integer, Sequence("id"), primary_key=True),
#               Column("name", String(255)),
#               Column("email", String(255), unique=True),
#               Column("password", String(255), ))
