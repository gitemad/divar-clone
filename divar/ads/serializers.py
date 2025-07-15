from rest_framework import serializers
from .models import (
    Category,
    Advertise,
    Neighborhood,
)

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'order',
            'children',
        )

    def get_children(self, obj):
        children = getattr(obj, 'childs', [])
        return CategorySerializer(children, many=True).data

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = [
            'title',
        ]

class AdvertiseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = [
            'title',
            'category',
            'city',
            'neighborhood',
            'description',
            'image',
            'price',
        ]

class AdvertiseListSerializer(serializers.ModelSerializer):
    neighborhood = NeighborhoodSerializer()

    class Meta:
        model = Advertise
        fields = [
            'uuid',
            'title',
            'neighborhood',
            'image',
            'price',
            'created',
        ]

class AdvertiseRetrieveSerializer(serializers.ModelSerializer):
    neighborhood = NeighborhoodSerializer()

    class Meta:
        model = Advertise
        fields = [
            'title',
            'neighborhood',
            'image',
            'price',
            'created',
            'description',
        ]

class AdvertiseContactInfoSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Advertise
        fields = [
            'phone_number',
        ]
    
    def get_phone_number(self, obj):
        return obj.user.phone_number
