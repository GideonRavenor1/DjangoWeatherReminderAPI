from django.contrib import admin
from .models import WeatherApp


class WeatherAppAdmin(admin.ModelAdmin):
    list_display = ('create_at', 'update')
    fields = ('create_at', 'update',)
    readonly_fields = ('create_at',)
    list_filter = ('create_at', 'update')


admin.site.register(WeatherApp, WeatherAppAdmin)
