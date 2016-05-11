from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.currency_home),
    url(r'add/$', views.add_currency),
    url(r'calc/$', views.ajax_calc),
]