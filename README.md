DjangoWeatherReminder
=
##A small API service for sending weather. You can add cities, subscribe to them, choose the frequency of sending weather to e-mail.
#Technologies used:

>Docker
> 
>Django
> 
>DjangoRestFramework
>
>Celery
>
>Redis
>
>PostgreSQL
>
>Swagger
>
>Flower
> 
>SendGrid

#To use you need:
>Your customized SednGrid account and host key.
>
>Downloaded and installed docker.
>
>Account and API key on the service https://openweathermap.org/

After cloning the repository, go to the folder on the level with the docker-compose file, and enter the 
>docker-compose build
> 
command.

After building, enter 
>docker-compose up -d
> 
To create a superuser, enter 
>docker-compose exec django python manage.py createsuperuser
> 

#To view Swagger follow the link
>localhost:8000/swagger/
> 
#Flower
>localhost:5555
> 
#Admin area
>localhost:8000/admin
