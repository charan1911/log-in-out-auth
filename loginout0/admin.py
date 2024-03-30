from django.contrib import admin
from .models import Product
#from .models import CustomerBooked

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    search_fields = ['name', 'description']

"""@admin.register(CustomerBooked)
class CustomerBookedAdmin(admin.ModelAdmin):
    list_display = ['user', 'car_name', 'price', 'days', 'no_of_days', 'total_price']
"""

# admin.py

from django.contrib import admin
from .models import Bookings

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_name', 'price']  # Display these fields in the admin list view
    list_filter = ['user', 'product_name']  # Add filters for these fields


from django.contrib import admin
from .models import LikedProduct

@admin.register(LikedProduct)
class LikedProduct(admin.ModelAdmin):
    list_display = ('user', 'product')  # Display user and product in the admin list
    list_filter = ('user',)  # Add filter by user in the admin
    search_fields = ('user__username', 'product__name')  # Add search by user's username and product's name
