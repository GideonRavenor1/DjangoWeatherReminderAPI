from django.db import models
from User.models import UserApp
from City.models import CityApp


class SubListApp(models.Model):
    HOURS = (
        (1, 1),
        (3, 3),
        (6, 6),
        (9, 9),
        (12, 12),
        (24, 24)
    )
    city_id = models.ForeignKey(CityApp, related_name='subscriptions',
                                on_delete=models.CASCADE, verbose_name='City id')
    user_id = models.ForeignKey(UserApp, related_name='subscriptions',
                                on_delete=models.CASCADE, verbose_name='User id')
    create_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Create at')
    send_email = models.SmallIntegerField(default=1, choices=HOURS, verbose_name='Send interval')

    def __str__(self):
        return '%s - %s' % (self.user_id.username, self.city_id.name)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        unique_together = ('city_id', 'user_id')
        ordering = ['-create_at']

