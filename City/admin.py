from django.contrib import admin
from .models import CityApp
from Weather.models import WeatherApp


class WeatherInTab(admin.TabularInline):
    model = WeatherApp
    extra = 0
    fields = ('update', 'temp', 'feels_like', 'pressure', 'visibility', 'wind', 'city')
    readonly_fields = ('temp', 'feels_like', 'pressure', 'visibility', 'wind', 'city')


class CityAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')
    fields = ('name', 'create_at',)
    readonly_fields = ('create_at',)
    search_fields = ('name',)
    list_filter = ('name', 'create_at')
    inlines = [WeatherInTab]


admin.site.register(CityApp, CityAppAdmin)
