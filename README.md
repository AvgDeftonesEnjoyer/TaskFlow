askFlow Project

TaskFlow — це вебзастосунок для управління завданнями (тасками), створений на базі Django та Django REST Framework. Він поєднує класичні HTML-інтерфейси та REST API для інтеграції.

Функціонал

    CRUD-операції для завдань

    Фільтрація за статусом і пріоритетом

    REST API для взаємодії із зовнішніми сервісами

    Swagger / Redoc для документації API

    JWT-аутентифікація через SimpleJWT

    PostgreSQL як база даних

    Docker / Docker Compose для швидкого запуску

    Unit-тести для HTML-інтерфейсів

Технології

    Python 3.11

    Django

    Django REST Framework

    drf-yasg (Swagger/Redoc)

    PostgreSQL

    Docker / Docker Compose

Запуск проекту

    1️⃣ Клонування репозиторію

    git clone https://github.com/AvgDeftonesEnjoyer/TaskFlow.git
    cd taskflow

    2️⃣ Запуск через Docker Compose

    docker-compose up --build

    Доступ до сервісів

    бекенд: http://localhost:8000

    Swagger: http://localhost:8000/swagger/

    Redoc: http://localhost:8000/redoc/

.env приклад

    DEBUG=True
    SECRET_KEY=your_super_secret_key
    ALLOWED_HOSTS=127.0.0.1,localhost

    DB_NAME=taskflow_db
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432

API документація

    Swagger: http://localhost:8000/swagger/

    Redoc: http://localhost:8000/redoc/

Структура проекту

    taskflow/
    │
    ├── src/
    │   ├── config/
    │   └── taskflowapp/
    │       ├── models.py
    │       ├── serializers.py
    │       ├── views.py
    │       ├── templates/
    │       └── tests_views.py
    │
    ├── dockerfile
    ├── docker-compose.yml
    └── .env