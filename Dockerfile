FROM python:3.11-slim

WORKDIR /app

# копіюємо залежності
COPY pyproject.toml poetry.lock ./

# встановлюємо poetry і залежності
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# копіюємо весь код
COPY . .

# створюємо папку статики і збираємо її
RUN mkdir -p src/staticfiles && \
    python src/manage.py collectstatic --noinput

# запускаємо
CMD ["gunicorn", "src.config.wsgi:application", "--bind", "0.0.0.0:8000"]
