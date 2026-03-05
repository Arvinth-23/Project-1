from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    openai_api_key: str = ""
    gemini_api_key: str
    database_url: str
    secret_key: str

    model_config = SettingsConfigDict(        env_file=str(Path(__file__).parent.parent / ".env"),
        env_file_encoding="utf-8"
    )

settings = Settings()