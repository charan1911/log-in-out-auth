from django.db import models

# Create your models here.

from django.db import models

class Userr(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
