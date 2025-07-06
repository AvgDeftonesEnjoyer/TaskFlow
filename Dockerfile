FROM python:3.11-slim

WORKDIR /app

# копіюємо залежності
COPY pyproject.toml poetry.lock README.md ./

# встановлюємо poetry і залежності
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# копіюємо весь код
COPY src ./src

# запускаємо
CMD ["gunicorn", "src.config.wsgi:application", "--bind", "0.0.0.0:8000"]
