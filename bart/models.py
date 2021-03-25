from django.db import models

class Delays(models.Model):
    amount = models.FloatField()
    def __str__(self):
        return self.amount
