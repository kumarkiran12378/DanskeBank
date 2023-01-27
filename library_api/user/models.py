from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    """
    User model custom manager.
    """

    def create(self, **validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = User(**validated_data)
        user.save()
        return user


class User(AbstractBaseUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('uid','password')
    uid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=127)
    email = models.EmailField(max_length=63, unique=True)
    mobile_no = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=127)
    status = models.SmallIntegerField()
    islibrarian = models.BooleanField()

    objects = UserManager()
    
    class Meta:
        db_table = 'user'
    