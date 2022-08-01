from django.contrib import admin
from .models import User, Album, Picture


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password', 'created_at', 'updated_at')


admin.site.register(Album)
admin.site.register(Picture)
