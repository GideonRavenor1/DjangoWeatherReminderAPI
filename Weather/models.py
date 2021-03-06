from django.db import models
from City.models import CityApp


class WeatherApp(models.Model):
    create_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Create at')
    temp = models.CharField(max_length=5, verbose_name='Temperature in C', blank=True, null=True)
    feels_like = models.CharField(max_length=5, verbose_name='Feels like in C', blank=True, null=True)
    pressure = models.CharField(max_length=5, verbose_name='Pressure', blank=True, null=True)
    visibility = models.CharField(max_length=20, verbose_name='Visibility', blank=True, null=True)
    wind = models.CharField(max_length=10, verbose_name='Wind m.s', blank=True, null=True)
    icon = models.CharField(max_length=200, verbose_name='Icon', blank=True, null=True)
    city = models.ForeignKey(CityApp, related_name='weather',
                             on_delete=models.CASCADE, verbose_name='City', null=True)

    def __str__(self):
        return 'Temperature in %s' % self.city.name

    class Meta:
        verbose_name = 'Weather'
        verbose_name_plural = 'Weather'
        ordering = ['-create_at']
