from django.urls import path

from accounts.api.views import UserApiView, UserApiDetailView, RegisterApiView

app_name = 'accounts'

urlpatterns = [
    path('users', UserApiView.as_view(), name="users_api"),
    path('users/<pk>', UserApiDetailView.as_view(), name="user_detail"),
    # path('users/<pk>/deactivate', UserApiDeactView.as_view(), name="user_deact"),
    # path('users/<pk>/update', UserApiUpdateView.as_view(), name="user_update"),
    # path('users/<pk>/reset', UserApiResetView.as_view(), name="user_pass_reset"),
    path('register', RegisterApiView.as_view(), name="register"),
]