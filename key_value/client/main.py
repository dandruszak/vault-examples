import json
import os
from functools import lru_cache

import requests
from fastapi import FastAPI, Depends
from pydantic import BaseSettings


class Settings(BaseSettings):
    server: str
    auth: str

    class Config:
        env_file = os.getenv("ENV_FILE", "config/.env")


app = FastAPI()


@lru_cache
def get_settings():
    return Settings()


@app.get("/call-server")
def main(settings: Settings = Depends(get_settings)):
    headers = {"X-Vault-Auth": settings.auth}
    response = requests.get(f"{settings.server}/api", headers=headers)
    return json.loads(response.text)
