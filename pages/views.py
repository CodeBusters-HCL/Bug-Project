from django.shortcuts import render
from django.http import HttpResponse
from accounts.decorators import authorisation_check
# Create your views here.

@authorisation_check
def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')


