from DjangoWeatherRemider.celery import app
from .models import SubListApp
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from User.models import UserApp
from City.models import CityApp
from Weather.models import WeatherApp


@app.task(name="Preparing to send e-mail every one hour")
def send_email_every_one_hour():
    subscriptions = SubListApp.objects.filter(send_email=1)
    if not subscriptions:
        return 'Subscriptions not found'
    user_city_list = [[subscription.user_id.pk, subscription.city_id.pk] for subscription in subscriptions]
    send_email.delay(user_city_list)
    return 'Successfully'


@app.task(name="Preparing to send e-mail every three hours")
def send_email_every_three_hours():
    subscriptions = SubListApp.objects.filter(send_email=3)
    if not subscriptions:
        return 'Subscriptions not found'
    user_city_list = [[subscription.user_id.pk, subscription.city_id.pk] for subscription in subscriptions]
    send_email.delay(user_city_list)
    return 'Successfully'


@app.task(name="Preparing to send e-mail every six hours")
def send_email_every_six_hours():
    subscriptions = SubListApp.objects.filter(send_email=6)
    if not subscriptions:
        return 'Subscriptions not found'
    user_city_list = [[subscription.user_id.pk, subscription.city_id.pk] for subscription in subscriptions]
    send_email.delay(user_city_list)
    return 'Successfully'


@app.task(name="Send email")
def send_email(user_city_list):
    con = get_connection()
    con.open()
    email_list = []
    try:
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
            subject = f"Hi, {user.username}!"
            body_text = render_to_string('body.html', context)
            email = EmailMultiAlternatives(subject=subject, body=body_text, to=[user.email], connection=con)
            email.attach_alternative(body_text, 'text/html')
            email_list.append(email)
        con.send_messages(email_list)
        con.close()
        return 'Successfully'
    except BaseException as error:
        return 'An exception occurred: {}'.format(error)
