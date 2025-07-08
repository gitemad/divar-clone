from rest_framework.generics import ListAPIView
from .models import (
    Province,
    City,
    Neighborhood,
)
from .serializers import (
    ProvinceSerializer,
    CitySerializer,
    NeighborhoodSerializer,
)

# Create your views here.
class ProvinceListAPIView(ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    pagination_class = None

class CityListAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        province = request.query_params.get('province')
        query = request.query_params.get('q')

        if province:
            self.queryset = self.queryset.filter(province=province)
        
        if query:
            self.queryset = self.queryset.filter(title__contains=query)
        
        if not (query or province):
            self.queryset = self.queryset.none()

        return super().get(request, *args, **kwargs)

class NeighborhoodListAPIView(ListAPIView):
    serializer_class = NeighborhoodSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        neighborhoods = Neighborhood.objects.filter(city=city_id)

        if query := self.request.query_params.get('q'):
            neighborhoods = neighborhoods.filter(title__contains=query)

        return neighborhoods
