from django.db import models
from django.utils.timezone import now
import uuid


class CovidCaseWebData(models.Model):
    country_name = models.CharField(max_length=100)
    total_cases = models.CharField(max_length=100)
    acive_cases = models.CharField(max_length=100)
    total_deaths = models.CharField(max_length=100)
    recovery_rate = models.CharField(max_length=10)
    pop_infected_per = models.CharField(max_length=10)
    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Covid Case Data"
        verbose_name_plural = "Covid Case Datas"

    def __str__(self):
        return "Data of " + self.country_name
