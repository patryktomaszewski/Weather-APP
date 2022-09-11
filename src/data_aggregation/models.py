from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class Country(models.Model):
    name = models.CharField(_("Country name"), max_length=255, unique=True)
    city = models.CharField(_("City name"), max_length=255)
    lat = models.DecimalField(_("Geographical coordinates latitude"), max_digits=255, decimal_places=2, blank=True, null=True)
    lon = models.DecimalField(_("Geographical coordinates longitude)"), max_digits=255, decimal_places=2, blank=True, null=True)


class WeatherData(models.Model):
    datetimeStr = models.CharField(max_length=255, null=True)
    wdir = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    temp = models.DecimalField(max_digits=255, decimal_places=2)
    maxt = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    visibility = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    wspd = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    solarenergy = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    cloudcover = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    mint = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    datetime = models.DecimalField(max_digits=78, decimal_places=0, null=True)
    precip = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    sealevelpressure = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    snow = models.IntegerField(null=True)
    dew = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    precipcover = models.IntegerField(null=True)
    wgust = models.DecimalField(max_digits=255, decimal_places=2, null=True)
    conditions = models.CharField(max_length=255, null=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
    )

    @property
    def get_date_time(self):
        datetime_str, _ = self.datetimeStr.split("+")
        dt = int(datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S").timestamp())
        return dt
