# Python version
[![Python Version](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)

# ER диаграмма БД
![ER](ER.png)

# Клонирование репозитория
`git clone https://github.com/fvhr/rinhhack_project`

# Создайте файл ./backend/.env
```
ALLOWED_HOSTS=127.0.0.1,0.0.0.0,localhost
SECRET_KEY=django-insecure-

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

# Запуск
`docker-compose up --build -d`
