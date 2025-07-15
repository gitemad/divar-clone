from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('advertises/', views.AdvertiseCreateAPIView.as_view(), name='advertise_create'),
    path('advertises/<uuid:uuid>/', views.AdvertiseRetrieveAPIView.as_view(), name='advertise_retrieve'),
    path('city/<slug:city_slug>/', views.AdvertiseListAPIView.as_view(), name='advertise_list'),
]