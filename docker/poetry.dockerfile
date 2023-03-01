FROM python:3
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -