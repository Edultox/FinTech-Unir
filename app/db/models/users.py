from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)


class User(UserBase, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    password: str = Field()


class UserCreate(UserBase):
    password: str


class UserPublic(UserBase):
    id: UUID
