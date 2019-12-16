from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.db import transaction
from django.contrib.auth.models import (
AbstractBaseUser, PermissionsMixin, BaseUserManager
)
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError('This Value Must be set')
        try:
            with transaction.atomic():
                user = self.model(email= email, **extra_field)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
    def create_user(self, email, password=None, **extra_field):
        extra_field.setdefault('is_staff', False)
        extra_field.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_field)
    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_staff',True)
        extra_field.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_field)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    isActive = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dateOfJoin = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *agrs, **kwargs):
        super(User, self).save(*agrs, **kwargs)
        return self
# Create your models here.
