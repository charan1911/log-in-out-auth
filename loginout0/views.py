from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import HttpResponseBadRequest



from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import LikedProduct



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LikedProduct

@login_required
def liked_products(request):
    # Get the default username (current logged-in user's username)
    default_username = request.user.username
    
    # Retrieve liked products associated with the user
    liked_products = LikedProduct.objects.filter(user=request.user)
    
    # Pass the liked products and default username to the template
    return render(request, 'liked_products.html', {'liked_products': liked_products, 'default_username': default_username})






from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import LikedProduct, Product
#from .views import liked_product
@login_required
def like_this_product(request, product_id):
    # Get the user object corresponding to the logged-in user
    user = request.user
    
    # Retrieve the product object using product_id
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the product is already liked by the user
    liked_product, created = LikedProduct.objects.get_or_create(user=user, product=product)
    
    # Redirect to the success page if the product is liked successfully
    if created:
        return redirect('user_success_c')
    else:
        # If the product is already liked, you can redirect to some other page or render a message
        return redirect('user_success_c')

"""@login_required
def like_this_product(request):
    # Get the default username (current logged-in user's username)
    default_username = request.user.username
    
    # Get the user object corresponding to the default username
    user = User.objects.filter(username=default_username).first()
    
    if user:
        # Retrieve liked products associated with the user
        liked_products = LikedProduct.objects.filter(user=user)
        
        # Pass the liked products and default username to the template
        return render(request, 'liked_products.html', {'liked_products': liked_products, 'default_username': default_username})
    else:
        # Render an error page if the user is not found
        return render(request, 'error.html', {'message': 'User not found'})


"""










# views.py

from django.shortcuts import redirect, get_object_or_404
from .models import Bookings

def book_product(request, product_id):
    if request.method == 'POST' and request.user.is_authenticated:
        # Get the product based on the provided ID
        product = get_object_or_404(Product, pk=product_id)
        
        # Retrieve form data
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        
        # Create a booking instance using the product details and the logged-in user
        booking = Bookings.objects.create(
            user=request.user,
            product_name=product_name,
            price=price
        )

        # Add more fields to the booking object as needed

        return redirect('success_c')  # Redirect to product detail page after booking
    else:
        return redirect('user_login')  # Redirect to login page if user is not authenticated

























@login_required(login_url='/login/')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



@login_required(login_url='/login/')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})



@login_required(login_url='/login/')
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        if not name or not description or not price:
            return HttpResponseBadRequest("Please provide all required fields.")
        
        picture = request.FILES.get('picture')
        if not picture:
            return HttpResponseBadRequest("Please provide a picture.")

        Product.objects.create(name=name, description=description, price=price, picture=picture)
        return redirect('user_success_g')
    return render(request, 'product_form.html')




@login_required(login_url='/login/')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        if not name or not description or not price:
            return HttpResponseBadRequest("Please provide all required fields.")
        
        picture = request.FILES.get('picture')
        if not picture:
            return HttpResponseBadRequest("Please provide a picture.")

        product.name = name
        product.description = description
        product.price = price
        product.picture = picture
        product.save()
        return redirect('user_success_g')
    return render(request, 'product_form.html', {'product': product})



@login_required(login_url='/login/')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('user_success_g')
    return render(request, 'product_delete.html', {'product': product})




















def basee(request):
    return render(request,"basee.html")

'''

def signin(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if User.objects.filter(username=username).exists():
            error = 'Username already exists.'
        elif password != confirm_password:
            error = 'Password and confirm password do not match.'
        else:
            User.objects.create(username=username, password=password)
            error = 'User created successfully!'
            # Redirect to signin page after successful registration
            

    return render(request, 'signin.html', {'error': error})

'''

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Check if the passwords match
        if password != confirm_password:
            return HttpResponse('Password and confirm password do not match.', status=400)

        # Check if the user exists in the database
        if User.objects.filter(username=username).exists():
            # Authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                # User authenticated successfully, redirect to base.html
                return redirect('basee')  # Assuming 'base' is the name of the URL pattern for 'base.html'
            else:
                # Password is incorrect
                return HttpResponse('Incorrect password. Please try again.', status=401)
        else:
            # Create a new user
            User.objects.create_user(username=username, password=password)
            # Authenticate the newly created user
            user = authenticate(username=username, password=password)
            if user is not None:
                # User authenticated successfully, redirect to base.html
                return redirect('basee')  # Assuming 'base' is the name of the URL pattern for 'base.html'
            else:
                # Something went wrong with authentication
                return HttpResponse('Unable to authenticate user.', status=500)

    return render(request, 'signin.html')


"""@login_required(login_url='/login/')
def success_c(request):
    context = {}
    context['user'] = request.user
    return render (request , 'success_c.html', context)
"""


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, LikedProduct

@login_required(login_url='/login/')
def success_c(request):
    context = {}
    context['user'] = request.user
    products = Product.objects.all()
    context['products'] = products
    
    # Get the liked products associated with the current user
    liked_products = LikedProduct.objects.filter(user=request.user)
    context['liked_products'] = liked_products
    
    return render(request, 'success_c.html', context)



@login_required(login_url='/login/')
def success_g(request):
    context = {}
    context['user'] = request.user
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'success_g.html', context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('basee'))

from django.shortcuts import redirect

def user_go_back(request):
    username = request.user.username  # Assuming user is authenticated
    if username == 'gummma':
        return redirect('user_success_g')  # Redirect to 'user_success_g' for username 'gummma'
    else:
        return redirect('user_success_c')  # Redirect to 'user_success_c' for other usernames



def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username == 'gummma':
                return redirect(reverse('user_success_g'))
            else:
                return redirect(reverse('user_success_c'))
        else:
            context['error'] = "Provide valid username and password"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)
