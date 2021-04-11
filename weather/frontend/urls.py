from django.urls import path
from django.views.generic.base import RedirectView

from frontend.views import WeatherListView, WeatherSummary, \
                WeatherFormView


app_name = 'frontend'

urlpatterns = [
    path('', RedirectView.as_view(url='list/')),
    path('list/', WeatherListView.as_view(), name='weather-list'), 
    path('summary/', WeatherSummary.as_view(), name='weather-summary'),
    path('add/', WeatherFormView.as_view(), name='weather-add'),
]