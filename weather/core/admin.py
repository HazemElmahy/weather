from django.contrib import admin

from core.models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    pass

