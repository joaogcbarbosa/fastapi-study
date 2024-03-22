from config import DBConnection
from sqlalchemy.orm import declarative_base

db_conn = DBConnection()
engine = db_conn.get_engine()

Base = declarative_base()
Base.metadata.create_all(bind=engine)
