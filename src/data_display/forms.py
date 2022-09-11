import datetime

from django import forms

from data_aggregation.models import Country


class FilterForm(forms.Form):
    time_from = forms.DateTimeField(widget=forms.SelectDateWidget(years=range(1985, datetime.date.today().year + 1)),
                                    required=False)
    time_to = forms.DateTimeField(widget=forms.SelectDateWidget(years=range(1985, datetime.date.today().year + 1)),
                                    required=False)
    temp_from = forms.DecimalField(required=False)
    temp_to = forms.DecimalField(required=False)
    country = forms.ChoiceField(choices=Country.objects.all().values_list("id", "name"), required=False)