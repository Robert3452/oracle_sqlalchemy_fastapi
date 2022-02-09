from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from sqlalchemy.schema import Sequence
from config.db import meta


addresses = Table("addresses", meta,
                  Column("id", Integer, Sequence("id"), primary_key=True),
                  Column("address", String(255), nullable=False),
                  Column("postal_code", String(255), nullable=True),
                  Column("district", Integer, nullable=False),
                  Column("province", Integer, nullable=False),
                  Column("department", Integer, nullable=False),
                  )
