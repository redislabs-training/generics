FROM google/cloud-sdk:slim

RUN apt update
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
