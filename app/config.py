from sqlalchemy.engine import URL
from os import environ

from dotenv import load_dotenv

load_dotenv()
if environ.get("TESTING") == "True":
    SQLALCHEMY_DATABASE_URL = URL.create(
        drivername="mysql+pymysql",
        password="Prueba123",
        username="Tester",
        host="localhost",
        port=3307,
        database="tests",
    )

else:
    SQLALCHEMY_DATABASE_URL = URL.create(
        drivername="mysql+pymysql",
        password=environ["MYSQL_PASSWORD"],
        username=environ["MYSQL_USER"],
        host=environ["MYSQL_HOST"],
        port=environ["MYSQL_PORT"],
        database=environ["MYSQL_DATABASE"],
    )

ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
JWT_SECRET_KEY = environ["JWT_SECRET_KEY"]
