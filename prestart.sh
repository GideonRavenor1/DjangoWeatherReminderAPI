sleep 10;
python manage.py migrate

sleep 10;
python manage.py collectstatic

sleep 10;
python manage.py runserver 0.0.0.0:8000