# Étape de construction de l'application
FROM python:3.6-slim
ARG GEOCODING_API_KEY
ARG DB_DATABASE
ARG DB_USER
ARG DB_PASSWD
ARG DB_HOST

ENV GEOCODING_API_KEY=$GEOCODING_API_KEY
ENV DB_DATABASE=$DB_DATABASE
ENV DB_USER=$DB_USER
ENV DB_PASSWD=$DB_PASSWD
ENV DB_HOST=$DB_HOST
COPY . /srv/flask_app
WORKDIR /srv/flask_app

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --src /usr/local/src

COPY build/nginx.conf /etc/nginx
RUN chmod +x ./buidl/start.sh

CMD ["./build/start.sh"]