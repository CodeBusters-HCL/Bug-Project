from django.urls import path

from accounts.api.views import UserApiView, UserApiDetailView, RegisterApiView

app_name = 'accounts'

urlpatterns = [
    path('users', UserApiView.as_view(), name="users_api"),
    path('users/<pk>', UserApiDetailView.as_view(), name="user_detail"),
    path('register', RegisterApiView.as_view(), name="register"),
]