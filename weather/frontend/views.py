from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import redirect

from core.models import Weather
from frontend.forms import WeatherForm


def compare_item_to_previous(list):
    """
    compares a list items with the ones before them
    and returns a list of 0, 1 and 2. 1 means greater
    than, 2 means less than and 0 means equal.
    """
    
    compared_list = []
    prev_index = list[0]
    for i in list:
        if i > prev_index:
            compared_list.append(1)
        elif i < prev_index:
            compared_list.append(2)
        else:
            compared_list.append(0)
        
        prev_index = i
    return compared_list


class WeatherListView(ListView):
    """
    List view of Weather data
    """

    template_name = "frontend/weather_list.html"
    model = Weather


    def get_context_data(self, **kwargs):
        weather_query = Weather.objects.all()
        temp_list = list(weather_query.values_list('temperature', flat=True))
        humidity_list = list(weather_query.values_list('humidity', flat=True))
        
        if len(temp_list) > 0:
            temp_list_compared = compare_item_to_previous(temp_list)
            humidity_list_compared = compare_item_to_previous(humidity_list)

            data = super().get_context_data(**kwargs)

            context = {
                "object_list": list(zip(data["object_list"],
                        temp_list_compared, humidity_list_compared))
            }

            print("context2222: ", context)

            return context


def split_list_into_chunks(raw_list, n=10):    
    """
    yields a nested generator of each 10 items of a list
    [1, 2,..., 11, 12...] >> [[1, 2,...], [11, 12...]]
    """

    for i in range(0, len(raw_list), n): 
        yield raw_list[i:i + n]


def average_of_list(raw_list):
    """
    returns average of a list
    """
    avg_list = []
    for i in raw_list:
        average = sum(i) / len(i)
        avg_list.append(average)
        
    return avg_list


def first_and_last_item(raw_list):
    """
    returns a nested list of the first and last items of 
    another nested list inner lists 
    [[1,2,3,4],[5,6,7,8]] >> [[1,4],[5,8]]
    """

    firstLast_list = []
    for i in raw_list:
        inner_list = [i[0], i[-1]]
        firstLast_list.append(inner_list)
    
    return firstLast_list

import json
class WeatherSummary(TemplateView):
    """
    Lists the average of each 10 weather records, their start date
    and end date
    """

    template_name = "frontend/summary.html"


    def get_context_data(self, **kwargs):
        weather_query = Weather.objects.all().order_by('-id')
        temp_list = list(weather_query.values_list('temperature', flat=True))
        humidity_list = list(weather_query.values_list('humidity', flat=True))
        timedate_list = list(weather_query.values_list('time_recorded', flat=True))
        id_list = list(weather_query.values_list('id', flat=True))

        humidity_average_list = average_of_list(split_list_into_chunks(humidity_list))
        temp_average_list = average_of_list(split_list_into_chunks(temp_list))
        timedate_first_last_list = first_and_last_item(split_list_into_chunks(timedate_list))
        chunk_id_list = split_list_into_chunks(id_list)

        context = {
            'summary_list': list(zip(humidity_average_list, temp_average_list, timedate_first_last_list, chunk_id_list))
        }

        print("context ", context)

        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":

            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode).replace("[","").replace("]","")
            weather_ids = list(body.split(","))

            print("weather_ids ", weather_ids)
            for id in weather_ids:
                weather = Weather.objects.get(pk=id)
                weather.delete()
            return redirect(reverse('frontend:weather-summary'))


class WeatherFormView(CreateView):
    template_name = 'frontend/weather_add.html'
    form_class = WeatherForm

    def get_success_url(self):
        return reverse('frontend:weather-list')

