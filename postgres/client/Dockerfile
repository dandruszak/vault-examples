FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt .
RUN pip install --upgrade pip wheel && pip install -r requirements.txt

COPY ./main.py /app
COPY ./.env.ctmpl /app/template/