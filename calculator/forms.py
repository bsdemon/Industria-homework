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

    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Име на валутата"
        self.fields['code'].label = "Код на валута"
        self.fields['units'].label = "Количество"
        self.fields['cost_leva'].label = "Левове за единица валута"
        self.fields['reverse_cost'].label = "Валута за 1 лев"


class ChooseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ChooseForm, self).__init__(*args, **kwargs)
        self.fields['from_currency'] = forms.ChoiceField(
            choices=get_my_choices(),
            label='От валута')
        self.fields['to_currency'] = forms.ChoiceField(
            choices=get_my_choices(),
            label="Във валута")

    units = forms.IntegerField(label='Единици')


def get_my_choices():
    queryset = Currency.objects.all()
    choices = []
    for query in queryset:
        choice = (query.name, query.name)
        choices.append(choice)
    return choices
