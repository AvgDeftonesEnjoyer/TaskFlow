FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./
COPY src ./src

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

RUN poetry install -vvv
