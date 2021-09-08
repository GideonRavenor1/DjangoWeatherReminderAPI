from django.db import models


class CityApp(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='City')
    create_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Create at')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        for weather in self.weather.all():
            weather.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-create_at']
