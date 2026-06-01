"""Configuration management using Pydantic Settings."""

from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration settings."""

    APP_NAME: str = "Purplle Shrinkage Detection"
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite:///./data/events.db"
    YOLO_MODEL_PATH: str = "models/yolov8n.pt"
    LOG_LEVEL: str = "INFO"

    class Config:
        """Pydantic config."""

        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
