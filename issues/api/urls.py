from django.urls import path

from issues.api.views import IssueApiView, IssueDetailApiView, IssueDeleteApiView, IssueUpdateApiView, IssueCreateApiView

app_name = 'accounts'

urlpatterns = [
    path('issues', IssueApiView.as_view(), name="issues-list"),
    path('create', IssueCreateApiView.as_view(), name="issues-create"),
    path('issues/<abc>', IssueDetailApiView.as_view(), name="issue-detail"),
    path('issues/<abc>/delete', IssueDeleteApiView.as_view(), name="issue-delete"),
    path('issues/<abc>/edit', IssueUpdateApiView.as_view(), name="issue-update"),
]