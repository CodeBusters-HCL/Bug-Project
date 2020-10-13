from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('pages.urls')),
    path('',include('accounts.urls')),
    path('',include('issues.urls')),
   

    path('admin/', admin.site.urls),

    # #REST FRAMEWORK API URLS
    path('accounts/api/', include('accounts.api.urls', 'accounts_api')),
    path('issues/api/', include('issues.api.urls', 'issues_api')),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
