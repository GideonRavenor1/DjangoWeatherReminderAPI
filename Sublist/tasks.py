from DjangoWeatherRemider.celery import app
from .models import SubListApp
from django.core.mail import EmailMessage, get_connection
from django.template.loader import render_to_string
from User.models import UserApp
from City.models import CityApp
from Weather.models import WeatherApp


@app.task
def send_email_every_one_hour():
    subscriptions = SubListApp.objects.filter(send_email=1)
    if not subscriptions:
        return 'Subscriptions not found'
    user_city_list = [[subscription.user_id.pk, subscription.city_id.pk] for subscription in subscriptions]
    print(user_city_list)
    send_email.delay(user_city_list)
    return 'Successfully'


@app.task
def send_email_every_three_hours():
    subscriptions = SubListApp.objects.filter(send_email=3)
    if not subscriptions:
        return 'Subscriptions not found'
    user_city_list = [[subscription.user_id.pk, subscription.city_id.pk] for subscription in subscriptions]
    print(user_city_list)
    send_email.delay(user_city_list)
    return 'Successfully'


@app.task
def send_email_every_six_hours():
    subscriptions = SubListApp.objects.filter(send_email=6)
    if not subscriptions:
        return 'Subscriptions not found'
    user_city_list = [[subscription.user_id.pk, subscription.city_id.pk] for subscription in subscriptions]
    print(user_city_list)
    send_email.delay(user_city_list)
    return 'Successfully'


@app.task
def send_email(user_city_list):
    con = get_connection()
    con.open()
    email_list = []
    for element in user_city_list:
        weather = WeatherApp.objects.get(city=element[1])
        user = UserApp.objects.get(pk=element[0])
        city = CityApp.objects.get(pk=element[1])
        context = {
            'username': user.username,
            'city': city.name,
            'temp': weather.temp,
            'feels_like': weather.feels_like,
            'pressure': weather.pressure,
            'visibility': weather.visibility,
            'wind': weather.wind,
            'icon': weather.icon,
        }
        print(context)
        subject = render_to_string('subject.txt', context)
        body_text = render_to_string('body.txt', context)
        email = EmailMessage(subject=subject, body=body_text, to=[user.email], connection=con)
        email_list.append(email)
    print(email_list)
    con.send_messages(email_list)
    con.close()
