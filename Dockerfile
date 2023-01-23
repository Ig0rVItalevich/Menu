FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get -y install postgresql-client

COPY wait-for-postgres.sh wait-for-postgres.sh

RUN chmod +x wait-for-postgres.sh

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY ./app ./app
