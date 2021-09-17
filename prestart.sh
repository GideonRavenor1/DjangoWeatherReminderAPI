#!/usr/bin/env bash

sleep 5;
python manage.py migrate

sleep 5;
python manage.py makemigrations

sleep 5;
python manage.py collectstatic

sleep 5;
python manage.py runserver 0.0.0.0:8000
