from rest_framework import serializers
from .models import Category

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
