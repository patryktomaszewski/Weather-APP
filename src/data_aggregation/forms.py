from django import forms
import datetime

from data_aggregation.models import Country


class RequestForm(forms.Form):
    time = forms.DateTimeField(widget=forms.SelectDateWidget(years=range(1985, datetime.date.today().year+1)))
    country = forms.ChoiceField(choices=Country.objects.all().values_list("id", "name"))
