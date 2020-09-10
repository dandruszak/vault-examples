import os

import psycopg2
from fastapi import FastAPI, Depends
from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    port: str
    username: str
    password: str
    dbname: str

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")


app = FastAPI()


def get_settings():
    return Settings()


@app.get("/database")
def main(settings: Settings = Depends(get_settings)):
    try:
        conn = psycopg2.connect(host=settings.host,
                                port=settings.port,
                                user=settings.username,
                                password=settings.password,
                                dbname=settings.dbname)
    except psycopg2.OperationalError:
        return {"message": "connection failed"}

    cur = conn.cursor()
    cur.execute("SELECT 1")
    cur.fetchone()
    cur.close()
    conn.close()

    return {"message": "ok"}
