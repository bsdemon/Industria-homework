from django.shortcuts import render,HttpResponseRedirect
from .forms import CurrencyForm, ChooseForm
from .models import Currency
from decimal import *

# Create your views here.


def currency_home(request):
    queryset = Currency.objects.all()
    form = ChooseForm(request.POST or None)

    context = {
        "title": "Currency list",
        "currency_list": queryset,
        "form": form,
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
