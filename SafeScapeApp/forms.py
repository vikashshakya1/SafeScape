from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Is_Admin = models.BooleanField('Is Admin',default=False)
    Is_Civilian = models.BooleanField('Is Civilian',default=False)
    Is_LawEnforcement = models.BooleanField('Is_LawEnforcement',default=False)