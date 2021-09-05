from django.db import models
from User.models import UserApp
from City.models import CityApp


class SubListApp(models.Model):
    city_id = models.ForeignKey(CityApp, related_name='subscriptions',
                                on_delete=models.CASCADE, verbose_name='City id')
    user_id = models.ForeignKey(UserApp, related_name='subscriptions',
                                on_delete=models.CASCADE, verbose_name='User id')
    create_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Create at')

    def __str__(self):
        return '%s - %s' % (self.user_id.username, self.city_id.name)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        ordering = ['-create_at']

