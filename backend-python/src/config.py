from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Esta clase define las variables de entorno que se pueden usar en el
    # proyecto y las opciones de configuración
    APP_PORT: int
    APP_HOST: str
    APP_DEBUG: bool
    APP_ENV: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Instancia de la configuración
settings = Settings()
