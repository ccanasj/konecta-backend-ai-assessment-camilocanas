from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from models import Base


class Task(Base):
    __tablename__ = "tasks"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"{self.title}\nCompleted: {self.completed}"
