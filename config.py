from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    API_YANDEX_WEATHER_TOKEN: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_HOST: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()