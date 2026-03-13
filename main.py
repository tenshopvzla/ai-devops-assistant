from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="AI DevOps Assistant API",
    description="Training project for FastAPI and service-layer architecture.",
    version="1.0.0",
)

app.include_router(router)


    