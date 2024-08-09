from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_curso.models import User, table_registry


def test_create_user_db(session):
    # sqlite criado em memória para testagem
    engine = create_engine("sqlite:///:memory:")
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username="dunossauro", email="duno@sauro.com", password="31324664"
        )
        session.add(user)
        session.commit()

        # ele encontra o objeto python através de uma query
        result = session.scalar(
            # select com where
            select(User).where(User.email == "duno@sauro.com")
        )

        # session.refresh(user)

        assert user.id == 1
        assert result.username == "dunossauro"
