FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
COPY README.md ./
COPY .env .env

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .

ENV PYTHONPATH="/app"

EXPOSE 8000

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]

