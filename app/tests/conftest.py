from models import Base, User
from database import Session, engine
import pytest
import os


def pytest_sessionstart(session):
    if not os.getenv("TESTING") == "True":
        return pytest.exit(
            "Test environment not set correctly, set the 'TESTING' environment variable to 'True'"
        )


@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(engine)

    session = Session()

    User.create(
        session, {"id": 1, "username": "User tester", "password": "123456789"}
    )

    yield session

    session.close()
    Base.metadata.drop_all(engine)
