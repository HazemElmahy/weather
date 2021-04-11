from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


app_name = 'api'

urlpatterns = [
    path('', views.api_root),
    path('weather/', views.WeatherList.as_view(), name='api-weather-list'),
    path('weather/<int:pk>/', views.WeatherDetail.as_view(), name='api-weather-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)