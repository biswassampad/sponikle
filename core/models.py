from django.db import models
from djongo import models


class User(models.Model):
    name = models.CharField(max_length=100)
