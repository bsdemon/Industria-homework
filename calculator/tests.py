from django.test import TestCase
from .models import Currency

# Create your tests here.


class CurrencyTest(TestCase):
    def create_currency(self, name="Щатски долар",
                        code="USD",
                        units=1,
                        cost_leva=1.73036,
                        reverse_cost=0.577914):
        return Currency.objects.create(name=name,
                                       code=code,
                                       units=units,
                                       cost_leva=cost_leva,
                                       reverse_cost=reverse_cost)

    def test_currency_creation(self):
        c = self.create_currency()
        self.assertTrue(isinstance(c, Currency))
        self.assertEqual(c.__str__(), c.name)