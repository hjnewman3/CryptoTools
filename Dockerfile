FROM python:3.6

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 4130:4130

RUN pip install  --no-cache-dir --upgrade -r /api/requirements.txt

COPY . /api

# RUN uvicorn src.app:app --host 0.0.0.0 --port 4130
# CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "4130"]