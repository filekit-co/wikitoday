import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import greet, trends
from app.config import get_app_level
from app.logger import setup_logger

app = FastAPI(title='wikitoday.io api server')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [
    greet.router,
    trends.router,
]

for router in routers:
    app.include_router(router)

@app.on_event("startup")
def startup_event():
    app_level = get_app_level()
    setup_logger(app_level)
    logger = logging.getLogger(__name__)
    logger.info("Startup logger successfully")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8080)), log_level="info")