from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category_list'),
]