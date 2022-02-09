from sqlalchemy import create_engine, MetaData
import cx_Oracle
from env_config import Settings
from sqlalchemy.orm import sessionmaker

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

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

conn = engine.connect()
meta = MetaData()


def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
