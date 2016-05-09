from django.shortcuts import render,HttpResponseRedirect
from .forms import CurrencyForm, ChooseForm
from .models import Currency
from decimal import *

# Create your views here.


def currency_home(request):
    queryset = Currency.objects.all()

    result = 0
    form = ChooseForm(request.POST or None)
    usd = Currency.objects.get(name='Щатски долар')
    usd.refresh_from_db()
    if form.is_valid():
        cost_leva = form.cleaned_data.get('from_currency')
        to_currency = form.cleaned_data.get('to_currency')
        units = form.cleaned_data.get('units')
        result = round(Decimal(units) * Decimal(cost_leva) * 1/Decimal(to_currency), 6)
    else:
        print('form is not valid!!!!!!!!!!!!!!!!!!!!')
    context = {
        "title": "Currency list",
        "currency_list": queryset,
        "form": form,
        "result": result
    }
    return render(request, "calculator.html", context)


def add_currency(request):
    form = CurrencyForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.name = form.cleaned_data.get("name")
        instance.code = form.cleaned_data.get("code")
        instance.units = form.cleaned_data.get("units")
        instance.cost_leva = form.cleaned_data.get("cost_leva")
        instance.reverse_cost = form.cleaned_data.get("reverse_cost")
        instance.save()
        return HttpResponseRedirect('/add')

    context = {
        "title": "Add currency",
        "form": form
    }
    return render(request, "add.html", context)
