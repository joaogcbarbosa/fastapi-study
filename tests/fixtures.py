import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.config.db import get_session
from app.init_db import Base
from app.main import app

load_dotenv()

MSSQL_USER = os.getenv("MSSQL_USER")
MSSQL_PASSWD = os.getenv("MSSQL_PASSWD")
MSSQL_HOST = os.getenv("MSSQL_HOST")
MSSQL_PORT = os.getenv("MSSQL_PORT")
TEST_DB_URL = f"mssql+pymssql://{MSSQL_USER}:{MSSQL_PASSWD}@{MSSQL_HOST}:{MSSQL_PORT}/todos"


test_engine = create_engine(
    TEST_DB_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Base.metadata.create_all(bind=test_engine)


@pytest.fixture(scope="function")
def db_session():
    connection = test_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_session] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def test_user():
    return {"username": "testuser", "password": "testpass"}
