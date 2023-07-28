from datetime import datetime

from fastapi import APIRouter, Request, status

router = APIRouter()

@router.get("/")
async def greet(request: Request):
    current_time = datetime.utcnow()
    return {'message':f"LLM API Server 🤖(UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"}


@router.get("/ping", status_code=status.HTTP_200_OK)
async def pong():
    return {"ping": "pong!"}

