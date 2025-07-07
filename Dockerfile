FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY src ./src

RUN python src/manage.py collectstatic --noinput

CMD ["gunicorn", "src.config.wsgi:application", "--bind", "0.0.0.0:8000"]
