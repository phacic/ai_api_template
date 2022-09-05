from api.v1.routers import health
from core.config import settings
from fastapi import FastAPI, responses

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.releaseId,
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


@app.on_event("startup")
async def init_models() -> None:
    """
    initialize models on app startup if needed
    """
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", debug=True, reload=True)
