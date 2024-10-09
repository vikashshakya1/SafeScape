# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=150, blank=True, null=True)
#     phonenumber = models.CharField(max_length=15, blank=True, null=True)


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150, blank=True, null=True)
    phonenumber = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")]
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username  # Or return self.email or self.name based on your preference
