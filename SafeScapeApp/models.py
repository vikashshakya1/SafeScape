from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
