from django import forms
from .models import Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ["name", "code", "units", "cost_leva", "reverse_cost"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name

    def clean_code(self):
        code = self.cleaned_data.get('code')
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


class ChooseForm(forms.Form):
    currency_form = forms.ModelMultipleChoiceField(
        queryset=Currency.objects.all().order_by('name'))