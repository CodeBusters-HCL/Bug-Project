from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from .permissions import IsOwnerOrReadOnly


from issues.models import Issue
from issues.api.serializers import IssueSerializer, IssueCreateSerializer

class IssueCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Issue.objects.all()
    serializer_class = IssueCreateSerializer

    def perform_create(self, serializer):
        serializer.save(issuer=self.request.user)

class IssueApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetailApiView(RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_field = 'issue_title'
    lookup_url_kwarg = 'abc'

class IssueDeleteApiView(DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    lookup_field = 'issue_title'
    lookup_url_kwarg = 'abc'

class IssueUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = IssueCreateSerializer
    lookup_field = 'issue_title'
    lookup_url_kwarg = 'abc'