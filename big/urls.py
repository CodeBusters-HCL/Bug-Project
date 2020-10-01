
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('pages.urls')),
    path('',include('accounts.urls')),
    path('',include('issues.urls')),
    path('admin/', admin.site.urls),
]
