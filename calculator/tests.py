from django.test import TestCase
from django.http import HttpRequest
from .models import Currency
from .views import currency_home, add_currency
import unittest

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


class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = currency_home(request)
        self.assertIn('<title>Currency list</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.strip().startswith(b'<!DOCTYPE html>'))
        self.assertTrue(response.content.strip().endswith(b'</html>'))
