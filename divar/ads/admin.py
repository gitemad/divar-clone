from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Category,
    Advertise,
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'parent',
        'order',
    )
    list_filter = (
        'parent',
    )
    search_fields = (
        'title',
        'slug',
    )


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'title',
        'category',
        'user',
        'price',
        'created',
    )
    list_filter = (
        'category',
    )
    search_fields = (
        'title',
    )

