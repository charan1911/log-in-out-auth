from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *
from .views import success_g, success_c

from django.urls import reverse  # Import reverse function

'''
urlpatterns = [
    # plain front page----------------
    path('',basee,name='basee'),
    path('signin/',signin,name='signin'),
    #path('login/', login_page, name='login'),
    
    path("login/",user_login, name="user_login"),
    path('success_g/', success_g, name='success_g'),
    path('success_c/', success_c, name='success_c'),
    path("logout/",user_logout, name="user_logout"),

]
'''

urlpatterns = [
    path('', basee, name='basee'),
    path('signin/', signin, name='signin'),
    path('login/', user_login, name='user_login'),  # Changed to user_login
    path('success_g/', success_g, name='user_success_g'),  # Changed to user_success_g
    path('success_c/', success_c, name='user_success_c'),  # Changed to user_success_c
    path('logout/', user_logout, name='user_logout'),  # Changed to user_logout
]
