# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster AS basic

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

FROM basic AS development
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM basic AS production
CMD ["gunicorn", "-b", "0.0.0.0:8000", "backend.wsgi"]
