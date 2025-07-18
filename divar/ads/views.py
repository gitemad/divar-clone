from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import (
    Category,
    Advertise,
)
from .serializers import (
    CategorySerializer,
    AdvertiseCreateSerializer,
    AdvertiseListSerializer,
    AdvertiseRetrieveSerializer,
    AdvertiseContactInfoSerializer,
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

class AdvertiseListAPIView(ListAPIView):
    serializer_class = AdvertiseListSerializer

    def get_queryset(self):
        city_slug = self.kwargs.get('city_slug')
        return Advertise.objects.filter(city__slug=city_slug)

class AdvertiseRetrieveAPIView(RetrieveAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseRetrieveSerializer
    lookup_field = 'uuid'

class AdvertiseContactInfoAPIView(RetrieveAPIView):
    queryset = Advertise.objects.select_related('user')
    serializer_class = AdvertiseContactInfoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'
