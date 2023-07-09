from logging import getLogger
from fastapi import Request, status
from fastapi.responses import JSONResponse
from datetime import datetime


log = getLogger("ErrorLogger")


async def exception_handler(request: Request, ex: Exception):
    log.error(f"-----------------------{ex.__class__.__name__}-----------------------")
    log.error(f"Request URL: {request.url}")
    log.error(f"Request Method: {request.method}")
    log.error(f"{ex}")
    log.error(f"-----------------------{datetime.now()}-----------------------\n")

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": str(ex.args)}
    )
