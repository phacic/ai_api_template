import pydantic


class MLModelNotFoundError(pydantic.BaseModel):
    detail: str = "ML model not found"
