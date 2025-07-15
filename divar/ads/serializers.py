from rest_framework import serializers
from .models import (
    Category,
    Advertise,
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
