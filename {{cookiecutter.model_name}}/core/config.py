from pathlib import Path

import pydantic


class Settings(pydantic.BaseSettings):
    version: str = "1.0"
    releaseId: str = "1.1"
    APP_NAME: str = "{{cookiecutter.model_name}}"
    API_V1_STR: str = "/api/v1"
    BASE_DIR: str = str(Path(__file__).parent.parent)


settings = Settings()
