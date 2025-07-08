from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('provinces/', views.ProvinceListAPIView.as_view(), name='province_list'),
    path('cities/', views.CityListAPIView.as_view(), name='city_list'),
    path('neighborhoods/<int:city_id>/', views.NeighborhoodListAPIView.as_view(), name='neighborhood_list'),
]