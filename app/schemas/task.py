from pydantic import BaseModel, Field
from typing import Optional


class TaskSchema(BaseModel):
    title: str = Field(..., max_length=256)
    description: str
    completed: Optional[bool] = False


class ShowTaskSchema(TaskSchema):
    id: int

    class Config(TaskSchema.Config):
        orm_mode = True
