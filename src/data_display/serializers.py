from rest_framework import serializers

from data_aggregation.models import WeatherData
from datetime import datetime


class GetWeather(serializers.ModelSerializer):
    date_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = WeatherData
        fields = "__all__"

    def get_date_time(self, obj):
        datetime_str, _ = obj.datetimeStr.split("+")
        dt = int(datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S").timestamp())
        return dt


class GetWeatherListSerializer(serializers.ListSerializer):
    child = serializers.SerializerMethodField(method_name="get_child")  # type: ignore

    def get_child(self, weather_obj) -> "Optional[Dict]":
        return GetWeather(weather_obj).data
