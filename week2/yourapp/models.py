# yourapp/models.py
from django.db import models

class YourModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()