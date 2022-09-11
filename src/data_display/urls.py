from django.urls import path

from data_display.views import DataDisplayView
from data_display.views import home

app_name = "data_display"


# urlpatterns = [
#     path('', DataDisplayView.as_view(), name="data-display"),
# ]

urlpatterns = [
    path('', home, name='home'),
    path('weather-chart/', DataDisplayView.as_view(), name='weather-chart'),
]