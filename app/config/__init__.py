from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///weather.db"
    app_name: str = "weather_plus"

settings = Settings()