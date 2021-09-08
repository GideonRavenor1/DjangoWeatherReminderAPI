from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import WeatherApp


class WeatherAppAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'create_at', 'update', 'temp', 'get_icon')
    fields = ('create_at', 'update', 'get_icon', 'temp', 'feels_like', 'pressure', 'visibility', 'wind', 'city')
    readonly_fields = ('create_at', 'get_icon', 'temp', 'feels_like', 'pressure', 'visibility', 'wind', 'city')
    list_filter = ('create_at', 'update')

    def get_icon(self, obj):
        return mark_safe(f'<img src="{obj.icon}" width="50", height=60">')

    get_icon.short_description = "Icon"


admin.site.register(WeatherApp, WeatherAppAdmin)
