from django.db import models

# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    units = models.IntegerField()
    cost_leva = models.DecimalField(max_digits=15, decimal_places=6)
    reverse_cost = models.DecimalField(max_digits=15, decimal_places=6)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name