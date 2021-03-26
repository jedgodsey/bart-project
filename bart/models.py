# from django.db import models
from djongo import models

class Delays(models.Model):
    amount = models.FloatField()
    def __str__(self):
        return str(self.amount)
