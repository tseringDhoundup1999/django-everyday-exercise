from django.db import models

# Create your models here.

class Person(models.Model):
    SHIRT_SIZES = {
        "S":"Small",
        "M":"Medium",
        "L":"Large"
    }

    name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZES)

    def __str__(self):
        return f"{self.name} and shirt size is {self.shirt_size}"


class Runner(models.Model):
    medalType = models.TextChoices("MedalType","GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal= models.CharField(blank=True,choices=medalType,max_length=10)