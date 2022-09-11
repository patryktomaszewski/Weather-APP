
from django.urls import path

from data_aggregation.views import DataAggregatorView

app_name = "data_aggregation"


urlpatterns = [
    path('', DataAggregatorView.as_view(), name="data_aggregation"),
]
