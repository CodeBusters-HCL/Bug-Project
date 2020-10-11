from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from accounts.models import User, MyUserManager
from accounts.api.serializers import UserSerializer, RegistrationSerializer


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserApiDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterApiView(CreateAPIView):
    queryset = User.objects.last()
    serializer_class = RegistrationSerializer

# @api_view(['POST', ])
# def registration_view(request):

#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data = request.data)
#         data = {}
#         if serializer.is_valid():
#             user = serializer.save()
#             data['response'] = "successfully registered"
#             data['email'] = user.email
#             data['username'] = user.username
#         else:
#             data = serializer.errors
#         return Response(data)
