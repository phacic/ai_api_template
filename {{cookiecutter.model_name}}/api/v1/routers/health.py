from typing import Union

import fastapi
from fastapi import responses

import schemas
from core.config import settings

router = fastapi.APIRouter()


class HealthResponse(responses.JSONResponse):
    media_type = "application/health+json"


@router.get(
    "/health",
    response_model=schemas.HealthOut,
    response_class=HealthResponse,
    responses={500: {"model": schemas.HealthOut}},
)
async def get_health(response: HealthResponse) -> Union[dict[str, str], HealthResponse]:
    response.headers["Cache-Control"] = "max-age=3600"

    return {
        "status": schemas.Status.PASS,
        "version": settings.version,
        "releaseId": settings.releaseId,
    }
