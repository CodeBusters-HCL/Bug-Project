from django.db import models # commentout all the below code if inbuilt user is needed
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class MyUserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, username, staff_req=False, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
               first_name=first_name,
               last_name=last_name,
               email=self.normalize_email(email),
               username=username,
               staff_req=staff_req,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
               first_name=first_name,
               last_name=last_name,
               email=self.normalize_email(email),
               password=password,
               username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(verbose_name='email',max_length=255, unique=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    staff_req = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', ]

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def har_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
