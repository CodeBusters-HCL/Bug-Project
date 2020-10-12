from django.urls import path

from issues.api.views import IssueApiView, IssueDetailApiView, IssueDeleteApiView, IssueUpdateApiView

app_name = 'accounts'

urlpatterns = [
    path('issues', IssueApiView.as_view(), name="issues_api"),
    path('issues/<abc>', IssueDetailApiView.as_view(), name="issue-detail"),
    path('issues/<abc>/delete', IssueDeleteApiView.as_view(), name="issue-delete"),
    path('issues/<abc>/edit', IssueUpdateApiView.as_view(), name="issue-update"),
]