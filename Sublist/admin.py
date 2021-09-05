from django.contrib import admin
from .models import SubListApp


class SubListAppAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'city_id', 'create_at')
    fields = ('user_id', 'city_id', 'create_at')
    readonly_fields = ('create_at',)
    search_fields = ('user_id', 'city_id',)
    list_filter = ('user_id', 'city_id', 'create_at')


admin.site.register(SubListApp, SubListAppAdmin)
