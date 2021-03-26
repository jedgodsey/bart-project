# from django.db import models
from djongo import models

class Delays(models.Model):
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.amount)
