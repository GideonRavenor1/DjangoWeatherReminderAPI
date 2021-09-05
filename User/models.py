from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models


class UserApp(AbstractUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER, default='Male', verbose_name='Sex')
