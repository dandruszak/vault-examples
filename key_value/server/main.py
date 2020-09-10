from typing import Optional

from fastapi import FastAPI, Header, Response

app = FastAPI()


@app.get("/api")
def main(response: Response, x_vault_auth: Optional[str] = Header(None)):
    if x_vault_auth == "secret":
        return {"message": "ok"}

    response.status_code = 401
    return {"message": "unauthorized"}
