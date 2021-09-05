from django.db import models
from Weather.models import WeatherApp


class CityApp(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='City')
    weather = models.ForeignKey(WeatherApp, related_name='city',
                                on_delete=models.CASCADE, verbose_name='Weather')
    create_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Create at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-create_at']
