FROM python:3.9-alpine

LABEL maintainer="github.com/hirakhax"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./ ./

RUN apk add --no-cache postgresql-client && \
    apk add --no-cache --virtual .tmp_build_deps \
    build-base postgresql-dev musl-dev && \
    pip install -r /app/requirements.txt && \
    apk del .tmp_build_deps && \
    adduser --disabled-password --no-create-home djangouser 

USER djangouser

EXPOSE 8000
