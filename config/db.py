from sqlalchemy import create_engine, MetaData
import cx_Oracle
from env_config import Settings

settings = Settings()

host = settings.ORACLEDB_HOST
port = settings.ORACLEDB_PORT
user = settings.ORACLEDB_USER
sid = settings.ORACLEDB_SID
password = settings.ORACLEDB_PASSWORD
sid = cx_Oracle.makedsn(host, port, sid=sid)

db_connection = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

engine = create_engine(db_connection)
conn = engine.connect()
meta = MetaData()
