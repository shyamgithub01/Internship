from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    class Config:
        env_file = "./env"

settings = Settings()