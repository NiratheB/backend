from django.db import models
from backend.constants import SHAPE_CHOICES


class Shape(models.Model):
    type = models.IntegerField(choices=SHAPE_CHOICES)
    color = models.CharField(max_length=6)
    attributes = models.JSONField()
