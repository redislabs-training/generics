FROM google/cloud-sdk:slim

RUN apt update
RUN apt install -y jq gettext-base
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
