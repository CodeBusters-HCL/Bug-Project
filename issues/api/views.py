from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from issues.models import Issue
from issues.api.serializers import IssueSerializer


class IssueApiView(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetailApiView(RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_field = 'issue_title'
    lookup_url_kwarg = 'abc'

class IssueDeleteApiView(DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_field = 'issue_title'
    lookup_url_kwarg = 'abc'

class IssueUpdateApiView(UpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_field = 'issue_title'
    lookup_url_kwarg = 'abc'