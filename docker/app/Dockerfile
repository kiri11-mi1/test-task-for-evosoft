FROM python:3.9.4-slim

RUN mkdir /src && apt-get update && apt-get install -y git libpq-dev postgresql-client
WORKDIR /src

COPY ./src/pyproject.toml /src/
COPY ./src/poetry.lock /src/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./src /src
