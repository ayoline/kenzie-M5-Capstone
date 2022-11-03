# Dockerfile
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

WORKDIR /code

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]