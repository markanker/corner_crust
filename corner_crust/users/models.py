from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.TextField(max_length=20, unique=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=1, null=True, blank=True)
