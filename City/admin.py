from django.contrib import admin
from .models import CityApp


class CityAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')
    fields = ('name', 'create_at')
    readonly_fields = ('name', 'create_at')
    search_fields = ('name',)
    list_filter = ('name', 'create_at')


admin.site.register(CityApp, CityAppAdmin)
