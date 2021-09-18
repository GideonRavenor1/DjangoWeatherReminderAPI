#!/usr/bin/env bash

python manage.py makemigrations --noinput

sleep  5;
python manage.py migrate --noinput

sleep  5;
python manage.py collectstatic --noinput

sleep  5;
python manage.py runserver 0.0.0.0:8000
# gunicorn DjangoWeatherRemider.wsgi:application --bind 0.0.0.0:8000 --reload -w 4