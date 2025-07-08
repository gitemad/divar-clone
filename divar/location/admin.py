from django.contrib import admin
from .models import (
    Province,
    City,
    Neighborhood,
)

# Register your models here.
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = (
        'title',
    )
    ordering = (
        'title',
    )

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    search_fields = (
        'title',
        'slug',
    )
    ordering = (
        'title',
    )

@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = (
        'title',
    )
    ordering = (
        'title',
    )