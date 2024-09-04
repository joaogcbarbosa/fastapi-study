from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from app.init_db import Base
from app.config.db import DBConnection


load_dotenv()

MSSQL_USER=os.getenv("MSSQL_USER")
MSSQL_PASSWD=os.getenv("MSSQL_PASSWD")
MSSQL_HOST=os.getenv("MSSQL_HOST")
MSSQL_PORT=os.getenv("MSSQL_PORT")
TEST_DB_URL = f"mssql+pymssql://{MSSQL_USER}:{MSSQL_PASSWD}@{MSSQL_HOST}:{MSSQL_PORT}/todos"


test_engine = create_engine(
    TEST_DB_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


Base.metadata.create_all(bind=test_engine)


def override_get_session():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[DBConnection().get_session] = override_get_session

test_client = TestClient(app=app, base_url="http://0.0.0.0:3000")
