
from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views       #to use the django inbuilt password reset feature


urlpatterns = [
    path('accounts/login',views.login, name= 'login'),
    path('accounts/login/',views.login, name= 'login'),
    path('accounts/register',views.register, name= 'register'),
    
    path('accounts/logout',views.logout, name= 'logout'),
    path('dactivate/', views.deactivate, name='deactivate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),
]
# in the above paths use template_name="path/to/html/template" parameter in as_view() function to use custom html templates instead of django admin templates