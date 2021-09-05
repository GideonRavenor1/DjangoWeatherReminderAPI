from django.db import models


class WeatherApp(models.Model):
    HOURS = (
        (3, 3),
        (6, 6),
        (9, 9),
        (12, 12),
        (24, 24)
    )
    create_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Create at')
    update = models.SmallIntegerField(default=3, choices=HOURS, verbose_name='Notice period')

    def __str__(self):
        return self.city.name

    class Meta:
        verbose_name = 'Weather'
        verbose_name_plural = 'Weather'
        ordering = ['-create_at']

