from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import renderers
from rest_framework.decorators import api_view


from core.models import Weather
from api.serializers import WeatherSerializer


class WeatherList(APIView):
    """
    List all Weather data, or create a new.
    """
    def get(self, request, format=None):
        weather_data = Weather.objects.all()
        serializer = WeatherSerializer(weather_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherDetail(APIView):
    """
    Retrieve, update or delete a weather instance.
    """
    def get_object(self, pk):
        try:
            return Weather.objects.get(pk=pk)
        except Weather.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        weather = self.get_object(pk)
        serializer = WeatherSerializer(weather)
        return Response(serializer.data)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'weather-data': reverse('api:api-weather-list', request=request, format=format)
    })
