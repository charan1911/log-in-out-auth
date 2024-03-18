from django.db import models

# Create your models here.

from django.db import models

class car(models.Model):
    carname = models.CharField(max_length=100)
    no_of_seats = models.IntegerField()
    color = models.CharField(max_length=50)
    pictures = models.ImageField(upload_to='car_pictures/')  # Assumes you'll upload pictures to a 'car_pictures' directory
    standard_price = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField for storing prices

    def __str__(self):
        return self.carname
