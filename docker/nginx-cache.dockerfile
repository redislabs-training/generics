FROM nginx:alpine

RUN apk update
RUN apk add python3

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -

COPY . /opt/generics

RUN ln -s /opt/generics/generics/nginx_cache/cache.conf /etc/nginx/conf.d/cache.conf
RUN rm /etc/nginx/conf.d/default.conf

WORKDIR /opt/generics
RUN poetry install

CMD nginx && poetry run cache-tester