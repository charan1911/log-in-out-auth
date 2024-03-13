from django.shortcuts import render , redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User

from .models import Userr
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required

from django.urls import reverse



# Create your views here.
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


@login_required(login_url='/login/')
def success_g(request):
    context = {}
    context['user'] = request.user
    return render (request , 'success_g.html', context)

@login_required(login_url='/login/')
def success_c(request):
    context = {}
    context['user'] = request.user
    return render (request , 'success_c.html', context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('basee'))
    






def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username == 'gummaaa':
                return redirect(reverse('user_success_g'))
            else:
                return redirect(reverse('user_success_c'))
        else:
            context['error'] = "Provide valid username and password"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)
