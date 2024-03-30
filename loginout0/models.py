from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="product_pictures/")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# models.py
# models.py

from django.db import models
from django.contrib.auth.models import User

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed for your booking details

    def __str__(self):
        return f"{self.user.username} - {self.product_name}"



from django.contrib.auth.models import User
from django.db import models

class LikedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming you have a Product model

    def __str__(self):
        return f"{self.user.username} likes {self.product.name}"





"""from django.contrib.auth.models import User

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Add more fields as needed for your booking details

    def __str__(self):
        return f"{self.user.username} - {self.carname}"

"""



"""from django.db import models
from django.contrib.auth.models import User

class CustomerBooked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.IntegerField()
    no_of_days = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.car_name}"
"""