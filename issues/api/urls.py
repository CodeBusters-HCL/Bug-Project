from django.urls import path

from issues.api.views import IssueApiView

app_name = 'accounts'

urlpatterns = [
    path('issues', IssueApiView.as_view(), name="issues_api"),
]