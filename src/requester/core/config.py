from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)
    api_key: str | None = None


def get_settings() -> Settings:
    return Settings()


settings = get_settings()
