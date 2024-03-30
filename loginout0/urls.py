from django.contrib import admin
from django.urls import path, reverse  # Import reverse function
from django.urls import include
from .views import basee, signin, user_login, success_g, success_c, user_logout  # Import individual views

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


from .views import  product_detail
from .views import product_update
#from .views import product_delete
from .views import product_create
from .views import product_delete
from .views import product_list
from django.urls import path
from .views import user_go_back
from .views import book_product
from .views import like_this_product
from .views import liked_products


urlpatterns = [
    path('',basee,name='basee'),
    path('basee/', basee, name='basee'),
    path('signin/', signin, name='signin'),
    path('login/', user_login, name='user_login'),  
    path('success_g/', success_g, name='user_success_g'),  
    path('success_c/', success_c, name='user_success_c'),  
    path('logout/', user_logout, name='user_logout'),  
    path('product/<int:pk>/', product_detail, name='product_detail'),  # Add product_detail URL pattern
    path('product/<int:pk>/update/', product_update, name='product_update'),  # Define the URL pattern for product_update view
    #path('product/<int:pk>/delete/', product_delete, name='product_delete'),  # Define the URL pattern for product_delete view
    path('product/create/', product_create, name='product_create'),  # Define the URL pattern for product_create view
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
    path('product/list/', product_list, name='product_list'),
    path('go-back/', user_go_back, name='go_back'),
    path('success/', success_c, name='success_c'),
    path('book_product/<int:product_id>/', book_product, name='book_product'),
    path('like_this_product/<int:product_id>/', like_this_product, name='like_this_product'),
    path('liked_products/', liked_products, name='liked_products'),

]



