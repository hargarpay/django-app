from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.fullname