
from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('accounts/login',views.login, name= 'login'),
    path('accounts/register',views.register, name= 'register'),
    
    path('accounts/logout',views.logout, name= 'logout'),
]
