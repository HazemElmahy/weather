FROM python:3.9-alpine
LABEL maintainer="Hazem Elmahy"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

## For PostgreSQL
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

###  "--no-cahce" flag to not store the registry index in the docker
### file to minize the number of extra packages included in the docker
### container, extra dependencies on the system can cause side effects and 
### can create security vulnerabilities

### "virtual" sets up an alias that we can use to remove them

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /weather
WORKDIR /weather
COPY ./weather /weather

### not using root for security
# RUN adduser -D user
# USER user