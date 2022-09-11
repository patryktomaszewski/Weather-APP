import django_filters
from data_aggregation.models import WeatherData
from django.forms.widgets import DateTimeInput, DateInput
from data_aggregation.models import WeatherData


class WeatherDataFilter(django_filters.FilterSet):
    class Meta:
        model = WeatherData
        fields = ["datetimeStr"]

    datetimeStr__gte = django_filters.DateTimeFilter(
        widget=DateInput(
            attrs={"type": "datetime-local"},
        ),
        lookup_expr="gte",
        field_name="datetimeStr",
        label="weather after date: ",
    )
    datetimeStr__lte = django_filters.DateTimeFilter(
        widget=DateInput(
            attrs={"type": "datetime-local"},
        ),
        lookup_expr="lte",
        field_name="datetimeStr",
        label="weather before date: ",
    )

    # category = django_filters.ChoiceFilter(choices=LogCategory.choices)

#
# class CpuDataFilter(BaseDataFilter):
#     class Meta:
#         model = CpuData
#         fields = ["category"]