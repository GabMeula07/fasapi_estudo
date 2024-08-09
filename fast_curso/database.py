from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_curso.settings import Setting

engine = create_engine(Setting().DATABASE_URL)


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session
