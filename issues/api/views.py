from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from issues.models import Issue
from issues.api.serializers import IssueSerializer


class IssueApiView(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer