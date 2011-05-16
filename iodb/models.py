from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    name = models.CharField(max_length=50)

class Event(models.Model):
    name = models.CharField(max_length=50)
    submited_by = models.CharField(User)
