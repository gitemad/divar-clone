from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number',
        'first_name',
        'last_name',
        'is_active',
    ]
    list_filter = [
        'is_active',
    ]
    search_fields = [
        'phone_number',
        'first_name',
        'last_name',
    ]
