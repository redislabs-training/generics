
FROM openresty/openresty

RUN apt update
RUN apt install -y curl python3 python3-pip python3-venv redis-tools

## the "official" ways of installing poetry don't work well in this context for some reason
RUN pip3 install poetry 

COPY . /opt/generics

RUN ln -s /opt/generics/generics/nginx_cache/cache.conf /etc/nginx/conf.d/cache.conf
RUN rm /etc/nginx/conf.d/default.conf

WORKDIR /opt/generics
RUN poetry install

CMD nginx && poetry run cache-tester