from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',include('pages.urls')),
    path('',include('accounts.urls')),
    path('',include('issues.urls')),
   

    path('admin/', admin.site.urls),


]
