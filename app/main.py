from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Smart Document Assistant"
)

app.include_router(router)
