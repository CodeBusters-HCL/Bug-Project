
from django.urls import path
from . import views


urlpatterns = [
    path('report_issue',views.report_issue, name= 'report_issue'),
    path('accounts/dashboard',views.dashboard, name= 'dashboard'),
    path('accounts/assigned_to_me',views.assigned_to_me, name= 'assigned_to_me'),
    path('accounts/issued_by_me',views.issued_by_me, name= 'issued_by_me'),
    path('accounts/search', views.search, name='search'),
    path('accounts/profile', views.profile, name='my_account'),
    path('<uuid:issue_id>',views.onebug, name= 'onebug'),
]
