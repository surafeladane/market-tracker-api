from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PriceEntry(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=100)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop} at {self.market} - {self.price}"