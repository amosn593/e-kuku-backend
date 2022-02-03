from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, user_name, password, ** extra_fields):
        extra_fields.setdefault('is_active', True)
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          is_active=True)
        user.set_password(password)
        user.is_active = True
        user.save()

        return user

    def create_superuser(self, email, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        user = self.create_user(
            email, user_name, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    user_name = models.CharField(max_length=8)
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def get_user_name(self):
        return self.user_name

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.email
