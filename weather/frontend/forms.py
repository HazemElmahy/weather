from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from core.models import Weather


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['temperature', 'humidity']
        widgets = {
            'humidity': forms.NumberInput(attrs={"placeholder":"Humidity", "min": 35, "max": 65}),
            'temperature': forms.NumberInput(attrs={"placeholder":"Temperature", "min": 19, "max": 28}),
        }