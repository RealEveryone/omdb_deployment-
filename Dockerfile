FROM python:3.10

RUN apt update -y \
    && apt upgrade -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web


WORKDIR $APP_HOME

RUN pip install --upgrade pip
COPY requirements.txt ./open_movie_data_base
RUN pip install -r requirements.txt
COPY . .
