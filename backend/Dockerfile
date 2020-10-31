# pull official base image
FROM python:3.9.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/backend

# create the appropriate directories
RUN mkdir $APP_HOME $APP_HOME/staticfiles $APP_HOME/mediafiles
WORKDIR $APP_HOME

# adding of Pipfiles
ADD ./backend/Pipfile* $APP_HOME/

# Update and install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg libffi-dev openssl-dev \
    && pip install --upgrade pip \
    && pip install --upgrade pipenv \
    && pipenv install --dev --system \
    && apk del build-deps

# copy(add) script
COPY ./backend/scripts/start.sh /

# copy(add) project
ADD ./backend $APP_HOME/
