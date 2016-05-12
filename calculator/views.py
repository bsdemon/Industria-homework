from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import CurrencyForm, ChooseForm
from .models import Currency
from decimal import *
from django.views.decorators.csrf import csrf_protect

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


@csrf_protect
def ajax_calc(request):
    result = 0

    if request.method == "POST":
        form = ChooseForm(request.POST or None)
        if request.is_ajax():
            if form.is_valid():
                from_currency_name = form.cleaned_data.get('from_currency')
                to_currency_name = form.cleaned_data.get('to_currency')
                units = form.cleaned_data.get('units')

                result = calculate(units, from_currency_name, to_currency_name)

    return HttpResponse(result)


def get_actual_currency(currency):
    currency_obj = Currency.objects.get(name=currency)
    currency_obj.refresh_from_db()
    return currency_obj


def calculate(units, from_currency_name, to_currency_name):
    from_currency_obj = get_actual_currency(from_currency_name)
    to_currency_obj = get_actual_currency(to_currency_name)

    from_currency_cost = Decimal(from_currency_obj.cost_leva)
    from_currency_units = Decimal(from_currency_obj.units)
    to_currency_cost = Decimal(to_currency_obj.cost_leva)
    to_currency_units = Decimal(to_currency_obj.units)
    units = Decimal(units)

    result = round(units
                   * from_currency_cost / from_currency_units
                   / to_currency_cost / to_currency_units, 6)

    return result
