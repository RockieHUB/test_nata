from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class AkunManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, **extra_fields)

class Akun(AbstractBaseUser):
    fullname = models.CharField(null=False, max_length=100)
    email = models.EmailField(unique=True, null=False)
    phoneNumber = models.CharField(max_length=25)
    password = models.CharField(null=False, max_length=100)
    userRole = models.CharField(null=False, max_length=10)

    objects = AkunManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'phoneNumber', 'password', 'userRole']

    def __str__(self):
        return self.email

    def has_perm(self):
        return True

    def has_module_perms(self):
        return True