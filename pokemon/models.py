from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    class PokemonTypes(models.TextChoices):
        WATER = 'WA'
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'
    
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=PokemonTypes.choices)
    hp = models.PositiveIntegerField()
    active = models.BooleanField(default = True)
    name_fr = models.CharField(max_length=30, default = "")
    name_ar = models.CharField(max_length=30, default = "")
    name_jp = models.CharField(max_length=30, default = "")
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now=True)