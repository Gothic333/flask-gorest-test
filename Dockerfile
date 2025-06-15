FROM python:3.13.3-alpine3.21


ENV APP_HOME=/app \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR $APP_HOME

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del .build-deps

COPY . .

EXPOSE 8000
