from fastapi import FastAPI
from database import engine
from models import Base
import routers
from utils import exception_handler


app = FastAPI(title="API Task manager", docs_url="/")


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


app.add_exception_handler(Exception, exception_handler)


app.include_router(routers.auth_router)
app.include_router(routers.tasks_router)
