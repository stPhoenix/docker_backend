# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /backend

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip3 install pipenv
RUN pipenv install --python 3.8

COPY . .

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:9000"]