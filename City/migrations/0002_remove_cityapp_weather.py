# Generated by Django 3.2.7 on 2021-09-08 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('City', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cityapp',
            name='weather',
        ),
    ]
