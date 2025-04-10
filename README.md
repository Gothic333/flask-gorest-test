## Flask GOREST TEST

Flask web application for manipulating data from the gorest.co.in external service via HTTP requests (GET, POST, PATCH, DELETE). University lab work.

### Requirements

- Python >= 3.10

### Usage

Create virtual environment

```bash
python3 -m venv env
```

Install packages using pip and the requirements.txt file.

```bash
pip install -r requirements.txt
```

Set environment variables for Flask CLI (.flaskenv) and app (.env):

| Variable       | Description                                  |
| -------------- | -------------------------------------------- |
| `FLASK_CONFIG` | App configuration (check **config.py**)      |
| `ACCESS_TOKEN` | API-token [gorest.co.in][1]                  |
| `SECRET_KEY`   | Secret key (random bytes or str)             |
| `FLASK_ENV`    | App configuration when startup via FLASK CLI |
| `FLASK_DEBUG`  | Enable debug mode on startup via Flask CLI   |

For start app run this command

```bash
flask run
```

Supported:

- Heroku deploy (Procfile)
- Docker

## Flask GOREST TEST

Веб-приложение на Flask для работы с данными внешнего сервиса gorest.co.in, посредством HTTP-запросов (GET, POST, PATCH, DELETE). Университетская лабораторная работа.

### Требования

- Python >= 3.10

### Использование

Создайте виртуальное окружение:

```bash
python3 -m venv env
```

Установите необходимые модули используя файл requirements.txt:

```bash
pip install -r requirements.txt
```

Настройте переменные окружения для Flask CLI (.flaskenv) и приложения (.env):

| Переменная     | Описание                                            |
| -------------- | --------------------------------------------------- |
| `FLASK_CONFIG` | Конфигурация запуска приложения (См.**config.py**)  |
| `ACCESS_TOKEN` | API-токен [gorest.co.in][1]                         |
| `SECRET_KEY`   | Секретный ключ (случайная строка байт или символов) |
| `FLASK_ENV`    | Конфигурация запуска приложения через Flask CLI     |
| `FLASK_DEBUG`  | Включить отладку при запуске через Flask CLI        |

Для запуска приложения следующую команду:

```bash
flask run
```

Поддержка:

- Деплой на Heroku (Procfile)
- Docker

[1]: https://gorest.co.in/my-account/access-tokens
