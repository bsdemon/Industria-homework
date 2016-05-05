from django import forms
from .models import Currency
from django.core.exceptions import ValidationError
import re


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ["name", "code", "units", "cost_leva", "reverse_cost"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        reg = re.compile('\w+')
        if not reg.match(name):
            raise ValidationError(u'%s is not a currency name' % name)
        return name

    def clean_code(self):
        code = self.cleaned_data.get('code')
        reg = re.compile('[A-Z]+')
        if not reg.match(code) or len(code) > 4:
            raise ValidationError(u'%s is not a currency code' % code)
        return code

    def clean_units(self):
        units = self.cleaned_data.get('units')
        return units

    def clean_cost_leva(self):
        cost_leva = self.cleaned_data.get('cost_leva')
        return cost_leva

    def clean_reverse_cost(self):
        reverse_cost = self.cleaned_data.get('reverse_cost')
        return reverse_cost

    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Име на валутата"
        self.fields['code'].label = "Код на валута"
        self.fields['units'].label = "Количество"
        self.fields['cost_leva'].label = "Стойност за 1 лев"
        self.fields['reverse_cost'].label = "Обратен курс за 1 лев"


class ChooseForm(forms.Form):
    CHOICES = Currency.objects.all()

    from_currency = forms.CharField(max_length=20,
                                    widget=forms.Select(
                                        choices=((ch.cost_leva, ch.name) for ch in CHOICES)))

    to_currency = forms.CharField(max_length=20,
                                  widget=forms.Select(
                                      choices=((ch.reverse_cost, ch.name) for ch in CHOICES)))

    units = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(ChooseForm, self).__init__(*args, **kwargs)
        self.fields['from_currency'].label = "От валута"
        self.fields['to_currency'].label = "Във валута"

    def clean_units(self):
        units = self.cleaned_data.get('units')
        return units

    def clean_from_currency(self):
        from_currency = self.cleaned_data.get('from_currency')
        return from_currency

    def clean_to_currency(self):
        to_currency = self.cleaned_data.get('to_currency')
        return to_currency
