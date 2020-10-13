from rest_framework import serializers
from accounts.models import User, MyUserManager
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User as django_user

# User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = { 'input_type': 'password' } )
    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
        extra_kwargs = {
            "password":{"write_only":True}
            }

    def create(self,validated_data):
        username=validated_data['username']
        email=validated_data['email']
        password = validated_data.pop('password')
        user = User(
                    username=username,
                    email=email,
                )
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = { 'input_type': 'password' } )

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            "password":{"write_only":True}
            }