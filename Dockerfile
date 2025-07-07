FROM python:3.11-slim

WORKDIR /app

# копіюємо залежності
COPY pyproject.toml poetry.lock ./

# ставимо poetry і встановлюємо пакети
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# копіюємо увесь проєктний код
COPY . .

# збираємо статику після повної копії
RUN python src/manage.py collectstatic --noinput

# запускаємо
CMD ["gunicorn", "src.config.wsgi:application", "--bind", "0.0.0.0:8000"]
