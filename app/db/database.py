from sqlmodel import create_engine, SQLModel, Session
from app.db.models.users import User


engine = create_engine("sqlite:///database.db", echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
