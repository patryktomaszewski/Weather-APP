
from django.shortcuts import redirect

from django.views.generic.edit import FormView
import requests
from datetime import datetime

from data_aggregation.forms import RequestForm
from data_aggregation.models import WeatherData, Country
import json

from data_aggregation.serializers import WeatherDataCreateSerializer
from rest_framework.response import Response


class DataAggregatorView(FormView):
    model = WeatherData
    template_name = "aggregate_data.html"
    form_class = RequestForm

    def post(self, request, *args, **kwargs):
        country = Country.objects.get(id=request.POST["country"])

        start_time, end_time = self.get_date_time(request)
        if not WeatherData.objects.filter(datetimeStr=start_time.strftime("%Y-%m-%dT%H:%M:%S+01:00"), country=country).exists():
            response = self.weather_api_request(start_time, end_time, country)
            detail = self.parse_error_message(response).get("locations").get(f"{country.city},{country.name}").get("values")[0]
            detail.update({"country": country.id})

            serializer = WeatherDataCreateSerializer(data=detail)
            serializer.is_valid(raise_exception=True)
            WeatherData.objects.get_or_create(**serializer.validated_data)
        return redirect(request.get_full_path())

    @staticmethod
    def get_date_time(request):
        start_time = datetime(year=int(request.POST["time_year"]), day=int(request.POST["time_day"]),
                              month=int(request.POST["time_month"]), hour=12)
        end_time = datetime(year=int(request.POST["time_year"]), day=int(request.POST["time_day"]),
                            month=int(request.POST["time_month"]), hour=12, second=1)
        return start_time, end_time

    @staticmethod
    def weather_api_request(start_time, end_time, country):
        url = "https://visual-crossing-weather.p.rapidapi.com/history"
        querystring = {"startDateTime": start_time.isoformat(), "aggregateHours": "1", "location": f"{country.city},{country.name}",
                       "endDateTime": end_time.isoformat(), "unitGroup": "metric", "contentType": "json",
                       "dayEndTime": "17:00:00", "shortColumnNames": "0"}

        headers = {
            "X-RapidAPI-Key": "1a8fdc4dffmsh8eff0330857d3e2p1aad15jsn7a12aa0b1534",
            "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    @staticmethod
    def parse_error_message(response: "Response") -> dict:
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            return {}