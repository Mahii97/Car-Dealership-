from django.db import models
from django.contrib.auth.models import User

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
