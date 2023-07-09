from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Task, User
from schemas import ShowTaskSchema, TaskSchema, BaseResponse
from database import get_db
from .dependencies.current_user import get_current_user


tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])


@tasks_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowTaskSchema],
)
async def get_tasks(current_user: User = Depends(get_current_user)):
    return current_user.tasks


@tasks_router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowTaskSchema,
)
async def get(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = Task.filter_first(db, Task.id == id, Task.user_id == current_user.id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task not found",
        )
    return task


@tasks_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowTaskSchema,
)
async def create(
    body: TaskSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = body.dict()
    task["user_id"] = current_user.id
    return Task.create(db, task)


@tasks_router.delete(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=BaseResponse,
)
async def delete(
    id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = Task.filter_first(db, Task.id == id, Task.user_id == current_user.id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task not found",
        )
    return Task.delete(db, id)


@tasks_router.put(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ShowTaskSchema,
)
async def update(
    id: str,
    body: TaskSchema,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = Task.filter_first(db, Task.id == id, Task.user_id == current_user.id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task not found",
        )
    body = body.dict(exclude_unset=True)

    return Task.update(db, id, body)


@tasks_router.post(
    "/bulk",
    status_code=status.HTTP_201_CREATED,
    response_model=list[ShowTaskSchema],
)
async def bulk(
    body: list[TaskSchema],
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    tasks = []
    for task in body:
        task = task.dict()
        task["user_id"] = current_user.id
        tasks.append(task)

    return Task.bulk(db, tasks)
