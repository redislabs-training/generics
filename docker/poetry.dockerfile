FROM python:3
RUN apt-get update && apt-get install -y redis-tools
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -