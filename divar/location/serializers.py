from rest_framework import serializers
from .models import (
    Province,
    City,
    Neighborhood,
)

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = (
            'id',
            'title',
        )

class CitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(
        read_only=True,
    )

    class Meta:
        model = City
        fields = (
            'id',
            'title',
            'slug',
            'province',
        )

class NeighborhoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Neighborhood
        fields = (
            'id',
            'title',
        )
