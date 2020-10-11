from django.shortcuts import render, redirect
from django.contrib import messages, auth
#from django.contrib.auth.models import User     #uncomment this and commentout below line if inbuilt user is needed
from .models import User
from issues.models import Issue
from django.template import context
from django.contrib.auth import views as auth_views       #to use the django inbuilt password reset feature
import math, random 
from django.contrib.auth.hashers import make_password, check_password
from .decorators import authorisation_check
# from accounts.api.serializers import UserSerializer
# from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view


# Create your views here.
# @api_view(['GET',])
@authorisation_check
def register(request):
    if request.method =='POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        req = request.POST.get('staff_req')
        staff_req = False
        if req=="on":
            staff_req=True

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                     first_name=first_name, last_name=last_name, staff_req=staff_req)
                    user.save()
                    messages.success(request, 'You are now registered and can login now.')
                    return redirect('login')

                
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
        
    else:
        return render(request,'accounts/register.html')


def deactivate(request):
    symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-_!@#$%^&*():<>;,~`/|"
    passw = ""
    length = len(symbols)
    for i in range(8):
        passw += symbols[math.floor(random.random() * length)]
    user = request.user
    user.is_active=False
    user.password = make_password(passw)
    user.save()
    messages.success(request, 'Profile successfully disabled.')
    return redirect('index')



@authorisation_check
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        

        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            user = User.objects.get(username=username)
            if not user.is_active:
                messages.error(request, "Your account is inactive, Please reset password before you use it")
                user.is_active = True
                user.save()
                return redirect('reset_password')
            else:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    messages.success(request,'You are now logged in')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid Credentials')
                    return redirect('login')
        else:
            messages.error(request, 'Invalid usernmame')
            return redirect('login')

        
    else:
        return render(request,'accounts/login.html')




def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request, 'You are Logged out')
        return redirect('index')
    
