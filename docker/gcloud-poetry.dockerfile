FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
