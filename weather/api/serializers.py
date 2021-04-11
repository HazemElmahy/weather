from rest_framework import serializers

from core.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Weather` instance, given the validated data.
        """
        return Weather.objects.create(**validated_data)