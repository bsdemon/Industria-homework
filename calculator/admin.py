from django.contrib import admin
from .models import Currency

# Register your models here.


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "units", "cost_leva", "reverse_cost"]
    list_filter = ["name", "cost_leva"]
    search_fields = ["nane"]

    class Meta:
        model = Currency


admin.site.register(Currency, CurrencyAdmin)