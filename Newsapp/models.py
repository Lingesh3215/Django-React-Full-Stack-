from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,AbstractUser
from django.contrib.auth.hashers import check_password, make_password


class RoleModel(models.Model):
    role_name = models.CharField(max_length=50)


class UserModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE, default=1)
    is_active=models.BooleanField(default=True)
    is_anonymous=models.BooleanField(default=True)
    is_authenticated=models.BooleanField(default=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    

class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    category=models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
