import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWeatherRemider.settings')

app = Celery('DjangoWeatherRemider')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_weather_every_one_hour': {
        'task': 'City.tasks.constant_weather_update_every_one_hour',
        'schedule': crontab(hour='*/1')
    },
    'send_email_every_one_hour': {
        'task': 'Sublist.tasks.send_email_every_one_hour',
        'schedule': crontab(hour='*/1')
    },
    'send_email_every_three_hours': {
        'task': 'Sublist.send_email_every_three_hours',
        'schedule': crontab(hour='*/3')
    },
    'send_email_every_six_hours': {
        'task': 'Sublist.send_email_every_six_hours',
        'schedule': crontab(hour='*/6')
    }
}
