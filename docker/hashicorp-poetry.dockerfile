FROM ubuntu

## Terraform/Packer
ENV DEBIAN_FRONTEND='noninteractive'
RUN apt update
RUN apt-get install -y curl gnupg2 lsb-core software-properties-common
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
RUN apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
RUN apt-get update 
RUN apt-get install -y packer terraform ansible

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -