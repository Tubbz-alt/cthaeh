import pytest

from sqlalchemy import create_engine

from cthaeh.models import Base
from cthaeh.session import Session


@pytest.fixture(scope="session")
def engine():
    # PRO-TIP: Set `echo=True` for lots more SQL debug log output.
    return create_engine('sqlite:///:memory:', echo=False)


@pytest.fixture(scope="session")
def _Session(engine):
    Session.configure(bind=engine)
    return Session


@pytest.fixture(scope="session")
def _schema(engine):
    Base.metadata.create_all(engine)


@pytest.fixture
def session(_Session, _schema):
    session = Session()
    try:
        yield session
    finally:
        session.rollback()
