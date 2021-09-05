from django.contrib import admin
from .models import UserApp


class UserAppAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    fields = ('username', 'email', 'date_joined', 'gender')
    readonly_fields = ('date_joined',)
    search_fields = ('username',)
    list_filter = ('username',)


admin.site.register(UserApp, UserAppAdmin)
