from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
    price = models.FloatField()

    class Meta:
        db_table = "wines"
