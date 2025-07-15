from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    Category,
    Advertise,
)
from .serializers import (
    CategorySerializer,
    AdvertiseCreateSerializer,
)

# Create your views here.
class CategoryListAPIView(APIView):
    # TODO: Optimze number of queries
    def get(self, request):
        categories = Category.objects.all()

        category_dict = {category.id: category for category in categories}

        tree = []

        for category in categories:
            if category.parent is None:
                tree.append(category)
            else:
                parent = category_dict.get(category.parent.id)
                if parent:
                    if not hasattr(parent, 'childs'):
                        parent.childs = []
                    parent.childs.append(category)

        serializer = CategorySerializer(tree, many=True)
        return Response(serializer.data)

# TODO: Delete category and shift the order

class AdvertiseCreateAPIView(CreateAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
