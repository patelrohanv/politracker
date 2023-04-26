from django.db import models

class Politician(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    # Other relevant fields

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

class Trade(models.Model):
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=20, choices=[("buy", "Buy"), ("sell", "Sell")])
    trade_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Other relevant fields
