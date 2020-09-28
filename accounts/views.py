from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method =='POST':
        print('Register')
        
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method =='POST':
        print('Login')
        
    else:
        return render(request,'accounts/login.html')
