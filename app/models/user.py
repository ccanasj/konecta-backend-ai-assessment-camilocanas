from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import Base

from utils import hash_password


class User(Base):
    __tablename__ = "users"

    username = Column(String(128), unique=True, nullable=False)
    password = Column(String(256), nullable=False)

    tasks = relationship("Task")

    def pre_add(self, item: dict) -> None:
        self.password = hash_password(self.password)

    def __repr__(self) -> str:
        return f"{self.username}"
