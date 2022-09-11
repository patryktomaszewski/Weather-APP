from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from data_aggregation.models import WeatherData
from data_display.filters import WeatherDataFilter
from data_display.forms import FilterForm
from data_display.serializers import GetWeatherListSerializer


def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FilterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            request.session['filter_form_data'] = form.data
    else:
        form = FilterForm()

    return render(request, "dashboard.html", {'form': form})


class DataDisplayView(ListAPIView):
    model = WeatherData
    queryset = WeatherData.objects.all()
    filterset_class = WeatherDataFilter
    # template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        labels = []
        data = []
        objs = self.get_queryset()
        for obj in objs:
            date = obj.datetimeStr.split("T")[0]
            city = obj.country.city
            country = obj.country.name
            labels.append(f"{date}, {country}, {city}")
            data.append(obj.temp)
        data = {
            'labels': labels,
            'data': data,
        }
        return Response(data)

    def get_queryset(self):
        qs = super().get_queryset()
        filter_data = self.request.session.get("filter_form_data")

        if filter_data:
            lookup = self.get_qs_lookup(filter_data)
            qs = qs.filter(**lookup)
            qs = self.filter_date(filter_data, qs)
        return qs

    def filter_date(self, filter_data, qs):
        if (day := filter_data.get("time_from_day")) and (year := filter_data.get("time_from_year")) and (month := filter_data.get("time_from_month")):
            ts = self.get_date_time_str(year, day, month)
            qs = [x for x in qs if x.get_date_time >= ts]

        if (day := filter_data.get("time_to_day")) and (year := filter_data.get("time_to_year")) and (
        month := filter_data.get("time_to_month")):
            ts = self.get_date_time_str(year, day, month)
            qs = [x for x in qs if x.get_date_time <= ts]
        return qs

    def get_qs_lookup(self, filter_data) -> dict:
        lookup = {}
        if country := filter_data.get("country"):
            lookup["country"] = int(country)
        if temp_from := filter_data.get("temp_from"):
            lookup["temp__gte"] = temp_from
        if temp_to := filter_data.get("temp_to"):
            lookup["temp__lte"] = temp_to

        return lookup

    @staticmethod
    def get_date_time_str(year, day, month):
        return int(datetime(year=int(year), day=int(day),
                 month=int(month), hour=12).timestamp())
