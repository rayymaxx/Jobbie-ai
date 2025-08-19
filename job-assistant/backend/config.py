from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Global config for backend
    PROJECT_NAME: str = "Job Assistant API"
    API_VERSION: str = "v1"
    DEBUG: bool = True

    class Config:
        env_file=".env"

settings  = Settings