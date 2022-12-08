FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pandas
RUN pip install re

EXPOSE 80

COPY ./app /app