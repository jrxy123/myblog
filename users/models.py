from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.username