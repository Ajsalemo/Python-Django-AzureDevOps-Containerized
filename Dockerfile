FROM python:3.9-slim

WORKDIR /app

COPY . /app/
RUN apt-get update -yy \
    && apt-get upgrade -yy \
    && apt-get install gcc libpq-dev python3-dev -yy \
    && pip install -r requirements.txt \
    && python manage.py collectstatic

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--chdir", "/app", "unsplash.wsgi", "--timeout", "600" ]

