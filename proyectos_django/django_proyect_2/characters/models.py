from typing import Match
from django.db import models
from django.db.models.base import Model

class City(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        db_table = "city"

class Universe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    foundation = models.CharField(max_length=100)

    class Meta:
        db_table = "universes"

class Power(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "powers"

class Character(models.Model):
    cit = models.ForeignKey(City, on_delete=models.CASCADE)
    uni = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    path = models.FileField(upload_to="")
    date_of_birth = models.CharField(max_length=100)
    #created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "characters"

class PowerCharacter(models.Model):
    pow = models.ForeignKey(Power, on_delete=models.CASCADE)
    cha = models.ForeignKey(Character, on_delete=models.CASCADE)
    level = models.FloatField()

    class Meta:
        db_table = "powers_character"



