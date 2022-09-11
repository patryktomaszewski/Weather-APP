
from rest_framework import serializers

from data_aggregation.models import WeatherData


class WeatherDataCreateSerializer(serializers.ModelSerializer):
        class Meta:
                model = WeatherData
                fields = '__all__'
