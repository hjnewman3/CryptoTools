FROM python:3.6

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 4130:4130

RUN pip install  --no-cache-dir --upgrade -r /api/requirements.txt

COPY . /api
