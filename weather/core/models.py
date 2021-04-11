from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Weather(models.Model):

    temperature = models.FloatField(
        validators=[MaxValueValidator(28), MinValueValidator(19)]
    )
    humidity = models.FloatField(
        validators=[MaxValueValidator(65), MinValueValidator(35)]
    )
    time_recorded = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.time_recorded)
