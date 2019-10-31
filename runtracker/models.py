from django.db import models

class Runtracker(models.Model):
    date = models.DateField()
    distance = models.DecimalField(
        decimal_places=0,
        max_digits=6
    )
    time = models.DecimalField(
        decimal_places=0,
        max_digits=6
    )
    calories = models.DecimalField(
        decimal_places=4,
        max_digits=8
    )