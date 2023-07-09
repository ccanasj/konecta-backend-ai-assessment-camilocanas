from pydantic import BaseModel, Field
from .task import ShowTaskSchema


class BaseUserSchema(BaseModel):
    username: str


class UserSchema(BaseUserSchema):
    password: str = Field(..., min_length=8, max_length=32)

    class Config:
        schema_extra = {
            "examples": [
                {
                    "username": "user",
                    "password": "secret password",
                }
            ]
        }


class ShowUserSchema(BaseUserSchema):
    id: int

    tasks: list[ShowTaskSchema]

    class Config:
        orm_mode = True
