import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from fast_curso.app import app
from fast_curso.database import get_session
from fast_curso.models import User, table_registry


@pytest.fixture
def user(session: Session):
    user = User("gabriel", "fjkahsfjdkaslkfdsa", "gabriel@gabi.com")
    session.add(user)
    session.commit()
    session.refresh
    return user


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    # pré teste
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    # Gerênciamento de contexto
    with Session(engine) as session:
        # yield = tranforma a função em gerador
        yield session

    # tierdown
    table_registry.metadata.drop_all(engine)
