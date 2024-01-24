# models.py
from django.db import models

class Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    trace_date = models.DateTimeField(auto_now_add=True)
    trace_count = models.IntegerField(default=0)
    def __str__(self):
        return self.product_title

