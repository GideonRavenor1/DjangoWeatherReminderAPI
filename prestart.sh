sleep 10;
python manage.py migrate --noinput

sleep 10;
python manage.py collectstatic --noinput

sleep 10;
python manage.py runserver 0.0.0.0:8000